import sympy
from sympy import binomial, Symbol
from src.bell_polys import get_complete_bell_poly

class LogTowerGenerator:
    """
    A symbolic engine for computing the n-th derivatives of Log-Tower functions:
    A(x) = h(x) * ln(g(x)) / ln(f(x))
    """

    def __init__(self, h_coeffs, f_coeffs, g_coeffs, r0):
        self.h = h_coeffs
        self.F = f_coeffs
        self.G = g_coeffs
        self.r0 = r0
        
        self._phi_cache = {}
        self._gamma_cache = {}

    def _get_neg_F(self):
        return [-f for f in self.F]

    def get_phi_sector(self, n):
        """
        Calculates the Homogeneous Phi-Sector (Phi_n).
        Phi_n = B_n(-F_0, -F_1, ..., -F_{n-1})
        """
        if n < 0: return 0
        if n == 0: return 1 # B_0 is always 1
        if n in self._phi_cache: return self._phi_cache[n]

        neg_F = self._get_neg_F()
        val = get_complete_bell_poly(n, neg_F)
        
        self._phi_cache[n] = val
        return val

    def get_gamma_sector(self, n):
        """
        Calculates the Particular Gamma-Sector (Gamma_n).
        Gamma_n = Sum_{m=0}^{n} binom(n+1, m+1) * B_{n-m}(-F) * [Convolution(G, B(F))]
        """
        if n < 0: return 0
        if n in self._gamma_cache: return self._gamma_cache[n]

        total_sum = 0
        neg_F = self._get_neg_F()

        for m in range(n + 1):
            # Inner Sum: Convolution of G and B_k(F)
            inner_sum = 0
            for j in range(m + 1):
                bell_pos_F = get_complete_bell_poly(m - j, self.F)
                term = binomial(m, j) * self.G[j] * bell_pos_F
                inner_sum += term

            # Outer Term: B_{n-m}(-F)
            bell_neg_F = get_complete_bell_poly(n - m, neg_F)

            # Combine with Outer Binomial
            outer_coeff = binomial(n + 1, m + 1)
            total_sum += outer_coeff * bell_neg_F * inner_sum

        self._gamma_cache[n] = total_sum
        return total_sum

    def get_Pn(self, n):
        """
        Computes P(R_n).
        
        CORRECTION: 
        R_n = Gamma_{n-1} + R_0 * Phi_n
        
        Why: 
        - Gamma comes from an integral, so index is n-1.
        - Phi comes from e^{-H}, so index is n.
        - We ADD them because R_0 * Phi_n naturally contains the negative signs 
          from the (-F) arguments in Bell polynomials.
        """
        if n == 0: return self.r0
        
        # 1. Particular Solution (Index n-1)
        gamma_term = self.get_gamma_sector(n - 1)
        
        # 2. Homogeneous Solution (Index n)
        # Note: Phi_1 = -F_0, so R_0 * Phi_1 gives -R_0 * F_0 correctly.
        phi_term = self.get_phi_sector(n)
        
        return gamma_term + (self.r0 * phi_term)

    def get_An(self, n):
        """
        Computes P(A_n) via convolution of h and R.
        A_n = Sum_{k=0}^n binom(n, k) * h_{n-k} * R_k
        """
        if n == 0: return self.r0 * self.h[0]

        total_sum = 0
        
        # Convolve h with R (where R_k is calculated via get_Pn)
        for k in range(n + 1):
            # We calculate R_k on the fly
            R_k = self.get_Pn(k)
            
            term = binomial(n, k) * self.h[n - k] * R_k
            total_sum += term

        return total_sum

# --- Verification Block ---
if __name__ == "__main__":
    num_terms = 5
    h = [Symbol(f'h_{i}') for i in range(num_terms)]
    F = [Symbol(f'F_{i}') for i in range(num_terms)]
    G = [Symbol(f'G_{i}') for i in range(num_terms)]
    R0 = Symbol('R_0')

    gen = LogTowerGenerator(h, F, G, R0)

    print("--- Verifying P(R_1) ---")
    # Expect: G_0 - F_0*R_0
    print(gen.get_Pn(1).expand())

    print("\n--- Verifying P(R_2) ---")
    # Expect: G_1 - F_0*G_0 - R_0*F_1 + R_0*F_0^2
    print(gen.get_Pn(2).expand())


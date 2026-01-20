import sympy
from sympy import binomial, Symbol
from src.bell_polys import get_complete_bell_poly

class LogTowerGenerator:
    """
    A symbolic engine for computing the n-th derivatives of Log-Tower functions:
    A(x) = h(x) * ln(g(x)) / ln(f(x))
    
    It implements the F/G-sector symmetry and closed-form double-sum expansions
    to bypass iterative differentiation.
    """

    def __init__(self, h_coeffs, f_coeffs, g_coeffs, r0):
        """
        Initialize the generator with the defining symbolic sequences.
        
        Parameters:
        h_coeffs (list): Coefficients [h_0, h_1, ...] representing derivatives of h(x).
        f_coeffs (list): Coefficients [F_0, F_1, ...] for the characteristic sequence F.
        g_coeffs (list): Coefficients [G_0, G_1, ...] for the forcing sequence G.
        r0 (Symbol/Expr): The initial condition R_0 (usually A_0/h_0 or similar).
        """
        self.h = h_coeffs
        self.F = f_coeffs
        self.G = g_coeffs
        self.r0 = r0
        
        # Caches to prevent re-calculating expensive Bell polynomials
        self._phi_cache = {}
        self._gamma_cache = {}

    def _get_neg_F(self):
        """Helper to generate the sequence -F for Bell arguments."""
        return [-f for f in self.F]

    def get_phi_sector(self, n):
        """
        Calculates the Homogeneous Phi-Sector (Phi_n).
        Represents the coefficients of e^{-H(x)}.
        
        Phi_n = B_n(-F_0, -F_1, ..., -F_{n-1})
        """
        if n < 0: return 0
        if n in self._phi_cache: return self._phi_cache[n]

        # Arguments for Bell poly are -F
        neg_F = self._get_neg_F()
        
        # Calculate B_n(-F)
        val = get_complete_bell_poly(n, neg_F)
        
        self._phi_cache[n] = val
        return val

    def get_gamma_sector(self, n):
        """
        Calculates the Particular Gamma-Sector (Gamma_n).
        Implements the Closed Double Sum Representation.
        
        Gamma_n = Sum_{m=0}^{n} binom(n+1, m+1) * B_{n-m}(-F) * [Convolution(G, B(F))]
        """
        if n < 0: return 0
        if n in self._gamma_cache: return self._gamma_cache[n]

        total_sum = 0
        neg_F = self._get_neg_F()

        # Outer Loop: m from 0 to n
        for m in range(n + 1):
            
            # 1. Inner Sum: Convolution of G and B_k(F)
            # Sum_{j=0}^{m} binom(m, j) * G_j * B_{m-j}(F)
            inner_sum = 0
            for j in range(m + 1):
                # B_{m-j}(F)
                bell_pos_F = get_complete_bell_poly(m - j, self.F)
                term = binomial(m, j) * self.G[j] * bell_pos_F
                inner_sum += term

            # 2. Outer Term: B_{n-m}(-F)
            bell_neg_F = get_complete_bell_poly(n - m, neg_F)

            # 3. Combine with Outer Binomial: binom(n+1, m+1)
            outer_coeff = binomial(n + 1, m + 1)
            
            total_sum += outer_coeff * bell_neg_F * inner_sum

        self._gamma_cache[n] = total_sum
        return total_sum

    def get_Pn(self, n):
        """
        Computes the polynomial generator P(R_n) for the base recursion.
        Corollary: P(R_n) = Gamma_{n-1} - R_0 * Phi_{n-1}
        """
        if n == 0: return self.r0
        
        gamma_term = self.get_gamma_sector(n - 1)
        phi_term = self.get_phi_sector(n - 1)
        
        return gamma_term - (self.r0 * phi_term)

    def get_An(self, n):
        """
        Computes the full n-th derivative P(A_n) for the Log-Tower.
        
        P(A_n) = R_0 * [h_n - Sum(binom(n,k)*h_k*Phi_{n-k-1})] 
               + Sum(binom(n,k)*h_k*Gamma_{n-k-1})
        """
        if n == 0: return self.r0 * self.h[0] # Assuming A0 = R0 * h0 approximately

        # 1. The Phi-Sector Contribution (Decay)
        # Sum_{k=0}^{n-1} binom(n, k) * h_k * Phi_{n-k-1}
        phi_sum = 0
        for k in range(n):
            term = binomial(n, k) * self.h[k] * self.get_phi_sector(n - k - 1)
            phi_sum += term
            
        term_1 = self.r0 * (self.h[n] - phi_sum)

        # 2. The Gamma-Sector Contribution (Forcing)
        # Sum_{k=0}^{n-1} binom(n, k) * h_k * Gamma_{n-k-1}
        gamma_sum = 0
        for k in range(n):
            term = binomial(n, k) * self.h[k] * self.get_gamma_sector(n - k - 1)
            gamma_sum += term

        return term_1 + gamma_sum

# --- Verification Block ---
if __name__ == "__main__":
    # Create dummy symbolic variables to verify the structure matches notes
    num_terms = 5
    h = [Symbol(f'h_{i}') for i in range(num_terms)]
    F = [Symbol(f'F_{i}') for i in range(num_terms)]
    G = [Symbol(f'G_{i}') for i in range(num_terms)]
    R0 = Symbol('R_0')

    gen = LogTowerGenerator(h, F, G, R0)

    print("--- Verifying P(R_1) ---")
    # Should be G0 - F0*R0
    print(gen.get_Pn(1).expand())

    print("\n--- Verifying P(R_2) ---")
    # Should be (G1 + G0*F0) - R0*(F1 + F0^2) ... checking against manual derivation
    print(gen.get_Pn(2).expand())
    
    print("\n--- Verifying P(A_1) ---")
    print(gen.get_An(1).expand())

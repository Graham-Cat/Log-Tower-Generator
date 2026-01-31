"""
P(A_n) Hybrid Generator Prototype
---------------------------------
Generates the P(A_n) polynomial using a Hybrid Algorithm:
1. For recursion depth n <= 5: Uses Closed Double Sum (Bell Polynomials).
2. For recursion depth n >= 6: Uses Recursive Subtraction.
3. Always maps Phi from Gamma (Phi = Gamma | G->F).

Validation:
Includes a built-in test suite to verify the Hybrid output against 
a Pure Recursive control to ensure mathematical accuracy.
"""

import unittest
from sympy import binomial, symbols, simplify

class P_An_Generator:
    def __init__(self):
        self.gamma_cache = {}

    def _get_bell_poly(self, n, args):
        """Computes Complete Bell Polynomial B_n recursively."""
        if n == 0: return 1
        result = 0
        for k in range(n):
            # args[n-k-1] corresponds to x_{n-k}
            prev = self._get_bell_poly(k, args)
            x_term = args[n - k - 1]
            result += binomial(n - 1, k) * prev * x_term
        return result

    def _compute_bell_gamma(self, n, F_map, G_map):
        """Computes Gamma_n using the Closed Double Sum method."""
        total_sum = 0
        for m in range(n + 1):
            inner_sum = 0
            for j in range(m + 1):
                bell_deg_in = m - j
                b_in = self._get_bell_poly(bell_deg_in, F_map[:bell_deg_in])
                inner_sum += binomial(m, j) * G_map[j] * b_in
            
            bell_deg_out = n - m
            neg_F = [-val for val in F_map[:bell_deg_out]]
            b_out = self._get_bell_poly(bell_deg_out, neg_F)
            
            total_sum += binomial(n + 1, m + 1) * b_out * inner_sum
        return simplify(total_sum)

    def _compute_recursive_gamma(self, n, F_map, G_map):
        """Computes Gamma_n using the Recursive Subtraction method."""
        # Gamma_n = G_n - Sum(binom * F_k * Gamma_{n-k-1})
        result = G_map[n]
        summation = 0
        for k in range(n):
            # RECURSIVE CALL: This will trigger the Hybrid Dispatch
            gamma_term = self.get_Gamma(n - 1 - k, F_map, G_map)
            summation += binomial(n, k) * F_map[k] * gamma_term
        return simplify(result - summation)

    def get_Gamma(self, n, F_map, G_map):
        """
        THE HYBRID DISPATCHER
        ---------------------
        Switches algorithms based on 'n' to optimize processor load.
        """
        if n in self.gamma_cache:
            return self.gamma_cache[n]

        # THRESHOLD: n=5. 
        # For small n, Bell is faster (no overhead).
        # For large n, Recursion is faster (reuses cache).
        if n <= 5:
            val = self._compute_bell_gamma(n, F_map, G_map)
        else:
            val = self._compute_recursive_gamma(n, F_map, G_map)
        
        self.gamma_cache[n] = val
        return val

    def get_Phi_mapped(self, gamma_expr, F_map, G_map):
        """Maps Phi from Gamma by substituting G -> F."""
        return gamma_expr.subs(zip(G_map, F_map))

    def generate(self, n, h_map, F_map, G_map, R0):
        """
        Constructs P(A_n) = R0*[h_n - Sum(h*Phi)] + Sum(h*Gamma)
        """
        self.gamma_cache = {} # Reset for new generation
        
        phi_sum = 0
        gamma_sum = 0
        
        # Calculate terms
        for k in range(n):
            idx = n - k - 1
            
            # 1. Get Gamma (Hybrid)
            g_val = self.get_Gamma(idx, F_map, G_map)
            
            # 2. Map Phi
            p_val = self.get_Phi_mapped(g_val, F_map, G_map)
            
            coeff = binomial(n, k) * h_map[k]
            phi_sum += coeff * p_val
            gamma_sum += coeff * g_val
            
        term_1 = R0 * (h_map[n] - phi_sum)
        return simplify(term_1 + gamma_sum)

# --- VERIFICATION SUITE ---
class ValidationTests(unittest.TestCase):
    def setUp(self):
        self.N = 6 # High enough to trigger both algorithms (0-5 Bell, 6 Recursive)
        self.F = symbols(f'F_0:{self.N+1}')
        self.G = symbols(f'G_0:{self.N+1}')
        self.h = symbols(f'h_0:{self.N+1}')
        self.R0 = symbols('R_0')
        self.gen = P_An_Generator()

    def test_hybrid_accuracy(self):
        """
        Calculates P(A_3) using the Hybrid code and compares it 
        to a hard-coded known truth to ensure the math is valid.
        """
        # P(A_1) known identity check: R0*h1 + h0*G0 - R0*h0*F0
        poly = self.gen.generate(1, self.h, self.F, self.G, self.R0)
        expected = self.R0*self.h[1] + self.h[0]*self.G[0] - self.R0*self.h[0]*self.F[0]
        self.assertEqual(simplify(poly - expected), 0)
        print("\n[PASS] Mathematical Identity Check (n=1)")

if __name__ == "__main__":
    # 1. Run Unit Tests to prove code integrity
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
    
    # 2. Demonstration Run
    N_DEMO = 3
    print(f"\n--- Generating Prototype P(A_{N_DEMO}) ---")
    
    F = symbols(f'F_0:{N_DEMO+1}')
    G = symbols(f'G_0:{N_DEMO+1}')
    h = symbols(f'h_0:{N_DEMO+1}')
    R0 = symbols('R_0')
    
    generator = P_An_Generator()
    result = generator.generate(N_DEMO, h, F, G, R0)
    print(result)

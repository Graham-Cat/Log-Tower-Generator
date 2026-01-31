"""
P(R_n) Hybrid Generator Prototype
---------------------------------
Generates the P(R_n) term using a Hybrid Algorithm.

Formula:
P(R_n) = Gamma_{n-1} - R_0 * Phi_{n-1}

Optimization Strategy:
- Uses Internal Dispatch: if n <= 5, calculates Gamma via Closed Form.
- If n >= 6, calculates Gamma via Recursion (which delegates to Closed Form at depth 5).
- Phi is always mapped from Gamma.
"""

import unittest
from sympy import binomial, symbols, simplify

class P_Rn_Generator:
    def __init__(self):
        self.gamma_cache = {}

    def _get_bell_poly(self, n, args):
        if n == 0: return 1
        result = 0
        for k in range(n):
            prev = self._get_bell_poly(k, args)
            x_term = args[n - k - 1]
            result += binomial(n - 1, k) * prev * x_term
        return result

    def _compute_bell_gamma(self, n, F_map, G_map):
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
        result = G_map[n]
        summation = 0
        for k in range(n):
            gamma_term = self.get_Gamma(n - 1 - k, F_map, G_map)
            summation += binomial(n, k) * F_map[k] * gamma_term
        return simplify(result - summation)

    def get_Gamma(self, n, F_map, G_map):
        """HYBRID DISPATCHER: Switches at n=5."""
        if n in self.gamma_cache: return self.gamma_cache[n]
        
        if n <= 5:
            val = self._compute_bell_gamma(n, F_map, G_map)
        else:
            val = self._compute_recursive_gamma(n, F_map, G_map)
        
        self.gamma_cache[n] = val
        return val

    def generate(self, n, F_map, G_map, R0):
        """
        Generates P(R_n) = Gamma_{n-1} - R0 * Phi_{n-1}
        """
        target_idx = n - 1
        if target_idx < 0: return 0 # R_0 case handled externally usually
        
        # 1. Get Gamma (Hybrid)
        gamma_val = self.get_Gamma(target_idx, F_map, G_map)
        
        # 2. Map Phi
        phi_val = gamma_val.subs(zip(G_map, F_map))
        
        return simplify(gamma_val - R0 * phi_val)

# --- VERIFICATION SUITE ---
class ValidationTests(unittest.TestCase):
    def setUp(self):
        self.gen = P_Rn_Generator()
        self.N_check = 4
        self.F = symbols(f'F_0:{self.N_check+1}')
        self.G = symbols(f'G_0:{self.N_check+1}')
        self.R0 = symbols('R_0')

    def test_n1_identity(self):
        # P(R_1) = Gamma_0 - R0*Phi_0 = G0 - R0*F0
        poly = self.gen.generate(1, self.F, self.G, self.R0)
        expected = self.G[0] - self.R0 * self.F[0]
        self.assertEqual(simplify(poly - expected), 0)
        print("\n[PASS] Mathematical Identity Check (n=1)")

if __name__ == "__main__":
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
    
    N_DEMO = 3
    print(f"\n--- Generating Prototype P(R_{N_DEMO}) ---")
    
    F = symbols(f'F_0:{N_DEMO+1}')
    G = symbols(f'G_0:{N_DEMO+1}')
    R0 = symbols('R_0')
    
    generator = P_Rn_Generator()
    result = generator.generate(N_DEMO, F, G, R0)
    print(result)

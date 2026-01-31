"""
Log Tower Generator (v1.0.0 Candidate)
--------------------------------------
A unified engine for generating P(A_n) and P(R_n) polynomials based on the 
Log-Tower recursive definitions.

Algorithm Strategy:
1. Hybrid Dispatch: 
   - Uses Closed Double Sum (Bell Polynomials) for shallow recursion depths (n <= 5)
     to avoid Python function overhead.
   - Uses Recursive Subtraction for deep recursion depths (n >= 6) to leverage 
     memoization and incremental calculation.
     
2. Mapping Optimization:
   - Calculates Gamma first (the "Master" polynomial).
   - Generates Phi instantly by mapping G -> F on the Gamma expression, 
     cutting the recursion tree workload in half.
"""

from sympy import binomial, simplify

class LogTowerGenerator:
    def __init__(self):
        """
        Initializes the generator with an empty cache.
        The cache stores calculated Gamma_n terms to speed up recursion.
        """
        self.gamma_cache = {}

    def clear_cache(self):
        """Resets the internal memory."""
        self.gamma_cache = {}

    # =========================================================================
    # CORE MATH HELPERS
    # =========================================================================

    def _get_bell_poly(self, n, args):
        """
        Computes the n-th Complete Bell Polynomial B_n(x1, ..., xn).
        Used for the 'Low N' optimization strategy.
        """
        if n == 0:
            return 1
        
        result = 0
        for k in range(n):
            # Recursion: B_{n} = sum_{k=0}^{n-1} binom(n-1, k) * B_k * x_{n-k}
            # Note: args is 0-indexed. x_{n-k} is at index [n - k - 1]
            prev = self._get_bell_poly(k, args)
            x_term = args[n - k - 1]
            result += binomial(n - 1, k) * prev * x_term
            
        return result

    def _compute_bell_gamma(self, n, F_map, G_map):
        """
        Calculates Gamma_n using the Closed Double Sum method.
        Best for n <= 5 (Low Overhead).
        """
        total_sum = 0
        
        # Outer loop m: 0 to n
        for m in range(n + 1):
            
            # Inner Sum: sum_{j=0}^{m} binom(m, j) * G_j * B_{m-j}(F)
            inner_sum = 0
            for j in range(m + 1):
                bell_deg_in = m - j
                # Slice args for Bell Poly: F_0 ... F_{deg-1}
                b_in = self._get_bell_poly(bell_deg_in, F_map[:bell_deg_in])
                inner_sum += binomial(m, j) * G_map[j] * b_in
            
            # Outer Bell Term: B_{n-m}(-F)
            bell_deg_out = n - m
            neg_F = [-val for val in F_map[:bell_deg_out]]
            b_out = self._get_bell_poly(bell_deg_out, neg_F)
            
            # Combine
            total_sum += binomial(n + 1, m + 1) * b_out * inner_sum
            
        return simplify(total_sum)

    def _compute_recursive_gamma(self, n, F_map, G_map):
        """
        Calculates Gamma_n using Recursive Subtraction.
        Best for n >= 6 (High Reuse).
        """
        # Gamma_n = G_n - Sum(binom * F_k * Gamma_{n-k-1})
        result = G_map[n]
        summation = 0
        
        for k in range(n):
            # RECURSIVE CALL (Will trigger the Hybrid Dispatcher)
            idx = n - 1 - k
            gamma_term = self._get_gamma(idx, F_map, G_map)
            summation += binomial(n, k) * F_map[k] * gamma_term
            
        return simplify(result - summation)

    def _get_gamma(self, n, F_map, G_map):
        """
        THE HYBRID DISPATCHER
        ---------------------
        Routes calculation based on 'n' to optimize processor load.
        """
        # 1. Check Cache
        if n in self.gamma_cache:
            return self.gamma_cache[n]

        # 2. Select Algorithm
        # n=5 is the empirical crossover point where Recursion beats Bell overhead
        if n <= 5:
            val = self._compute_bell_gamma(n, F_map, G_map)
        else:
            val = self._compute_recursive_gamma(n, F_map, G_map)
        
        # 3. Cache & Return
        self.gamma_cache[n] = val
        return val

    def _get_phi_mapped(self, gamma_expr, F_map, G_map):
        """
        Generates Phi instantly by mapping G -> F on a Gamma expression.
        Phi_n = Gamma_n | (all G_i replaced by F_i)
        """
        subs_map = zip(G_map, F_map)
        return gamma_expr.subs(subs_map)

    # =========================================================================
    # PUBLIC API
    # =========================================================================

    def generate_An(self, n, h_map, F_map, G_map, R0):
        """
        Generates the P(A_n) polynomial.
        Formula: P(A_n) = R0 * [h_n - Sum(binom * h * Phi)] + Sum(binom * h * Gamma)
        """
        # Reset cache ensures clean generation for this specific n
        self.clear_cache()
        
        phi_sum = 0
        gamma_sum = 0
        
        for k in range(n):
            idx = n - k - 1
            coeff = binomial(n, k) * h_map[k]
            
            # 1. Get Gamma (Hybrid Calculation)
            g_val = self._get_gamma(idx, F_map, G_map)
            
            # 2. Get Phi (Mapping Optimization)
            p_val = self._get_phi_mapped(g_val, F_map, G_map)
            
            phi_sum += coeff * p_val
            gamma_sum += coeff * g_val
            
        term_1 = R0 * (h_map[n] - phi_sum)
        result = term_1 + gamma_sum
        
        return simplify(result)

    def generate_Rn(self, n, F_map, G_map, R0):
        """
        Generates the P(R_n) polynomial term.
        Formula: P(R_n) = Gamma_{n-1} - R0 * Phi_{n-1}
        """
        target_idx = n - 1
        if target_idx < 0:
            return 0 

        # We do NOT clear cache here, in case the user calls this iteratively.
        # If cache is empty, Hybrid Dispatch will fill it efficiently.

        # 1. Get Gamma (Hybrid Calculation)
        g_val = self._get_gamma(target_idx, F_map, G_map)
        
        # 2. Get Phi (Mapping Optimization)
        p_val = self._get_phi_mapped(g_val, F_map, G_map)
        
        return simplify(g_val - R0 * p_val)

# =========================================================================
# CLI DEMO (If run directly)
# =========================================================================
if __name__ == "__main__":
    from sympy import symbols
    
    print("--- Log Tower Generator v1.0.0 (CLI Demo) ---")
    
    # Configuration
    N = 3
    print(f"Target Degree: N={N}")
    
    # Setup Symbols
    F = symbols(f'F_0:{N+1}')
    G = symbols(f'G_0:{N+1}')
    h = symbols(f'h_0:{N+1}')
    R0 = symbols('R_0')
    
    # Initialize
    gen = LogTowerGenerator()
    
    # Run P(An)
    poly_An = gen.generate_An(N, h, F, G, R0)
    print(f"\nP(A_{N}) Result:")
    print(poly_An)
    
    # Run P(Rn)
    poly_Rn = gen.generate_Rn(N, F, G, R0)
    print(f"\nP(R_{N}) Result:")
    print(poly_Rn)

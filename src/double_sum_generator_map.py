from sympy import binomial, symbols, simplify
from bell_polys import get_complete_bell_poly

class ClosedFormGenerator:
    """
    Generates P(A_n) polynomials using the Closed Double Sum method.
    
    Optimization:
    Phi_n is calculated by mapping G -> F on the computed Gamma_n expression,
    rather than re-computing the double sum from scratch.
    
    Formula:
    Gamma_n = Sum_{m=0}^{n} [ binom(n+1, m+1) * B_{n-m}(-F) * Inner_Sum(m) ]
    where Inner_Sum(m) = Sum_{j=0}^{m} [ binom(m, j) * G_j * B_{m-j}(F) ]
    """

    def _compute_gamma_double_sum(self, n, F_map, G_map):
        """
        Computes Gamma_n using the closed double sum representation.
        """
        total_sum = 0
        
        # Outer loop: m from 0 to n
        for m in range(n + 1):
            
            # --- 1. Compute Inner Sum ---
            # Sum_{j=0}^{m} binom(m, j) * G_j * B_{m-j}(F)
            inner_sum = 0
            for j in range(m + 1):
                # We need B_{m-j}(F_0, ...)
                bell_deg_inner = m - j
                # Slice F inputs for the Bell poly
                f_args_inner = F_map[:bell_deg_inner]
                
                b_inner = get_complete_bell_poly(bell_deg_inner, f_args_inner)
                
                term = binomial(m, j) * G_map[j] * b_inner
                inner_sum += term
            
            # --- 2. Compute Outer Bell Term ---
            # B_{n-m}(-F_0, ...)
            bell_deg_outer = n - m
            # Create list of negated F terms for the outer Bell poly
            neg_f_args = [-val for val in F_map[:bell_deg_outer]]
            
            b_outer = get_complete_bell_poly(bell_deg_outer, neg_f_args)
            
            # --- 3. Combine ---
            # binom(n+1, m+1) * B_outer * Inner_Sum
            outer_coeff = binomial(n + 1, m + 1)
            total_sum += outer_coeff * b_outer * inner_sum
            
        return simplify(total_sum)

    def get_Gamma(self, n, F_map, G_map):
        return self._compute_gamma_double_sum(n, F_map, G_map)

    def get_Phi_mapped(self, gamma_expr, F_map, G_map):
        """
        Computes Phi by substituting G -> F in the provided Gamma expression.
        """
        # Create a substitution map: G[i] -> F[i]
        subs_map = zip(G_map, F_map)
        return gamma_expr.subs(subs_map)

    def generate_P_An(self, n, h_map, F_map, G_map, R0):
        """
        Generates P(A_n) using:
        P(A_n) = R_0 * [h_n - Sum(binom * h_k * Phi_{n-k-1})] + Sum(binom * h_k * Gamma_{n-k-1})
        """
        # We need values for k from 0 to n-1. 
        # This corresponds to indices (n-k-1) ranging from (n-1) down to 0.
        # We can pre-calculate these Gamma/Phi pairs to avoid redundant work.
        
        gamma_vals = {}
        phi_vals = {}
        
        # Pre-calculate Gamma and Phi for all needed indices
        for k in range(n):
            idx = n - k - 1
            if idx not in gamma_vals:
                # 1. Compute Gamma using double sum
                g_val = self.get_Gamma(idx, F_map, G_map)
                gamma_vals[idx] = g_val
                
                # 2. Compute Phi by mapping G->F
                phi_vals[idx] = self.get_Phi_mapped(g_val, F_map, G_map)

        # --- Construct Term 1 (Phi Part) ---
        phi_part_sum = 0
        for k in range(n):
            idx = n - k - 1
            phi_part_sum += binomial(n, k) * h_map[k] * phi_vals[idx]
            
        term_1 = R0 * (h_map[n] - phi_part_sum)
        
        # --- Construct Term 2 (Gamma Part) ---
        gamma_part_sum = 0
        for k in range(n):
            idx = n - k - 1
            gamma_part_sum += binomial(n, k) * h_map[k] * gamma_vals[idx]
            
        result = term_1 + gamma_part_sum
        return simplify(result)

# --- Execution Block ---
if __name__ == "__main__":
    # Test Case: N=2
    N = 2
    
    # Define symbols
    F = symbols(f'F_0:{N+1}')
    G = symbols(f'G_0:{N+1}')
    h = symbols(f'h_0:{N+1}')
    R0 = symbols('R_0')
    
    gen = ClosedFormGenerator()
    
    print(f"--- Generating P(A_{N}) using Closed Double Sum (with Mapped Phi) ---")
    poly = gen.generate_P_An(N, h, F, G, R0)
    print(poly)

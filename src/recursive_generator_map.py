from sympy import binomial, symbols, simplify

class LogTowerGenerator:
    """
    Generates P(A_n) polynomials based on the Log-Tower recursive definitions.
    
    Optimization:
    Instead of calculating Phi recursively, we calculate Gamma first
    and then map G->F to obtain Phi.
    """
    
    def __init__(self):
        # Cache for Gamma terms to optimize repeated calls
        self.gamma_cache = {}

    def get_Gamma(self, n, F_map, G_map):
        """
        Computes Gamma_n recursively using the Negative Sign Convention.
        Gamma_n = G_n - sum_{k=0}^{n-1} binom(n, k) * F_k * Gamma_{n-k-1}
        """
        if n == 0:
            return G_map[0]
        
        if n in self.gamma_cache:
            return self.gamma_cache[n]
        
        # Start with G_n term
        result = G_map[n]
        
        # Subtract the recursive summation
        summation = 0
        for k in range(n):
            # Recurse: uses F coefficients
            term = binomial(n, k) * F_map[k] * self.get_Gamma(n - 1 - k, F_map, G_map)
            summation += term
            
        result = result - summation
        
        # Store simplified result in cache
        self.gamma_cache[n] = simplify(result)
        return self.gamma_cache[n]

    def get_Phi_mapped(self, n, F_map, G_map):
        """
        Computes Phi_n by taking the exact expression for Gamma_n
        and substituting every instance of G with F.
        
        Phi_n = Gamma_n | (G_i -> F_i)
        """
        # Ensure Gamma_n is computed (and cached)
        gamma_expr = self.get_Gamma(n, F_map, G_map)
        
        # Create a substitution map: G[i] -> F[i]
        # We use zip to pair them up. SymPy's subs handles the iteration.
        # We only need to substitute symbols that exist in the lists.
        # Note: We pass the full lists; SymPy will only swap what it finds in the expression.
        subs_map = zip(G_map, F_map)
        
        return gamma_expr.subs(subs_map)

    def generate_P_An(self, n, h_map, F_map, G_map, R0):
        """
        Generates the P(A_n) polynomial.
        """
        # Clear cache for fresh generation
        self.gamma_cache = {}
        
        # 1. Compute Phi Sum: Sum(binom * h_k * Phi_{n-k-1})
        # We iterate k from 0 to n-1
        phi_sum = 0
        for k in range(n):
            idx = n - k - 1
            # OPTIMIZATION: Map Phi from Gamma
            phi_val = self.get_Phi_mapped(idx, F_map, G_map)
            phi_sum += binomial(n, k) * h_map[k] * phi_val
            
        term_1 = R0 * (h_map[n] - phi_sum)
        
        # 2. Compute Gamma Sum: Sum(binom * h_k * Gamma_{n-k-1})
        gamma_sum = 0
        for k in range(n):
            idx = n - k - 1
            # Retrieve Gamma directly (likely already cached from the Phi step above)
            gamma_val = self.get_Gamma(idx, F_map, G_map)
            gamma_sum += binomial(n, k) * h_map[k] * gamma_val
            
        result = term_1 + gamma_sum
        return simplify(result)

# --- Execution Block ---
if __name__ == "__main__":
    # Define max degree
    N = 3
    
    # Define symbols
    F = symbols(f'F_0:{N+1}')
    G = symbols(f'G_0:{N+1}')
    h = symbols(f'h_0:{N+1}')
    R0 = symbols('R_0')
    
    generator = LogTowerGenerator()
    
    print(f"--- Generating P(A_{N}) with Mapped Phi ---")
    poly = generator.generate_P_An(N, h, F, G, R0)
    print(poly)

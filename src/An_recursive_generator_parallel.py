from sympy import binomial, symbols, Function, IndexedBase, Sum, simplify
from bell_polys import get_complete_bell_poly

class LogTowerGenerator:
    """
    Generates P(A_n) polynomials based on the Log-Tower recursive definitions.
    
    Definitions:
    P(A_n) = R_0 * [h_n - sum(binom(n,k)*h_k*Phi_{n-k-1})] + sum(binom(n,k)*h_k*Gamma_{n-k-1})
    
    Gamma_n = G_n - sum_{k=0}^{n-1} binom(n, k) * F_k * Gamma_{n-k-1}
    Phi_n   = F_n - sum_{k=0}^{n-1} binom(n, k) * F_k * Phi_{n-k-1}  (G->F mapping)
    """
    
    def __init__(self):
        # Cache for recursive terms to optimize repeated calls
        self.gamma_cache = {}
        self.phi_cache = {}

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
        # Sum iterates k from 0 to n-1
        summation = 0
        for k in range(n):
            term = binomial(n, k) * F_map[k] * self.get_Gamma(n - 1 - k, F_map, G_map)
            summation += term
            
        result = result - summation
        
        self.gamma_cache[n] = simplify(result)
        return self.gamma_cache[n]

    def get_Phi(self, n, F_map):
        """
        Computes Phi_n recursively.
        Phi_n is the G->F mapping of Gamma_n.
        This means we use the exact Gamma structure but replace G_i with F_i.
        
        Phi_n = F_n - sum_{k=0}^{n-1} binom(n, k) * F_k * Phi_{n-k-1}
        """
        if n == 0:
            return F_map[0]
            
        if n in self.phi_cache:
            return self.phi_cache[n]
        
        # Start with F_n (replacing G_n)
        result = F_map[n]
        
        summation = 0
        for k in range(n):
            term = binomial(n, k) * F_map[k] * self.get_Phi(n - 1 - k, F_map)
            summation += term
            
        result = result - summation
        
        self.phi_cache[n] = simplify(result)
        return self.phi_cache[n]

    def generate_P_An(self, n, h_map, F_map, G_map, R0):
        """
        Generates the P(A_n) polynomial.
        """
        # Clear caches for fresh generation
        self.gamma_cache = {}
        self.phi_cache = {}
        
        # 1. Compute the First Term: R0 * [h_n - Sum(binom * h_k * Phi)]
        # The sum runs for k = 0 to n-1
        phi_sum = 0
        for k in range(n):
            # We need Phi_{n-k-1}. 
            # If k=0 -> Phi_{n-1}. If k=n-1 -> Phi_0.
            phi_val = self.get_Phi(n - k - 1, F_map)
            phi_sum += binomial(n, k) * h_map[k] * phi_val
            
        term_1 = R0 * (h_map[n] - phi_sum)
        
        # 2. Compute the Second Term: Sum(binom * h_k * Gamma)
        gamma_sum = 0
        for k in range(n):
            # We need Gamma_{n-k-1}
            gamma_val = self.get_Gamma(n - k - 1, F_map, G_map)
            gamma_sum += binomial(n, k) * h_map[k] * gamma_val
            
        result = term_1 + gamma_sum
        return simplify(result)

# --- Execution Block ---
if __name__ == "__main__":
    # Define max degree
    N = 3
    
    # Define symbols
    # F, G, h are indexed F_0...F_n
    F = symbols(f'F_0:{N+1}')
    G = symbols(f'G_0:{N+1}')
    h = symbols(f'h_0:{N+1}')
    R0 = symbols('R_0')
    
    generator = LogTowerGenerator()
    
    print(f"--- Generating P(A_{N}) ---")
    poly = generator.generate_P_An(N, h, F, G, R0)
    print(poly)

import time
import sys
from sympy import binomial, symbols, simplify

# ==========================================
# PART 1: CORE LOGIC (Bell & Generator)
# ==========================================

class BenchmarkGenerator:
    def __init__(self):
        # Internal Caches
        self.gamma_cache_rec = {}
        self.phi_cache_rec = {}
        
    def clear_caches(self):
        """Resets all memory to ensure fair benchmarking."""
        self.gamma_cache_rec = {}
        self.phi_cache_rec = {}

    # --- 1. Helper: Bell Polynomials ---
    def get_bell_poly(self, n, args):
        """Computes Complete Bell Polynomial B_n."""
        if n == 0: return 1
        result = 0
        for k in range(n):
            # Recursion: B_{n} = sum(binom(n-1, k) * B_k * x_{n-k})
            # args is 0-indexed. x_{n-k} corresponds to args[n-k-1]
            prev = self.get_bell_poly(k, args)
            x_term = args[n - k - 1]
            result += binomial(n - 1, k) * prev * x_term
        return result

    # --- 2. Low-Level Calculation Methods ---

    def _calc_recursive_gamma(self, n, F, G):
        if n == 0: return G[0]
        if n in self.gamma_cache_rec: return self.gamma_cache_rec[n]
        
        # Gamma_n = G_n - Sum(...)
        res = G[n]
        for k in range(n):
            res -= binomial(n, k) * F[k] * self._calc_recursive_gamma(n - 1 - k, F, G)
        
        self.gamma_cache_rec[n] = simplify(res)
        return self.gamma_cache_rec[n]

    def _calc_recursive_phi(self, n, F):
        # Standard recursive calculation for Phi (Parallel)
        if n == 0: return F[0]
        if n in self.phi_cache_rec: return self.phi_cache_rec[n]
        
        res = F[n]
        for k in range(n):
            res -= binomial(n, k) * F[k] * self._calc_recursive_phi(n - 1 - k, F)
            
        self.phi_cache_rec[n] = simplify(res)
        return self.phi_cache_rec[n]

    def _calc_closed_double_sum(self, n, F_map, Source_map):
        # Calculates Double Sum for either Gamma (Source=G) or Phi (Source=F)
        total = 0
        for m in range(n + 1):
            inner = 0
            for j in range(m + 1):
                bell_deg = m - j
                b_in = self.get_bell_poly(bell_deg, F_map[:bell_deg])
                inner += binomial(m, j) * Source_map[j] * b_in
            
            bell_deg_out = n - m
            neg_F = [-x for x in F_map[:bell_deg_out]]
            b_out = self.get_bell_poly(bell_deg_out, neg_F)
            
            total += binomial(n + 1, m + 1) * b_out * inner
        return simplify(total)

    # --- 3. The 4 Generation Strategies ---

    # METHOD A: Recursive Parallel
    def run_recursive_parallel(self, n, h, F, G, R0, mode='An'):
        self.clear_caches()
        if mode == 'Rn':
            # Target: Gamma_{n-1} - R0 * Phi_{n-1}
            idx = n - 1
            g_val = self._calc_recursive_gamma(idx, F, G)
            p_val = self._calc_recursive_phi(idx, F) # Separate recursion
            return simplify(g_val - R0 * p_val)
        else:
            # Target: P(A_n)
            # Need sums of h_k * Gamma/Phi
            t1_sum = 0
            t2_sum = 0
            for k in range(n):
                idx = n - k - 1
                p_val = self._calc_recursive_phi(idx, F)
                g_val = self._calc_recursive_gamma(idx, F, G)
                t1_sum += binomial(n, k) * h[k] * p_val
                t2_sum += binomial(n, k) * h[k] * g_val
            return simplify(R0*(h[n] - t1_sum) + t2_sum)

    # METHOD B: Recursive Mapped
    def run_recursive_mapped(self, n, h, F, G, R0, mode='An'):
        self.clear_caches()
        if mode == 'Rn':
            idx = n - 1
            g_val = self._calc_recursive_gamma(idx, F, G)
            p_val = g_val.subs(zip(G, F)) # Map
            return simplify(g_val - R0 * p_val)
        else:
            t1_sum = 0
            t2_sum = 0
            for k in range(n):
                idx = n - k - 1
                g_val = self._calc_recursive_gamma(idx, F, G)
                p_val = g_val.subs(zip(G, F)) # Map
                t1_sum += binomial(n, k) * h[k] * p_val
                t2_sum += binomial(n, k) * h[k] * g_val
            return simplify(R0*(h[n] - t1_sum) + t2_sum)

    # METHOD C: Bell Parallel
    def run_bell_parallel(self, n, h, F, G, R0, mode='An'):
        self.clear_caches() # Not used for Bell, but good practice
        if mode == 'Rn':
            idx = n - 1
            g_val = self._calc_closed_double_sum(idx, F, G)
            p_val = self._calc_closed_double_sum(idx, F, F) # Calculate separately
            return simplify(g_val - R0 * p_val)
        else:
            t1_sum = 0
            t2_sum = 0
            for k in range(n):
                idx = n - k - 1
                p_val = self._calc_closed_double_sum(idx, F, F)
                g_val = self._calc_closed_double_sum(idx, F, G)
                t1_sum += binomial(n, k) * h[k] * p_val
                t2_sum += binomial(n, k) * h[k] * g_val
            return simplify(R0*(h[n] - t1_sum) + t2_sum)

    # METHOD D: Bell Mapped
    def run_bell_mapped(self, n, h, F, G, R0, mode='An'):
        self.clear_caches()
        if mode == 'Rn':
            idx = n - 1
            g_val = self._calc_closed_double_sum(idx, F, G)
            p_val = g_val.subs(zip(G, F)) # Map
            return simplify(g_val - R0 * p_val)
        else:
            t1_sum = 0
            t2_sum = 0
            for k in range(n):
                idx = n - k - 1
                g_val = self._calc_closed_double_sum(idx, F, G)
                p_val = g_val.subs(zip(G, F)) # Map
                t1_sum += binomial(n, k) * h[k] * p_val
                t2_sum += binomial(n, k) * h[k] * g_val
            return simplify(R0*(h[n] - t1_sum) + t2_sum)


# ==========================================
# PART 2: BENCHMARK RUNNER
# ==========================================

def run_suite():
    gen = BenchmarkGenerator()
    
    # CSV Header
    print("N,Target,Method,Time_Seconds")
    
    # Test Range (N=1 to 8)
    for N in range(1, 9):
        # Setup Symbols
        F = symbols(f'F_0:{N+1}')
        G = symbols(f'G_0:{N+1}')
        h = symbols(f'h_0:{N+1}')
        R0 = symbols('R_0')
        
        methods = [
            ("Recursive_Parallel", gen.run_recursive_parallel),
            ("Recursive_Mapped",   gen.run_recursive_mapped),
            ("Bell_Parallel",      gen.run_bell_parallel),
            ("Bell_Mapped",        gen.run_bell_mapped),
        ]
        
        targets = ["An", "Rn"]
        
        for target in targets:
            for name, func in methods:
                # Force garbage collection/clearing just in case
                gen.clear_caches()
                
                start = time.perf_counter()
                try:
                    _ = func(N, h, F, G, R0, mode=target)
                    end = time.perf_counter()
                    duration = end - start
                except Exception as e:
                    duration = -1.0 # Error flag
                
                print(f"{N},{target},{name},{duration:.6f}")
                
                # Flush stdout so user sees progress immediately
                sys.stdout.flush()

if __name__ == "__main__":
    run_suite()

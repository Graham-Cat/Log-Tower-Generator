from sympy import symbols, binomial, Function, Sum, IndexedBase, factorial, diff

# Define symbols
x = symbols('x')
n, k, m, j = symbols('n k m j', integer=True)

# Define Function placeholders
h = Function('h')(x)
f = Function('f')(x)
g = Function('g')(x)

# Define indexed bases for derivatives
# F_n corresponds to the n-th derivative of the base module
# G_n corresponds to the n-th derivative of the input module
# h_n corresponds to the n-th derivative of h
F = IndexedBase('F')
G_base = IndexedBase('G') # Renamed to avoid confusion with Gamma
H_base = IndexedBase('h')
R_base = IndexedBase('R')

def omega_cache_generator(target_n):
    """
    Generates the Omega Kernel cache up to target_n using dynamic programming.
    Returns a dictionary where keys are (m, n) tuples and values are symbolic expressions.
    Formula: Omega_{m,n} = - Sum_{j=0}^{m-1} binomial(n-1, j) * F_j * Omega_{m-1-j, n-1-j}
    """
    cache = {}

    # Base Case: Omega_{0, n} = 1 for all n
    for n_val in range(1, target_n + 2):
        cache[(0, n_val)] = 1

    # Recursive Step (DP)
    # We iterate through 'm' (kernel depth) then 'n' (derivative order)
    # Note: We need Omega up to index n+1 for the Gamma convolution
    for m_val in range(1, target_n + 1):
        for n_val in range(m_val + 1, target_n + 2): # n must be >= m for non-zero terms typically
            
            summation = 0
            # Implement the recursion: 
            # Omega_{m,n} = - sum_{k=0}^{m-1} bin(n-1, m-k-1) * F_{m-k-1} * Omega_{k, k+n-m}
            # Using the simplified index j from your derivation:
            for j_val in range(m_val):
                # j corresponds to the index of F
                # The binomial weight is (n-1) choose (j)
                # The previous Omega is Omega_{m-1-j, n-1-j}
                
                term = binomial(n_val - 1, j_val) * F[j_val] * cache[(m_val - 1 - j_val, n_val - 1 - j_val)]
                summation += term
            
            cache[(m_val, n_val)] = -summation

    return cache

def get_gamma_n(n_val, omega_cache):
    """
    Calculates Gamma_n using the discrete convolution formula.
    Gamma_n = Sum_{m=0}^{n} G_{n-m} * Omega_{m, n+1}
    """
    gamma_sum = 0
    for m_val in range(n_val + 1):
        # G index is n-m
        # Omega index is (m, n+1)
        # Note: Omega_{m, n+1} corresponds to the kernel depth m in the (n+1)-th derivative slot
        term = G_base[n_val - m_val] * omega_cache.get((m_val, n_val + 1), 0)
        gamma_sum += term
    
    return gamma_sum

def get_phi_n(n_val, omega_cache):
    """
    Calculates Phi_n (The F-Sector).
    This is structurally identical to Gamma_n, but maps G -> F.
    Phi_n = Sum_{m=0}^{n} F_{n-m} * Omega_{m, n+1}
    """
    phi_sum = 0
    for m_val in range(n_val + 1):
        term = F[n_val - m_val] * omega_cache.get((m_val, n_val + 1), 0)
        phi_sum += term
    
    return phi_sum

def generate_A_n(target_n):
    """
    Generates the full polynomial P(A_n).
    A_n = R_0 * (h_n - Sum binomial(n,k) h_k Phi_{n-k-1}) + Sum binomial(n,k) h_k Gamma_{n-k-1}
    """
    # 1. Pre-calculate the Omega Cache
    # We need coverage up to n+1
    omega_cache = omega_cache_generator(target_n)

    # 2. Build the summation parts
    # Gamma Sum (The G-Sector)
    gamma_part = 0
    for k_val in range(target_n):
        # Term: bin(n, k) * h_k * Gamma_{n-k-1}
        weight = binomial(target_n, k_val)
        h_term = H_base[k_val]
        gamma_val = get_gamma_n(target_n - k_val - 1, omega_cache)
        gamma_part += weight * h_term * gamma_val

    # Phi Sum (The F-Sector subtraction)
    phi_part = 0
    for k_val in range(target_n):
        # Term: bin(n, k) * h_k * Phi_{n-k-1}
        weight = binomial(target_n, k_val)
        h_term = H_base[k_val]
        phi_val = get_phi_n(target_n - k_val - 1, omega_cache)
        phi_part += weight * h_term * phi_val

    # 3. Combine
    # A_n = R_0 * (h_n - Phi_sum) + Gamma_sum
    # Note: h_n is H_base[target_n]
    
    R0 = R_base[0]
    A_n = R0 * (H_base[target_n] - phi_part) + gamma_part
    
    return A_n

def generate_R_n(target_n):
    """
    Generates P(R_n) using the Corollary.
    P(R_n) = Gamma_{n-1} - R_0 * Phi_{n-1}
    """
    if target_n == 0:
        return R_base[0]
        
    omega_cache = omega_cache_generator(target_n)
    
    gamma_prev = get_gamma_n(target_n - 1, omega_cache)
    phi_prev = get_phi_n(target_n - 1, omega_cache)
    
    R_n = gamma_prev - R_base[0] * phi_prev
    return R_n

# --- Sanity Check / Test Driver ---
if __name__ == "__main__":
    print("--- Generating A_3 (The Standard Test) ---")
    A3 = generate_A_n(3)
    # Expand to make it readable (grouping terms)
    print(A3.expand())
    
    print("\n--- Generating R_3 (The Corollary Test) ---")
    R3 = generate_R_n(3)
    print(R3.expand())

    print("\n--- Verification of Omega_3 (Kernel Check) ---")
    # Omega_3 corresponds to the 'drag' in the 3rd order
    # In our cache index (m,n), this is usually captured in row m=3
    cache = omega_cache_generator(4)
    # Let's inspect Omega_{3,4} which is the kernel for Gamma_3
    print(f"Omega_(3,4) = {cache.get((3,4))}")

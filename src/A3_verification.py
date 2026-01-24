import sympy as sp

def verify_A3_negative_convention():
    # 1. Define Symbols and Functions
    x = sp.symbols('x')
    f = sp.Function('f')(x)
    g = sp.Function('g')(x)
    h = sp.Function('h')(x)

    # 2. Define the Base Components
    # R = ln(g) / ln(f)
    log_f = sp.log(f)
    log_g = sp.log(g)
    R = log_g / log_f
    
    # The actual function A = R * h
    A_original = R * h

    # 3. Calculate "True" Derivative (Brute Force)
    print("Calculating brute force derivative (A''')...")
    A3_true = sp.diff(A_original, x, 3)

    # 4. Define the Modules (The "0-th" order)
    # F = f' / (f * ln f)
    # G = g' / (g * ln f)
    F_base = sp.diff(f, x) / (f * log_f)
    G_base = sp.diff(g, x) / (g * log_f)

    # 5. Define F_n and G_n as Explicit Derivatives
    # F(n) corresponds to the subscript notation F_n
    def F(n): return sp.diff(F_base, x, n)
    def G(n): return sp.diff(G_base, x, n)

    # Map to shorthand variables for readability
    F0, F1, F2 = F(0), F(1), F(2)
    G0, G1, G2 = G(0), G(1), G(2)
    h0 = h
    h1 = sp.diff(h, x, 1)
    h2 = sp.diff(h, x, 2)
    h3 = sp.diff(h, x, 3)

    # 6. Construct Gamma Terms (Using Negative Sign Convention)
    # Standard Pattern: Gamma_n = G_n - [Decay Terms]
    
    # Gamma_0 = G
    Gamma_0 = G0
    
    # Gamma_1 = G1 - GF
    Gamma_1 = G1 - G0*F0
    
    # Gamma_2 = G2 - G1F - G(2F1 - F^2)
    # Note: Using the preferred negative grouping -G(...)
    Gamma_2 = G2 - G1*F0 - G0*(2*F1 - F0**2)

    # 7. Construct Phi Terms (F-Sector)
    # Map G -> F in the Gamma definitions
    Phi_0 = F0
    Phi_1 = F1 - F0*F0
    Phi_2 = F2 - F1*F0 - F0*(2*F1 - F0**2)

    # 8. Assemble A3 using the Canonical Generator Form
    # A3 = R(h3 - F_Sector) + G_Sector
    # Sector Sum = sum( nCk * h_k * Gamma_{n-k-1} )
    # For n=3 (Terms: k=2, k=1, k=0)
    
    # Pascal Weights for n=3 (excluding the leading h3 term): 3, 3, 1
    
    F_sector = 3*h2*Phi_0 + 3*h1*Phi_1 + h0*Phi_2
    G_sector = 3*h2*Gamma_0 + 3*h1*Gamma_1 + h0*Gamma_2

    A3_candidate = R * (h3 - F_sector) + G_sector

    # 9. Verify Equality
    print("Verifying candidate against true derivative...")
    difference = sp.simplify(A3_candidate - A3_true)

    if difference == 0:
        print("\nSUCCESS: The A3 candidate matches exactly.")
        print("The Negative Sign Convention recursion is valid.")
    else:
        print("\nFAILURE: The expressions do not match.")
        print("Difference (simplified):")
        sp.pprint(difference)

if __name__ == "__main__":
    verify_A3_negative_convention()

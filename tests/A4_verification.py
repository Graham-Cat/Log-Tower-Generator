import sympy as sp

def verify_A4_negative_convention():
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
    print("Calculating brute force derivative (A'''')...")
    A4_true = sp.diff(A_original, x, 4)

    # 4. Define the Modules (The "0-th" order)
    # F = f' / (f * ln f)
    # G = g' / (g * ln f)
    F_base = sp.diff(f, x) / (f * log_f)
    G_base = sp.diff(g, x) / (g * log_f)

    # 5. Define F_n and G_n as Explicit Derivatives
    def F(n): return sp.diff(F_base, x, n)
    def G(n): return sp.diff(G_base, x, n)

    # Map to shorthand variables
    F0, F1, F2, F3 = F(0), F(1), F(2), F(3)
    G0, G1, G2, G3 = G(0), G(1), G(2), G(3)
    
    h0 = h
    h1 = sp.diff(h, x, 1)
    h2 = sp.diff(h, x, 2)
    h3 = sp.diff(h, x, 3)
    h4 = sp.diff(h, x, 4)

    # 6. Construct Gamma Terms (Recursive Decay Pattern)
    # Convention: Gamma_n = G_n - [Positive Decay Terms]
    
    # Gamma_0 = G
    Gamma_0 = G0
    
    # Gamma_1 = G1 - GF
    Gamma_1 = G1 - G0*F0
    
    # Gamma_2 = G2 - G1F - G(2F1 - F^2)
    Gamma_2 = G2 - G1*F0 - G0*(2*F1 - F0**2)
    
    # Gamma_3 = G3 - G2F - G1(3F1 - F^2) - G(3F2 - 5FF1 + F^3)
    Gamma_3 = G3 - G2*F0 \
                 - G1*(3*F1 - F0**2) \
                 - G0*(3*F2 - 5*F0*F1 + F0**3)

    # 7. Construct Phi Terms (F-Sector)
    # Map G -> F in the Gamma definitions
    Phi_0 = F0
    Phi_1 = F1 - F0**2
    Phi_2 = F2 - F1*F0 - F0*(2*F1 - F0**2)
    Phi_3 = F3 - F2*F0 \
               - F1*(3*F1 - F0**2) \
               - F0*(3*F2 - 5*F0*F1 + F0**3)

    # 8. Assemble A4 using the Canonical Generator Form
    # A4 = R(h4 - F_Sector) + G_Sector
    # Pascal Weights for n=4 (excluding the leading h4 term): 4, 6, 4, 1
    
    F_sector = 4*h3*Phi_0 + 6*h2*Phi_1 + 4*h1*Phi_2 + h0*Phi_3
    G_sector = 4*h3*Gamma_0 + 6*h2*Gamma_1 + 4*h1*Gamma_2 + h0*Gamma_3

    A4_candidate = R * (h4 - F_sector) + G_sector

    # 9. Verify Equality
    print("Verifying candidate against true derivative...")
    difference = sp.simplify(A4_candidate - A4_true)

    if difference == 0:
        print("\nSUCCESS: The A4 candidate matches exactly.")
    else:
        print("\nFAILURE: The expressions do not match.")
        print("Difference (simplified):")
        # sp.pprint(difference)

if __name__ == "__main__":
    verify_A4_negative_convention()

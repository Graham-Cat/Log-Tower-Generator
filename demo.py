"""
Log Tower Generator - Quick Start Demo (v1.0)
---------------------------------------------
This script demonstrates how to generate P(A_n) and P(R_n) polynomials
using the optimized Convolution Engine.

Usage:
    python demo.py
"""

from sympy import init_printing
# Import the new functional interface
from src import generate_A_n, generate_R_n

def run_demo():
    # Enable pretty printing for nicer console output (e.g., F[0] instead of F_0)
    init_printing(use_unicode=True)

    print("=== Log Tower Generator Demo (Convolution Engine) ===")

    # 1. Configuration
    N = 3
    print(f"\n[1] Configuration: Generating polynomials for N = {N}")

    # 2. Generate P(A_n)
    # The new engine handles symbol creation internally.
    # It uses IndexedBase symbols: h[n], F[n], G[n], R[0]
    print(f"[2] Generating P(A_{N})...")
    poly_An = generate_A_n(N)
    
    print(f"\n--- Result: P(A_{N}) ---")
    # We expand the result to ensure terms are grouped clearly
    print(poly_An.expand())

    # 3. Generate P(R_n)
    # Formula: P(R_n) = Gamma_{n-1} - R0 * Phi_{n-1}
    print(f"\n[3] Generating P(R_{N})...")
    poly_Rn = generate_R_n(N)
    
    print(f"\n--- Result: P(R_{N}) ---")
    print(poly_Rn.expand())

if __name__ == "__main__":
    run_demo()

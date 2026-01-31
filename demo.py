"""
Log Tower Generator - Quick Start Demo
--------------------------------------
This script demonstrates how to generate P(A_n) and P(R_n) polynomials
using the LogTowerGenerator library.

Usage:
    python demo.py
"""

from sympy import symbols, init_printing
from src import LogTowerGenerator

def run_demo():
    # Optional: Enable pretty printing for nicer console output
    init_printing(use_unicode=True)

    print("=== Log Tower Generator Demo ===")

    # 1. Configuration
    N = 3
    print(f"\n[1] Configuration: Generating polynomials for N = {N}")

    # 2. Define SymPy Symbols
    # We need lists of symbols for F, G, and h up to order N
    # Syntax 'F_0:4' creates symbols F_0, F_1, F_2, F_3
    F = symbols(f'F_0:{N+1}')
    G = symbols(f'G_0:{N+1}')
    h = symbols(f'h_0:{N+1}')
    R0 = symbols('R_0')

    # 3. Initialize the Generator
    print("[2] Initializing Generator...")
    gen = LogTowerGenerator()

    # 4. Generate P(A_n)
    # Formula: P(A_n) = R0 * [h_n - F-sector] + G-sector
    print(f"[3] Generating P(A_{N})...")
    poly_An = gen.generate_An(N, h, F, G, R0)
    
    print(f"\n--- Result: P(A_{N}) ---")
    print(poly_An)

    # 5. Generate P(R_n)
    # Formula: P(R_n) = Gamma_{n-1} - R0 * Phi_{n-1}
    print(f"\n[4] Generating P(R_{N})...")
    poly_Rn = gen.generate_Rn(N, F, G, R0)
    
    print(f"\n--- Result: P(R_{N}) ---")
    print(poly_Rn)

if __name__ == "__main__":
    run_demo()

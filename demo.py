"""
Log-Tower-Generator - Quick Start Demo (v2.0.0)
---------------------------------------------
This script demonstrates how to generate multidimensional mixed-partial 
derivatives P(A_alpha) and P(R_alpha) using the Chronological Step-Operator Engine.

Usage:
    python demo.py
"""

import symengine as se
import sympy as sp
from log_tower_generator import LogTowerGenerator

def run_demo():
    # Enable SymPy pretty printing for console output
    sp.init_printing(use_unicode=True)

    print("=== Log-Tower-Generator Demo (v2.0.0 Jet Space Engine) ===\n")

    # 1. Configuration: Define 3D spatial variables and abstract functions
    print("[1] Configuration: Setting up 3D Jet Space (x, y, z)...")
    x, y, z = se.symbols('x y z')
    vars = (x, y, z)
    
    f = se.Function('f')(x, y, z)
    g = se.Function('g')(x, y, z)
    h = se.Function('h')(x, y, z)

    # Instantiate the generator
    generator = LogTowerGenerator(vars, f, g)

    # Define the multi-index alpha for the derivative
    alpha = (2, 1, 1)  # 4th-order mixed partial
    print(f"    Target multi-index alpha = {alpha}\n")

    # 2. Generate P(R_alpha) [The Spine Bypass]
    print(f"[2] Generating P(R_alpha) for alpha = {alpha}...")
    print("    (Bypassing multi-index convolution via the Spine Projection Corollary)")
    poly_R_alpha = generator.get_R_alpha(alpha)
    
    print(f"\n--- Result: P(R_alpha) ---")
    # Cast back to SymPy for beautiful console formatting
    sp.pprint(sp.sympify(poly_R_alpha))
    print("\n" + "="*60 + "\n")

    # 3. Generate P(A_alpha) [The Master Generator]
    print(f"[3] Generating P(A_alpha) for alpha = {alpha}...")
    print("    (Executing the complete multi-index convolution loop)")
    poly_A_alpha = generator.get_A_alpha(alpha, h)
    
    print(f"\n--- Result: P(A_alpha) ---")
    sp.pprint(sp.sympify(poly_A_alpha))
    print("\n=== Demo Complete ===")

if __name__ == "__main__":
    run_demo()

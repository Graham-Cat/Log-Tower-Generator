"""
Verification Suite (v1.0.0)
----------------------------------
Verifies the LogTowerGenerator (Convolution Engine) by separating 
"Structure Generation" from "Value Substitution."

Adapts generator.py export style (IndexedBase) to the verification logic.
"""

import unittest
import sympy as sp
import sys
import os

# Ensure we can import from src
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import the specific generator function and the symbol bases used within it
from src.generator import generate_A_n, F, G_base, H_base, R_base

class TestLogTowerRobust(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        print("\n[Setup] Initializing Robust Environment...")
        cls.x = sp.symbols('x')
        cls.f = sp.Function('f')(cls.x)
        cls.g = sp.Function('g')(cls.x)
        cls.h = sp.Function('h')(cls.x)
        
        # 1. Real Derivatives (The "Values")
        cls.log_f = sp.log(cls.f)
        cls.log_g = sp.log(cls.g)
        cls.R_real = cls.log_g / cls.log_f
        
        # Base module definitions
        F_val = sp.diff(cls.f, cls.x) / (cls.f * cls.log_f)
        G_val = sp.diff(cls.g, cls.x) / (cls.g * cls.log_f)
        
        # Calculate lists of Real Expressions using Brute Force
        MAX_N = 6 
        cls.h_real = [cls.h]
        cls.F_real = [F_val]
        cls.G_real = [G_val]
        
        for i in range(MAX_N):
            cls.h_real.append(sp.diff(cls.h_real[-1], cls.x))
            cls.F_real.append(sp.diff(cls.F_real[-1], cls.x))
            cls.G_real.append(sp.diff(cls.G_real[-1], cls.x))

    def _verify_n(self, n):
        print(f"\n--- Verifying P(A_{n}) with Convolution Engine ---")
        
        # A. Calculate True Derivative (Brute Force)
        A_original = self.R_real * self.h
        print(f"1. Calculating Brute Force Derivative (Order {n})...")
        A_true = sp.diff(A_original, self.x, n)
        
        # B. Generate Polynomial Structure using the new Generator
        print(f"2. Generating Polynomial Structure...")
        # The new generator uses internal IndexedBase symbols (F, G_base, H_base)
        A_poly_structure = generate_A_n(n)
        
        # C. Substitute Real Values into the Structure
        print(f"3. Substiting Real Derivatives into Structure...")
        
        # Create substitution dictionary mapping the Generator's keys to Real Values
        subs_dict = {R_base[0]: self.R_real}
        
        for k in range(n + 1):
            # Map IndexedBase[k] -> RealList[k]
            subs_dict[H_base[k]] = self.h_real[k]
            subs_dict[F[k]]      = self.F_real[k]
            subs_dict[G_base[k]] = self.G_real[k]
            
        A_candidate = A_poly_structure.subs(subs_dict)
        
        # D. Verify
        print("4. Simplifying Difference...")
        # We simplify the difference to handle complex log expansions
        diff_val = sp.simplify(A_candidate - A_true)
        
        if diff_val == 0:
            print(f"[SUCCESS] P(A_{n}) matches exactly.")
        else:
            # Failure output for debugging
            print(f"[FAILURE] Mismatch at N={n}")
            print(f"Difference: {diff_val}")
            self.fail(f"Mismatch at N={n}")

    def test_A3(self):
        self._verify_n(3)

    def test_A4(self):
        self._verify_n(4)

    def test_A5(self):
        self._verify_n(5)

if __name__ == "__main__":
    unittest.main()

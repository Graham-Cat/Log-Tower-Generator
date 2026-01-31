"""
Unified Verification Suite (v1.0.0)
-----------------------------------
Rigorously verifies the LogTowerGenerator against the "True" mathematical 
derivatives calculated via brute-force differentiation.

Coverage:
- P(A_3)
- P(A_4)
- P(A_5)
"""

import unittest
import sympy as sp
import sys
import os

# Ensure we can import from src/
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src import LogTowerGenerator

class TestLogTowerAccuracy(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        """
        Sets up the heavy symbolic environment once for all tests.
        Pre-calculates derivatives up to N=5 to save runtime.
        """
        print("\n[Setup] Initializing Symbolic Environment...")
        
        # 1. Define Base Symbols
        cls.x = sp.symbols('x')
        cls.f = sp.Function('f')(cls.x)
        cls.g = sp.Function('g')(cls.x)
        cls.h = sp.Function('h')(cls.x)
        cls.R0 = sp.symbols('R_0') # Placeholder for structural R
        
        # 2. Define Real Mathematical Relationships
        # R = ln(g) / ln(f)
        cls.log_f = sp.log(cls.f)
        cls.log_g = sp.log(cls.g)
        cls.R_real = cls.log_g / cls.log_f
        
        # 3. Define The "Modules" (Base F and G)
        # F = f' / (f * ln f)
        # G = g' / (g * ln f)
        cls.F_base = sp.diff(cls.f, cls.x) / (cls.f * cls.log_f)
        cls.G_base = sp.diff(cls.g, cls.x) / (cls.g * cls.log_f)
        
        # 4. Generate Derivative Lists (The Inputs for the Generator)
        # We need up to 5th derivative for A_5
        MAX_N = 5
        
        print(f"[Setup] Pre-calculating derivatives up to Order {MAX_N}...")
        
        cls.h_list = [cls.h]
        cls.F_list = [cls.F_base]
        cls.G_list = [cls.G_base]
        
        for i in range(MAX_N):
            cls.h_list.append(sp.diff(cls.h_list[-1], cls.x))
            cls.F_list.append(sp.diff(cls.F_list[-1], cls.x))
            cls.G_list.append(sp.diff(cls.G_list[-1], cls.x))
            
        # Instantiate the Generator under test
        cls.gen = LogTowerGenerator()

    def _verify_n(self, n):
        """
        Helper validation logic:
        1. Calculate True Derivative: d^n/dx^n (R * h)
        2. Calculate Generator Result: P(A_n)
        3. Verify Identity: True - Gen == 0
        """
        print(f"\n--- Verifying N={n} ---")
        
        # A. The True Derivative (The "Control")
        # A = R * h
        A_original = self.R_real * self.h
        print(f"Calculating Brute Force Derivative (Order {n})...")
        A_true = sp.diff(A_original, self.x, n)
        
        # B. The Generator Result (The "Candidate")
        print(f"Running LogTowerGenerator (Hybrid Algorithm)...")
        # Note: We pass R_real as 'R0' so the generator substitutes the actual ln(g)/ln(f)
        # instead of a symbolic placeholder. This allows mathematical cancellation.
        A_candidate = self.gen.generate_An(
            n, self.h_list, self.F_list, self.G_list, self.R_real
        )
        
        # C. Compare
        print("Simplifying Difference...")
        diff = sp.simplify(A_candidate - A_true)
        
        # D. Assert
        self.assertEqual(diff, 0, f"Failure at N={n}: Generator output does not match true derivative.")
        print(f"[SUCCESS] P(A_{n}) matches exactly.")

    def test_A3(self):
        self._verify_n(3)

    def test_A4(self):
        self._verify_n(4)

    def test_A5(self):
        self._verify_n(5)

if __name__ == "__main__":
    unittest.main()

"""
Unified Symbolic Verification (v1.0.0)
--------------------------------------
Tests A_3, A_4, and A_5 using purely symbolic abstract functions (f, g, h).
Replicates the exact logic of the manual A_3 verification script but automates
the construction using the LogTowerGenerator.
"""

import unittest
import sympy as sp
import sys
import os

# Ensure we can import from src/
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src import LogTowerGenerator

class TestSymbolicAccuracy(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        print("\n[Setup] Initializing Abstract Symbolic Environment...")
        
        # 1. Define Symbols and Functions (Exactly as in your working snippet)
        cls.x = sp.symbols('x')
        cls.f = sp.Function('f')(cls.x)
        cls.g = sp.Function('g')(cls.x)
        cls.h = sp.Function('h')(cls.x)
        
        # 2. Define Base Components
        cls.log_f = sp.log(cls.f)
        cls.log_g = sp.log(cls.g)
        cls.R_real = cls.log_g / cls.log_f  # The actual R term
        
        # 3. Define the Modules (The "0-th" order)
        # F = f' / (f * ln f)
        # G = g' / (g * ln f)
        cls.F_base = sp.diff(cls.f, cls.x) / (cls.f * cls.log_f)
        cls.G_base = sp.diff(cls.g, cls.x) / (cls.g * cls.log_f)
        
        # 4. Pre-calculate Explicit Derivative Lists up to N=5
        # This replaces the manual "F0 = ..., F1 = ..." lines
        print("[Setup] Pre-calculating derivative lists (h, F, G)...")
        MAX_N = 5
        
        cls.h_list = [cls.h]
        cls.F_list = [cls.F_base]
        cls.G_list = [cls.G_base]
        
        for i in range(MAX_N):
            # Recursively differentiate the previous element
            # This builds the exact chain rule expansions SymPy needs to cancel terms
            cls.h_list.append(sp.diff(cls.h_list[-1], cls.x))
            cls.F_list.append(sp.diff(cls.F_list[-1], cls.x))
            cls.G_list.append(sp.diff(cls.G_list[-1], cls.x))
            
        # Initialize Generator
        cls.gen = LogTowerGenerator()

    def _run_test(self, n):
        print(f"\n--- Verifying P(A_{n}) (Abstract) ---")
        
        # 1. Calculate True Derivative (Brute Force)
        A_original = self.R_real * self.h
        print(f"Calculating brute force derivative A^({n})...")
        A_true = sp.diff(A_original, self.x, n)
        
        # 2. Generate Candidate from Library
        print("Running LogTowerGenerator...")
        # We pass self.R_real as 'R0' so the generator uses the actual log(g)/log(f)
        A_candidate = self.gen.generate_An(
            n, self.h_list, self.F_list, self.G_list, self.R_real
        )
        
        # 3. Verify Equality
        # Because we constructed inputs exactly like the working snippet, 
        # SymPy should be able to simplify the difference to 0.
        print("Simplifying difference (this may take a moment for higher N)...")
        diff = sp.simplify(A_candidate - A_true)
        
        if diff == 0:
            print(f"[SUCCESS] P(A_{n}) matches the true derivative exactly.")
        else:
            self.fail(f"Mismatch found for A_{n}. Difference does not simplify to 0.")

    def test_A3(self):
        self._run_test(3)

    def test_A4(self):
        self._run_test(4)

    def test_A5(self):
        # N=5 produces a massive expression, so simplification takes longer
        self._run_test(5)

if __name__ == "__main__":
    unittest.main()

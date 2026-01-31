"""
Robust Verification Suite (v1.0.0)
----------------------------------
Verifies the LogTowerGenerator by separating "Structure Generation" from 
"Value Substitution." This prevents SymPy from mangling the substitution 
mapping when handling complex derivative expressions.
"""

import unittest
import sympy as sp
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src import LogTowerGenerator

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
        
        F_base = sp.diff(cls.f, cls.x) / (cls.f * cls.log_f)
        G_base = sp.diff(cls.g, cls.x) / (cls.g * cls.log_f)
        
        # Calculate lists of Real Expressions
        MAX_N = 5
        cls.h_real = [cls.h]
        cls.F_real = [F_base]
        cls.G_real = [G_base]
        
        for i in range(MAX_N):
            cls.h_real.append(sp.diff(cls.h_real[-1], cls.x))
            cls.F_real.append(sp.diff(cls.F_real[-1], cls.x))
            cls.G_real.append(sp.diff(cls.G_real[-1], cls.x))

        # 2. Dummy Symbols (The "Shields")
        # We feed these to the generator so it can map G->F safely
        cls.F_sym = sp.symbols(f'F_0:{MAX_N+1}')
        cls.G_sym = sp.symbols(f'G_0:{MAX_N+1}')
        cls.h_sym = sp.symbols(f'h_0:{MAX_N+1}')
        cls.R_sym = sp.symbols('R_0')
        
        cls.gen = LogTowerGenerator()

    def _verify_n(self, n):
        print(f"\n--- Verifying P(A_{n}) with Symbolic Shielding ---")
        
        # A. Calculate True Derivative (Brute Force)
        A_original = self.R_real * self.h
        print(f"1. Calculating Brute Force Derivative (Order {n})...")
        A_true = sp.diff(A_original, self.x, n)
        
        # B. Generate Polynomial Structure using DUMMY SYMBOLS
        # This ensures the Generator's internal logic (G->F mapping) works perfectly
        print(f"2. Generating Polynomial Structure...")
        A_poly_structure = self.gen.generate_An(
            n, self.h_sym, self.F_sym, self.G_sym, self.R_sym
        )
        
        # C. Substitute Real Values into the Structure
        # Now we replace F_0 with f'/(f ln f), etc.
        print(f"3. substituting Real Derivatives into Structure...")
        
        # Create substitution dictionary
        subs_dict = {self.R_sym: self.R_real}
        for k in range(n + 1):
            subs_dict[self.h_sym[k]] = self.h_real[k]
            # Depending on N, we might not need all F/G terms, but mapping all is safe
            if k < len(self.F_sym): subs_dict[self.F_sym[k]] = self.F_real[k]
            if k < len(self.G_sym): subs_dict[self.G_sym[k]] = self.G_real[k]
            
        A_candidate = A_poly_structure.subs(subs_dict)
        
        # D. Verify
        print("4. Simplifying Difference...")
        diff = sp.simplify(A_candidate - A_true)
        
        if diff == 0:
            print(f"[SUCCESS] P(A_{n}) matches exactly.")
        else:
            self.fail(f"Mismatch at N={n}")

    def test_A3(self):
        self._verify_n(3)

    def test_A4(self):
        self._verify_n(4)

    def test_A5(self):
        self._verify_n(5)

if __name__ == "__main__":
    unittest.main()

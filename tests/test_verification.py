import pytest
import symengine as se
import sympy as sp
from log_tower_generator import LogTowerGenerator

# --- Fixtures for reusable pure abstract functions ---
@pytest.fixture
def base_symbols():
    x, y, z = se.symbols('x y z')
    f = se.Function('f')(x, y, z)
    g = se.Function('g')(x, y, z)
    h = se.Function('h')(x, y, z)
    return (x, y, z), f, g, h

# --- 1. Test Base Boundaries ---
def test_base_cases(base_symbols):
    """Verifies that the empty multi-index boundaries return correct base states."""
    vars, f, g, _ = base_symbols
    generator = LogTowerGenerator(vars, f, g)
    
    empty_alpha = (0, 0, 0)
    
    # Check internal base states
    assert generator._get_phi(empty_alpha) == -1
    assert generator._get_gamma(empty_alpha) == 0

# --- 2. Test 1D Master Generator ---
def test_1d_generator(base_symbols):
    """Verifies a 3rd-order derivative strictly along the x-axis."""
    vars, f, g, h = base_symbols
    generator = LogTowerGenerator(vars, f, g)
    
    x = vars[0]
    alpha = (3, 0, 0)
    
    # Brute Force
    A = h * (se.log(g) / se.log(f))
    brute_force = se.diff(A, x, 3)
    
    # Generator
    P_A_alpha = generator.get_A_alpha(alpha, h)
    
    # Algebraic Zero-Test
    diff_sp = sp.sympify(brute_force - P_A_alpha)
    assert sp.cancel(diff_sp) == 0

# --- 3. Test Multidimensional Spine Bypass ---
def test_multidimensional_spine(base_symbols):
    """Verifies the P(R_alpha) corollary bypass for a 3D mixed partial."""
    vars, f, g, _ = base_symbols
    generator = LogTowerGenerator(vars, f, g)
    
    x, y, z = vars
    alpha = (1, 1, 1) # Lightweight 3D mixed-partial
    
    # Brute Force (Spine only)
    R = se.log(g) / se.log(f)
    brute_force = se.diff(R, x, 1, y, 1, z, 1)
    
    # Generator Bypass
    P_R_alpha = generator.get_R_alpha(alpha)
    
    # Algebraic Zero-Test
    diff_sp = sp.sympify(brute_force - P_R_alpha)
    assert sp.cancel(diff_sp) == 0

# --- 4. Test Multidimensional Master Generator ---
def test_multidimensional_master(base_symbols):
    """Verifies the P(A_alpha) multi-index convolution for a 3D mixed partial."""
    vars, f, g, h = base_symbols
    generator = LogTowerGenerator(vars, f, g)
    
    x, y, z = vars
    alpha = (2, 1, 1) # 4th-order 3D mixed-partial
    
    # Brute Force
    A = h * (se.log(g) / se.log(f))
    brute_force = se.diff(A, x, 2, y, 1, z, 1)
    
    # Generator
    P_A_alpha = generator.get_A_alpha(alpha, h)
    
    # Algebraic Zero-Test
    diff_sp = sp.sympify(brute_force - P_A_alpha)
    assert sp.cancel(diff_sp) == 0

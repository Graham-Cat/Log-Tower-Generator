"""
Log Tower Generator Library
---------------------------
Exposes the main generator class for calculating Log-Tower polynomials P(A_n) and P(R_n).
"""

# Expose the main class directly to the package level
from .generator import LogTowerGenerator

# Package Metadata
__version__ = "1.0.0"
__all__ = ["LogTowerGenerator"]

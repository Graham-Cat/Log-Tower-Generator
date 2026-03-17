# **Changelog**

All notable changes to the **Log-Tower-Generator** will be documented in this file. This project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## **2026-03-16**

* Corrected location of module in testing suite

## **[2.0.0] - 2026-03-12**

*Major Architectural Overhaul: The Log-Tower-Generator has been completely rebuilt from a 1-dimensional discrete sequence generator into a fully optimized, n-dimensional jet space mathematical engine.*

### **Added**

* **Multidimensional Jet Space Architecture:** Upgraded the master equation to evaluate high-order mixed partial derivatives across any number of orthogonal dimensions using strict multi-index notation ($\alpha$).
* **Chronological Step-Operator Engine:** Introduced Anchor and Historical Web routing logic to strictly enforce a right-to-left spatial gradient sequence, generating the constrained index set $\mathcal{A}_\alpha$ and completely bypassing invalid path generation.
* **Asymmetric Tensor Caching ($\Omega^\alpha_\beta$):** Implemented an isolated, persistent tensor cache for the F-sector that completely decouples the computational drag of the denominator from the numerator.
* **The Spine Projection Corollary:** Added a direct mathematical bypass ($P(R_\alpha) = \Gamma_\alpha - R \Phi_\alpha$) to evaluate the pure logarithmic scaffold without triggering the full multi-index convolution loop.
* **SymEngine (C++) Integration:** Integrated SymEngine for core recursive generation, shifting massive multi-index expression trees to a highly optimized C++ backend to eliminate processor hanging.
* **Performance Visualizations:** Added Python benchmarking scripts to plot and visualize the "Warm Cache Flatline" and "Input Swapping" processor savings.

### **Changed**

* **Class-Based State Machine:** Replaced the v1.0.0 functional framework with the `LogTowerGenerator` class architecture to ensure the $\Phi$ and $\Gamma$ tensor caches persist continuously in memory across multiple evaluations.
* **Verification Protocol:** Upgraded `test_verification.py` to handle multidimensional jet spaces, utilizing SymEngine for the heavy lifting and strictly reserving SymPy for the final algebraic zero-test (`cancel()`).
* **Multi-Index Convolution:** Replaced the 1D discrete polynomial convolution loop with an $n$-dimensional dynamic itertools bound evaluator.

### **Removed**

* **Legacy 1D Endpoints:** Removed the `generate_A_n` and `generate_R_n` functions in favor of the unified multidimensional `get_A_alpha()` and `get_R_alpha()` class methods.
* **Standard Geometric Bounds:** Eliminated pure geometric multi-index bound loops (e.g., $0 \le \beta \le \alpha$) from the internal module generation, as they inherently produce invalid, path-independent mixed-partial branches.


## **[1.0.0] - 2026-02-04**

### **Added**

* **Discrete Convolution Engine:** Implemented a high-performance polynomial generator that separates "System Structure" from "Input Signal."
* **The  Kernel:** Introduced a cached 2D grid for the F-Kernel (), enabling  computational complexity.
* **Bivariate Generating Function:** Established the "Master Equation" for the entire kernel grid, providing a closed-form analytical definition for the system's infinite hierarchy.
* **Robust Verification Suite:** Added a comprehensive test suite that validates generated polynomials against brute-force symbolic differentiation.
* **Automated Python API:** Exposed functional endpoints (`generate_A_n`, `generate_R_n`) for seamless integration into larger symbolic math workflows.
* **Installation and Quickstart Instructions:** Instructions added to README.md for ease of user interaction.

### **Changed**

* **Architecture Shift:** Replaced the initial recursive class-based structure with an optimized functional framework to prevent symbolic "combinatorial explosion."
* **Symbol Management:** Transitioned to `sympy.IndexedBase` for internal symbol handling, ensuring consistent variable naming () across all derivative orders.
* **Walkthrough Updates:** Walkthrough updated to reflect architecture shift and improve clarity of derivations.
* **About Section Update:** updated to reflect architecture shift and new features

### **Fixed**

* **Import Resolution:** Resolved a package initialization error where `__init__.py` was referencing a deprecated class.
* **Simplification Logic:** Improved polynomial expansion to ensure the output matches the canonical "Simplified Form" (e.g., correctly grouping  terms in the F-sector).

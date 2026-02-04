# **Changelog**

All notable changes to the **Log-Tower-Generator** will be documented in this file. This project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

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

### **Fixed**

* **Import Resolution:** Resolved a package initialization error where `__init__.py` was referencing a deprecated class.
* **Simplification Logic:** Improved polynomial expansion to ensure the output matches the canonical "Simplified Form" (e.g., correctly grouping  terms in the F-sector).

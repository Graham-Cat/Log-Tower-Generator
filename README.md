# Log-Tower Generator v2.0.0

[](https://www.google.com/search?q=https://doi.org/PLACEHOLDER) *(Make sure to update this with your new Zenodo link!)*

### Overview

The Log-Tower Generator is a high-performance, multidimensional differential ring generator designed to completely bypass the $O(n!)$ combinatorial explosion traditionally associated with multivariable product rules (e.g., Faà di Bruno's formula and Bell polynomials).

By utilizing a highly efficient, path-dependent step-operator approach, this engine translates continuous spatial gradients into discrete, multi-index algebra.

### Industrial Architecture & Jet Space Integration

Version 2.0.0 upgrades the generator from a 1-D recursive tool into a full $n$-dimensional tensor framework. It is natively structured to integrate with **Jet Space** architectures.

Instead of executing computationally lethal symbolic calculus on the fly, the Log-Tower algorithm acts as a combinatorial router. It allows high-performance computing (HPC) environments to calculate massive, multivariable composite derivatives—such as testing millions of $g(X)$ candidate functions against a static $f(X)$ denominator—using $O(1)$ database lookups.

**Primary Use Cases:**

* **Physics-Informed Neural Networks (PINNs):** Bypassing deep automatic differentiation (AutoDiff) graphs for high-order multivariable derivatives to accelerate training.
* **Aerospace / Fluid Dynamics:** Optimizing multivariable tensor calculations for complex Navier-Stokes simulations.
* **Quantum Chemistry:** Efficiently testing massive sets of multivariable electron wavefunction approximations.

### Under the Hood

This generator is built using **Python** and **SymPy**. The parallel assembly logic ensures that both the $\Phi_\alpha$ and $\Gamma_\alpha$ states are calculated and rolled up simultaneously, maximizing CPU cache locality and eliminating the need for expensive post-processing Abstract Syntax Tree (AST) traversals.

---

### About the Project & Maintenance Status

This framework was developed by an independent mathematics hobbyist. It began in the summer of 2025 as a passionate exploration into closed differential families and rapidly evolved into the multidimensional matrix architecture presented here.

**Please Note:** This is a passion project managed by a single independent researcher with limited bandwidth. While the mathematics are rigorously proven and the core architecture is stable, this repository is not managed like a corporate software product.

* Bug reports and pull requests are welcome and will be reviewed as time permits.
* Highly specific feature requests or demands for custom edge-case implementations may not be accommodated.

If you use this architecture in your research, simulations, or ML models, please cite the Zenodo DOI provided above.

---

# **Contributing**

Contributions are welcome.
Open an issue or submit a pull request if you have:

- mathematical insights
- simplifications
- symbolic optimizations
- documentation improvements

## License

This project utilizes a dual-license strategy to cover both the software implementation and the theoretical work:

### Software (Code)
The source code (files within `src/` and `tests/`) is licensed under the **MIT License**. See the `LICENSE` file for details.

### Content (Theory & Documentation)
The mathematical derivations, "Walkthrough" narratives, diagrams, and theoretical discoveries (specifically the F/G-sector symmetry and related alphabet) are licensed under a **Creative Commons Attribution 4.0 International License (CC BY 4.0)**.


[![CC BY 4.0](https://licensebuttons.net/l/by/4.0/88x31.png)](http://creativecommons.org/licenses/by/4.0/)

**Attribution:** If you adapt or redistribute the theoretical concepts from this repository, please cite as:
> [Christopher Feick]. (2026). *Log-Tower-Generator: An explicit n-th derivative generator for h⋅ln(g)/ln(f) via F/G-sector symmetry*. (https://github.com/Graham-Cat/Log-Tower-Generator).

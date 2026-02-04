# **Log‑Tower-Generator Framework**
### *A Canonical, Self‑Similar Algebra for Logarithmic Derivative Towers*

This repository hosts a symbolic engine for computing the n-th derivatives of functions in the class $A(x) = h(x) \cdot \ln(g(x)) / \ln(f(x))$.

By mapping the derivatives to a stable F/G-sector symmetry, we establish a closed family of derivative modules that allows for direct computation. This approach avoids the combinatorial explosion of the quotient rule, offering optimized solutions for symbolic computation, asymptotic analysis, and problems in mathematical physics.

We provide an explicit, closed-form solution for general first-order linear recurrence relations. While the generating function solution for such recurrences is well-known via the integrating factor method, explicit formulas for the $n$-th term typically require ad-hoc expansions.

This project generalizes that process, utilizing a **Dual-Sector Convolution** approach. It separates the "System Structure" (the **F-Kernel**) from the "Input Signal" ($G$), allowing for the direct generation of the $n$-th term via binomial convolution without redundant iteration. This allows for the rapid computation of 'exotic' sequences where no obvious algebraic pattern exists.

---

# **Motivation**

Directly differentiating "Log-Tower" expressions of the form $A(x) = h(x) \cdot \log_{f(x)}(g(x))$ leads to a combinatorial explosion. The raw higher-order derivatives $A_n$ become increasingly opaque, tangling the contributions of $f$, $g$, and $h$ into complex, unstructured expressions.

The Log‑Tower-Generator resolves this by mapping the derivatives into a canonical normal form. By isolating the distinct "forcing" and "decay" dynamics of the components, the framework reorganizes the expansion into:
- **Sector Decomposition:** Splitting the solution into a homogeneous $\Phi$-sector and a particular $\Gamma$-sector.
- **Kernel Isolation:** Pre-calculating the system's "Drag" (the $\Omega$ Kernel) independent of the input.
- **Linear Superposition:** Generating the final $n$-th term $P(A_n)$ as a linear combination of these modular components.

This approach reveals deep structural symmetries in the derivative tower, drawing parallels to:
- Lie‑operator expansions
- Renormalization‑group (RG) flow
- Faà di Bruno and Bell‑polynomial hierarchies

# **Core Objects**

Let

- $f$, $g$, and $h$ be differentiable functions of $x$
- $F_n$ be the $n$‑th derivative of $\frac{f'}{f \cdot \ln(f)}$ (Base Module)
- $G_n$ be the $n$‑th derivative of $\frac{g'}{g \cdot \ln(f)}$ (Input Module)
- $h_n$ be the $n$‑th derivative of $h$ (Scaling Module)
- $R_n$ be the $n$‑th derivative of $\frac{\ln(g)}{\ln(f)}$ (The Spine)

Define two recursively corrected sector operators:

- $\Gamma_n$ (G‑sector)
- $\Phi_n$ (F‑sector, the G→F mapping of $\Gamma_n$)

These sectors absorb all induced cross‑sector structure and form the backbone of the canonical expansion.

---

# **Domain Constraints**

To ensure the Log-Tower expression $A(x) = h(x) \frac{\ln g(x)}{\ln f(x)}$ remains well-defined, the following conditions must be satisfied on the domain of $x$:
- **Positivity:** Both $f(x) > 0$ and $g(x) > 0$ must hold to satisfy the requirements of the natural logarithm.
- **Non-Vanishing Denominator:** $f(x) \neq 1$ is required to prevent a zero-valued denominator in the quotient $\ln f(x)$.
- **Singularity Analysis:** Special consideration is required at points where $f(x) \to 1$, $f(x) \to 0$, or $g(x) \to 0$. Depending on the local behavior of $h(x)$ and the logarithmic growth rates, these points may represent poles, branch points, or removable singularities requiring limit-based evaluation.

---

# **Log Tower N-th Derivative Generator**

For $n \geq 1$, the $n$-th derivative of the Log-Tower function $A(x) = h(x) \frac{\ln g(x)}{\ln f(x)}$ is given by the polynomial generator $P(A_n)$:

$$P(A_n) = R_0\big[h_n - \sum_{k=0}^{n-1} \binom{n}{k} h_k \Phi_{n-k-1}\big] + \sum_{k=0}^{n-1} \binom{n}{k} h_k \Gamma_{n-k-1}$$

This formulation expresses the complex derivative as a linear superposition of binomial convolutions, providing an explicit map of how the individual components contribute to the total structure:
- **Raw $h$-sector ($h_n$):** The direct $n$-th derivative of the scaling function $h(x)$.
- **Recursively corrected F-sector ($\Phi_n$):** The homogeneous component accounting for the internal dynamics of the denominator $f(x)$.
- **Recursively corrected G-sector ($\Gamma_n$):** The particular component accounting for the forcing input of the numerator $g(x)$.

By decoupling these sectors, the generator enables the direct computation of higher-order derivatives while bypassing the combinatorial complexity of repeated applications of the quotient rule.

---

# **The Engine: Convolution & The F-Kernel**

While the system can be defined recursively, it is most efficiently computed via **Discrete Convolution**. The system separates the **Input Signal ($G$)** from the **System Structure ($\Omega$)**.

### **The Convolution Formula**
Instead of calculating $\Gamma_n$ recursively, we calculate it as the dot product of the input vector $G$ and the pre-calculated F-Kernel $\Omega$:

$$\Gamma_n = \sum_{m=0}^{n} G_{n-m} \Omega_{m, n+1}$$

### **The F-Kernel ($\Omega$)**
The coefficients $\Omega_{m,n}$ represent the "Drag" of the system—purely a function of the base $f$. They form a stable 2D grid that can be cached and reused for both the F-Sector and G-Sector.

**Recursive Definition (Caching Algorithm):**

$$\Omega_{m,n} = - \sum_{j=0}^{m-1} \binom{n-1}{j} F_j \Omega_{m-1-j, \ n-1-j}$$

(With Base Case $\Omega_{0,n} = 1$)

---

# **The Master Equation**

The entire infinite grid of Kernel values $\Omega_{m,n}$ is generated by a single **Bivariate Generating Function**. This equation represents the "Grand Unified" definition of the Log-Tower's structure.

$$\sum_{m=0}^{\infty} \sum_{n=0}^{\infty} \Omega_{m,n} \frac{x^n}{n!} y^m = e^{-\mathcal{H}(xy)} \left( 1 + \int_0^x e^{t + \mathcal{H}(ty)} dt \right)$$

Where $\mathcal{H}(z)$ is the accumulated base function:
$$\mathcal{H}(z) = \sum_{n=0}^{\infty} F_n \frac{z^{n+1}}{(n+1)!}$$

This proves that the complex behavior of the higher derivatives is deterministically evolved from the simple interaction between the Identity Function ($e^x$) and the Base Function ($F$).

---

# **Corollary**

This derivative structure also implies that the "Spine" derivative $R_n$ is simply the projection of the sectors onto the base:

$$P(R_n) = \Gamma_{n-1} - R_0 \Phi_{n-1}$$

---

# Walkthrough

The walkthrough of how all equations were derived and the narrative behind their discovery is available to read starting [here](https://github.com/Graham-Cat/Log-Tower-Generator/tree/main/walkthrough) and spans five parts.

---

## **Installation**

### **Prerequisites**

* **Python 3.8+**
* **SymPy**: The library relies on SymPy for symbolic mathematics.

### **1. Clone the Repository**

```bash
git clone https://github.com/Graham-Cat/Log-Tower-Generator.git
cd Log-Tower-Generator

```

### **2. Set Up a Virtual Environment (Recommended)**

```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate

```

### **3. Install Dependencies**

You can install the package in "editable" mode, which allows you to run the demo and tests immediately:

```bash
pip install -e .

```

*Note: This will automatically install `sympy` as a dependency.*

### **4. Verify Installation**

Run the verification suite to ensure the **Convolution Engine** is correctly generating and validating polynomials on your system:

```bash
python tests/test_verification.py

```

*You should see `[SUCCESS] P(A_n) matches exactly` for orders 3, 4, and 5.*

---

### **Quick Start**

To see the generator in action, run the provided demo script:

```bash
python demo.py

```

This will output the expanded canonical forms for $P(A_3)$ and $P(R_3)$ .

---

### Features

New in v1.0.0: The $\Omega$-Kernel Engine
Replaces recursive calls with a cached dynamic programming grid ( $O(n^3)$ ), allowing for rapid generation of high-order polynomials without combinatorial explosion.

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


<img width="191" height="20" alt="image" src="https://github.com/user-attachments/assets/3bd1a43c-6deb-44e0-b84b-e3f74a8a4fc5" />

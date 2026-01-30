# **Log‑Tower-Generator Framework**  
### *A Canonical, Self‑Similar Algebra for Logarithmic Derivative Towers*

This repository hosts a symbolic engine for computing the n-th derivatives of functions in the class $A(x) = h(x) \cdot \ln(g(x)) / \ln(f(x))$.

By mapping the derivatives to a stable F/G-sector symmetry, we establish a closed family of derivative modules that allows for direct computation. This approach avoids the combinatorial explosion of the quotient rule, offering optimized solutions for symbolic computation, asymptotic analysis, and problems in mathematical physics.

We provide an explicit, closed-form solution for general first-order linear recurrence relations. While the generating function solution for such recurrences is well-known via the integrating factor method, explicit formulas for the $n$-th term typically require ad-hoc expansions.

This project generalizes that process, utilizing Bell Polynomials to expand the integrating factor, resulting in a double-sum generator that computes the $n$-th term directly from the sequence inputs without iteration. This allows for the rapid computation of 'exotic' sequences where no obvious algebraic pattern exists.

---

# **Motivation**

Directly differentiating "Log-Tower" expressions of the form $A(x) = h(x)⋅\log_{f(x)}(g(x))$ leads to a combinatorial explosion. The raw higher-order derivatives $A_n$ become increasingly opaque, tangling the contributions of $f$, $g$, and $h$ into complex, unstructured expressions.

The Log‑Tower-Generator resolves this by mapping the derivatives into a canonical normal form. By isolating the distinct "forcing" and "decay" dynamics of the components, the framework reorganizes the expansion into:
- Sector Decomposition: Splitting the solution into a homogeneous $\Phi$-sector and a particular $\Gamma$-sector.
- Triangular Recurrence: Computing coefficients via stable binomial convolutions rather than nested derivatives.
- Linear Superposition: Generating the final $n$-th term $P(A_n)$ as a linear combination of these modular components.

This approach reveals deep structural symmetries in the derivative tower, drawing parallels to:
- Lie‑operator expansions
- Renormalization‑group (RG) flow
- Faà di Bruno and Bell‑polynomial hierarchies

# **Core Objects**

Let

- $f$, $g$, and $h$ be differentiable functions of $x$
- $F_n$ be the $n$‑th derivative of $\frac{f'}{f⋅ln(f)}$  
- $G_n$ be the $n$‑th derivative of $\frac{g'}{g⋅ln(f)}$  
- $h_n$ be the $n$‑th derivative of $h$
- $R_n$ be the $n$‑th derivative of $\frac{ln(g)}{ln(f)}$

Define two recursively corrected sector operators:

- $\Gamma_n$ (G‑sector)  
- $\Phi_n$ (F‑sector, the G→F mapping of $\Gamma_n$)

These sectors absorb all induced cross‑sector structure and form the backbone of the canonical expansion.

---

# **Domain Constraints** 

To ensure the Log-Tower expression $A(x) = h(x) \frac{\ln g(x)}{\ln f(x)}$ remains well-defined, the following conditions must be satisfied on the domain of $x$:
- Positivity: Both $f(x) > 0$ and $g(x) > 0$ must hold to satisfy the requirements of the natural logarithm.
- Non-Vanishing Denominator: $f(x) \neq 1$ is required to prevent a zero-valued denominator in the quotient $\ln f(x)$.
- Singularity Analysis: Special consideration is required at points where $f(x) \to 1$, $f(x) \to 0$, or $g(x) \to 0$. Depending on the local behavior of $h(x)$ and the logarithmic growth rates, these points may represent poles, branch points, or removable singularities requiring limit-based evaluation.
---

# **Log Tower N-th Derivative Generator**

For $n \geq 1$, the $n$-th derivative of the Log-Tower function $A(x) = h(x) \frac{\ln g(x)}{\ln f(x)}$ is given by the polynomial generator $P(A_n)$:

$$P(A_n) = R_0\big[h_n - \sum_{k=0}^{n-1} \binom{n}{k} h_k \Phi_{n-k-1}\big] + \sum_{k=0}^{n-1} \binom{n}{k} h_k \Gamma_{n-k-1}$$

This formulation expresses the complex derivative as a linear superposition of binomial convolutions, providing an explicit map of how the individual components contribute to the total structure:
- Raw $h$-sector ($h_n$): The direct $n$-th derivative of the scaling function $h(x)$.
- Recursively corrected F-sector ($\Phi_n$): The homogeneous component accounting for the internal dynamics of the denominator $f(x)$.
- Recursively corrected G-sector ($\Gamma_n$): The particular component accounting for the forcing input of the numerator $g(x)$.

By decoupling these sectors, the generator enables the direct computation of higher-order derivatives while bypassing the combinatorial complexity of repeated applications of the quotient rule.

---

# **Recursions**

### **G‑sector recursion**

$$\Gamma_n = G_n - \sum_{k=0}^{n-1} \binom{n}{k} F_k \Gamma_{n-k-1}$$

### **Base case**

$$\Gamma_0 = G$$

### **F‑sector recursion**

$$\Phi_n = \text{G→F mapping of } \Gamma_n$$

### Closed form of G-sector recursion

$$\Gamma_n = n! [x^n] \overline{\gamma}(x)$$

Where

$$\overline{\gamma}(x) = \overline{g}(x) - \overline{f}(x) e^{-H(x)} \int_0^x \overline{g}(t) e^{H(t)} dt$$

$$\overline{f}(x) = \sum_{n=0}^{\infty} F_n \frac{x^n}{n!}$$

$$\overline{g}(x) = \sum_{n=0}^{\infty} G_n \frac{x^n}{n!}$$

and

$$H(x) = \sum_{n=0}^{\infty} F_n \frac{x^{n+1}}{(n+1)!}$$


### Closed double sum representation of G-sector recursion

$$\Gamma_n = \sum_{m=0}^{n} \binom{n+1}{m+1} B_{n-m}(-F_0, \dots, -F_{n-m-1}) \left[ \sum_{j=0}^{m} \binom{m}{j} G_j B_{m-j}(F_0, \dots, F_{m-j-1}) \right]$$


Summary of Terms

1. $G_j$: The $j$-th element of $G$.
2. $F_k$: The $k$-th element of $F$.
3. $B_k(\dots)$: The $k$-th Complete Bell Polynomial.
4. Indices: Note carefully that the arguments for the Bell polynomials are shifted: the $k$-th polynomial takes inputs $(F_0, \dots, F_{k-1})$.

# **Corollary**

This derivative structure also implies that

$$ P(R_n) = \Gamma_{n-1} - R_0 \Phi_{n-1} $$

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

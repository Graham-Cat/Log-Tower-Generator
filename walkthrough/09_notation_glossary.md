# Appendix: Mathematical Notation & Definitions (v2.0.0)

This appendix serves as a glossary for the specific notation used throughout the **$P(A_\alpha)$ Log-Tower Generator** walkthrough. While most symbols follow standard multivariate calculus conventions, the module operators, constrained index sets, and sector definitions are specific to the $F/G$-sector symmetry framework operating across $n$-dimensional jet space.

## The Closed Alphabet $\left\lbrace R, h, F, G, u, v \right\rbrace$

The complete family of objects that are **closed under partial differentiation** across orthogonal variables $X = (x_1, x_2, \dots, x_d)$:

| Symbol | Definition | Role | Description |
| --- | --- | --- | --- |
| **$A$** | $\log_f(g^h)$ | **Target Function** | the primary multivariate function being differentiated |
| **$R$** | $\frac{\ln g(X)}{\ln f(X)}$ | **The Spine** | the ratio of logs acting as the scaffold |
| **$h$** | $h(X)$ | **The Exponent** | the exponent function in the tower $g(X)^{h(X)}$ |
| **$F^{(w)}$** | $\frac{f_w}{f \ln f}$ | **Base Module** | the relative rate of change of the base scaled by its log, rooted in dimension $w$ |
| **$G^{(w)}$** | $\frac{g_w}{g \ln f}$ | **Input Module** | the relative rate of change of the input scaled by the base log, rooted in dimension $w$ |
| **$u^{(w)}$** | $\frac{f_w}{f}$ | **Log Derivative** | the logarithmic derivative of the base function $f(X)$ along dimension $w$ |
| **$v^{(w)}$** | $\frac{g_w}{g}$ | **Log Derivative** | the logarithmic derivative of the input function $g(X)$ along dimension $w$ |

> **Note: Spine vs. Modules**
> While $R$ is part of the closed alphabet, it functions as the **scaffold**. The directional components $F^{(w)}, G^{(w)}, u^{(w)}, v^{(w)}$ act as **modules**—algebraic building blocks that drive the evolution of $R$ across any dimension $w$.

## Multi-Index Derivative Notation

To keep equations compact in jet space, this walkthrough uses multi-index notation $\alpha = (\alpha_1, \alpha_2, \dots, \alpha_d)$ for spatial gradients.

| Symbol | Equivalent | Description |
| --- | --- | --- |
| **$y_\alpha$** or **$D^\alpha y$** |  | the $\alpha$-th mixed partial derivative of the function $y(X)$ |
| **$h_\alpha$** |  | the $\alpha$-th mixed partial derivative of the exponent $h(X)$ |
| **$F^{(w)}_\alpha$** | $D^\alpha F^{(w)}$ | the $\alpha$-th mixed partial derivative of the $w$-rooted **Base Module** |
| **$G^{(w)}_\alpha$** | $D^\alpha G^{(w)}$ | the $\alpha$-th mixed partial derivative of the $w$-rooted **Input Module** |
| **$e_w$** | $(0, \dots, 1, \dots, 0)$ | the standard basis vector representing a single derivative shift in dimension $w$ |

## Structural Variables

Variables used to define the multidimensional recursive architecture:

| Symbol | Definition | Description |
| --- | --- | --- |
| **$P(A_\alpha)$** | $D^\alpha \left(h \frac{\ln g}{\ln f}\right)$ | the master generator for the $\alpha$-th partial differential of the target function |
| **$\hat{A}_\alpha$** | $\bigcup \left( \mathcal{S}\_{k, \text{anchor}} \cup \mathcal{S}_{k, \text{web}} \right)$ | the **Constrained Index Set** of chronologically valid jet space coordinates |
| **$\Gamma_\alpha$** | (Recursive) | the recursive polynomial state within the **G-Sector** |
| **$\Phi_\alpha$** | (Recursive) | the recursive polynomial state within the **F-Sector** |
| **$\Omega^\alpha_\beta$** | (Recursive) | the multidimensional **F-Kernel**: a cached tensor grid representing system "drag" |

## Identity Reference

Key differential equations and step-operators driving the $n$-dimensional system:

**1. The Fundamental Dimensional Identity:**
For any dimension $w$:


$$R_w = G^{(w)} - R F^{(w)}$$

**2. The Log Derivative Unit Template:**
For any log unit $\mu \in \left\lbrace u, v \right\rbrace$ and its dimensional superscripts:


$$\frac{\partial}{\partial w} \mu^{(\alpha)} = \mu^{(\text{index} + 1_w)} - \mu^{(\alpha)}\mu^{(w)}$$

**3. The Base Module Template:**
For any module $M \in \left\lbrace F, G \right\rbrace$ and its corresponding log unit $\mu \in \left\lbrace u, v \right\rbrace$:


$$\frac{\partial}{\partial w} M^{(z)}_{(\alpha)} = M^{(\text{index} + 1_w + 1_z)} - M^{(\text{index} + 1_w)}\left(\mu^{(z)} + F^{(z)}\right)$$

**4. The Derivative Shift Operators:**
To advance the polynomial states along a spatial gradient:


$$\Gamma_\alpha = \frac{\partial}{\partial w}\Gamma_{\alpha - e_w} - \Phi_{\alpha - e_w} G^{(w)}$$

$$\Phi_\alpha = \frac{\partial}{\partial w}\Phi_{\alpha - e_w} - \Phi_{\alpha - e_w} F^{(w)}$$

$$\Omega_{\beta}^{\alpha} = \frac{\partial}{\partial x} \Omega_{\beta-e_w}^{\alpha-e_w} + \Omega_{\beta}^{\alpha-e_w}$$

**5. The Multidimensional Omega Kernel ($\Omega$):**


$$\Omega^\alpha_\beta = - \sum_{0 \leq \gamma \leq \beta - e_w} \binom{\alpha-e_w}{\gamma} F^{(w)}_\gamma \Omega^{\alpha - e_w - \gamma}_{\beta - e_w - \gamma}$$


(Base case: $\Omega_\emptyset^\alpha = 1$)

**6. The Constrained Sector Accumulation:**
The evaluation of the master polynomial states over the $\hat{A}_\alpha$ routing history:


$$\Gamma_\alpha = \sum_{(x_k, \beta) \in \hat{A}_\alpha} G^{(x_k)}_{\beta} \Omega_{\alpha - \beta}^\alpha$$

$$\Phi_\alpha = \sum_{(x_k, \beta) \in \hat{A}_\alpha} F^{(x_k)}_{\beta} \Omega_{\alpha - \beta}^\alpha$$


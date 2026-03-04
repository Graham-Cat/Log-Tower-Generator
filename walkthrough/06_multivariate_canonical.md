# Part 6: Two Out of Four Ain't Bad

With as much as we've gone through in this repo, you might think we've accomplished a ton.

While we have gone through quite a bit, all we've done so far is create and optimize the generator with respect to a single variable, $x$.

If you look around the room you're in, you might notice that it's three-dimensional. I assume looking around took some time, so there's apparently a fourth dimension, too. Whaddaya know?

Without taking the generator at least 2-D, there's not much use for it except as a curiosity, and without including $x$, $y$, $z$, and $t$ in its final form, its true power (providing a straightforward, factorized, and optimized QFT and perturbation theory testing tool) will never be realized.

So, let's dive in -- at least partially.

## Partial to Derivatives

Making the derivative generator function n-dimensionally requires developing its ability to take **partial** derivatives with respect to each variable.

That means, instead of entering $f(x)$, $g(x)$, and $h(x)$ and asking the generator for the n-th derivative of $A(x) = h(x)\frac{\text{ln}g(x)}{\text{ln}f(x)}$ we'll need to be able to enter $f(x,y,z,t)$, $g(x,y,z,t)$, and $h(x,y,z,t)$ and ask for the function that provides $n_x$ -th, $n_y$ -th, $n_z$ -th, and $n_t$ -th *partial* derivatives with respect to $x$, $y$, $z$, and $t$ of $A(x,y,z,t) = h(x,y,z,t)\frac{\text{ln}g(x,y,z,t)}{\text{ln}f(x,y,z,t)}$ all at the same time.

In other words, by the time we're done we should be able to ask for 

$$\frac{\partial^{(n_x+n_y+n_z+n_t)}}{\partial x^{n_x} \partial y^{n_y} \partial z^{n_z} \partial t^{n_t}} A(x,y,z,t) = \frac{\partial^{(n_x+n_y+n_z+n_t)}}{\partial x^{n_x} \partial y^{n_y} \partial z^{n_z}  \partial t^{n_t}} \left(h(x,y,z,t)\frac{\text{ln}g(x,y,z,t)}{\text{ln}f(x,y,z,t)}\right)$$

and expect a factorized 4-D response that provides a single function for any chosen whole number designations of $n_x$, $n_y$, $n_z$, and $n_t$.

So, where to start?

### It Takes Two, Baby

Once we get a firm grasp on a 2-D generator, adding n-dimensions will have a straightforward roadmap, so let's begin there.

Our target function is

$$\frac{\partial^{n_x+n_y}}{\partial x^{n_x}\partial y^{n_y}} A(x,y) = \frac{\partial^{n_x+n_y}}{\partial x^{n_x}\partial y^{n_y}} \left(h(x,y)\frac{\text{ln}g(x,y)}{\text{ln}f(x,y)}\right)$$

We begin by defining $G^{(x)}$, $G^{(y)}$, $F^{(x)}$, and $F^{(y)}$ as

$$G^{(x)} = \frac{g_x}{g\text{ln}f}$$
$$G^{(y)} = \frac{g_y}{g\text{ln}f}$$
$$F^{(x)} = \frac{f_x}{f\text{ln}f}$$
$$F^{(y)} = \frac{f_y}{f\text{ln}f}$$

Where

$$g_x = \frac{\partial}{\partial x}g(x,y)$$
$$g_y = \frac{\partial}{\partial y}g(x,y)$$
$$f_x = \frac{\partial}{\partial x}f(x,y)$$
$$f_y = \frac{\partial}{\partial y}f(x,y)$$

Since the complexity of the generator is rooted in understanding derivatives of $R = \frac{\text{ln}g}{\text{ln}f}$, let's start by analyzing it in two dimensions.

Based on the identities from our 1-D work,

$$\frac{\partial}{\partial x} R = R_{(1,0)} = G^{(x)} - F^{(x)}R$$

and 

$$\frac{\partial}{\partial y} R = R_{(0,1)} = G^{(y)} - F^{(y)}R$$


There are two ways to express $R_{(1,1)}$:

$$\frac{\partial}{\partial y} R_{(1,0)} = R_{(1,1)} = G^{(x)}\_{\text{(0,1)}} - F^{(x)}\_{\text{(0,1)}}R - F^{(x)}R\_{\text{(0,1)}}$$

$$\frac{\partial}{\partial x} R_{(0,1)} = R_{(1,1)} = G^{(y)}\_{\text{(1,0)}} - F^{(y)}\_{\text{(1,0)}}R - F^{(y)}R\_{\text{(1,0)}}$$

Note how changing the $x$ 's to $y$ 's impacts the subscripts.

For the sake of satisfying Clairaut’s theorem (or Schwarz's theorem) for mixed partial derivatives (i.e., taking partial derivatives with respect to $x$ and $y$ produces an algebraically equivalent function regardless of the order in which they are performed), let's go through the exercise of proving that these two representations are the same.

We start by substituting the definition of $R_{(0,1)} = G^{(y)} - F^{(y)}R$ into the first equation:

$$R_{(1,1)} = G^{(x)}\_{(0,1)} - F^{(x)}\_{(0,1)}R - F^{(x)}\left[ G^{(y)} - F^{(y)}R \right]$$

Distribute $F^{(x)}$ and group the terms:

$$R_{(1,1)} = \underbrace{\left[ G^{(x)}_{(0,1)} - F^{(x)}G^{(y)} \right]}\_{\text{Independent Term } (\Gamma)} - R \cdot \underbrace{\left[ F^{(x)}_{(0,1)} - F^{(x)}F^{(y)} \right]}_{\text{Coefficient Term } (\Phi)}$$

Then we substitute the definition of $R_{(1,0)} = G^{(x)} - F^{(x)}R$ into the second equation:

$$R_{(1,1)} = G^{(y)}\_{(1,0)} - F^{(y)}_{(1,0)}R - F^{(y)}\left[ G^{(x)} - F^{(x)}R \right]$$

Distribute $F^{(y)}$ and group the terms:

$$R_{(1,1)} = \underbrace{\left[ G^{(y)}_{(1,0)} - F^{(y)}G^{(x)} \right]}\_{\text{Independent Term } (\Gamma)} - R \cdot \underbrace{\left[ F^{(y)}_{(1,0)} - F^{(y)}F^{(x)} \right]}_{\text{Coefficient Term } (\Phi)}$$

Proving that the coefficient terms ($\Phi$) are equal will be a good start, so let's show that

$$F^{(x)}\_{(0,1)} - F^{(x)}F^{(y)} = F^{(y)}_{(1,0)} - F^{(y)}F^{(x)}$$

Since $F^{(x)}F^{(y)} = F^{(y)}F^{(x)}$ we can remove them from both sides, leaving us with the need to prove that

$$F^{(x)}\_{(0,1)} = F^{(y)}_{(1,0)}$$

Using the definitions $F^{(x)} = \frac{f_x}{f \ln f}$ and $F^{(y)} = \frac{f_y}{f \ln f}$:

$$F^{(x)}\_{(0,1)} = \frac{\partial}{\partial y}\left( \frac{f_x}{f \ln f} \right) = \frac{f_{xy}}{f \ln f} - \frac{f_x}{f}\cdot\frac{f_y}{f \ln f} - \frac{f_x}{f \ln f}\cdot\frac{f_y}{f \ln f}$$

and

$$F^{(y)}\_{(1,0)} = \frac{\partial}{\partial x}\left( \frac{f_y}{f \ln f} \right) = \frac{f_{yx}}{f \ln f} - \frac{f_y}{f}\cdot\frac{f_x}{f \ln f} - \frac{f_y}{f \ln f}\cdot\frac{f_x}{f \ln f}$$

Cursory inspection and application of the commutative property of multiplication and Clairaut’s theorem (i.e., $f_{xy} = f_{yx}$) shows these two expressions to be equivalent.

The independent ($\Gamma$) terms don't have the benefit of immediate cancellation since $G^{(x)}F^{(y)} \neq G^{(y)}F^{(x)}$, so let's write the whole thing out:

$$G^{(x)}\_{(0,1)} - F^{(x)}G^{(y)} = {G^{(y)}}\_{(1,0)} - F^{(y)}G^{(x)}$$

Using definitions $G^{(x)} = \frac{g_x}{g \ln f}$ and $G^{(y)} = \frac{g_y}{g \ln f}$:

$${G^{(x)}}\_{(0,1)} = \frac{\partial}{\partial y}\left( \frac{g_x}{g \ln f} \right) = \frac{g_{xy}}{g \ln f} - \frac{g_x g_y}{g^2 \ln f} - \frac{g_x f_y}{g f \ln^2 f}$$

Then we subtract the product term $F^{(x)}G^{(y)} = \frac{f_x g_y}{f g \ln^2 f}$ to complete the LHS:

$$\Gamma_{\text{LHS}} = \frac{g_{xy}}{g \ln f} - \frac{g_x}{g}\cdot\frac{g_y}{g \ln f} - \frac{g_x}{g \ln f}\cdot\frac{f_y}{f \ln f} - \frac{g_y}{g \ln f}\cdot\frac{f_x}{f \ln f}$$

Development of the RHS requires a simple index swap, so

$$\Gamma_{\text{RHS}} = \frac{g_{yx}}{g \ln f} - \frac{g_y}{g}\cdot\frac{g_x}{g \ln f} - \frac{g_y}{g \ln f}\cdot\frac{f_x}{f \ln f} - \frac{g_x}{g \ln f}\cdot\frac{f_y}{f \ln f}$$


Again, these two expressions are clearly equivalent proving that 

$$R_{(1,1)} = G^{(x)}\_{\text{(0,1)}} - F^{(x)}\_{\text{(0,1)}}R - F^{(x)}R\_{\text{(0,1)}} = G^{(y)}\_{\text{(1,0)}} - F^{(y)}\_{\text{(1,0)}}R - F^{(y)}R\_{\text{(1,0)}}$$

### Multivariate Module Magic

Moreover, the above representations of the partial derivatives of $F^{(x)}$, $F^{(y)}$, $G^{(x)}$, and $G^{(y)}$ reinforce that, even when we expand to two dimensions, the closed family endures. Note that:

$$\frac{\partial}{\partial y} F^{(x)} = F^{(x)}_{(0,1)} = \frac{f_{xy}}{f \ln f} - \frac{f_x}{f}\cdot\frac{f_y}{f \ln f} - \frac{f_x}{f \ln f}\cdot\frac{f_y}{f \ln f} = F^{(1,1)} - F^{(0,1)}\left(u^{(x)} + F^{(x)}\right)$$

$$\frac{\partial}{\partial x} F^{(y)} = F^{(y)}_{(1,0)} = \frac{f_{yx}}{f \ln f} - \frac{f_y}{f}\cdot\frac{f_x}{f \ln f} - \frac{f_y}{f \ln f}\cdot\frac{f_x}{f \ln f} = F^{(1,1)} - F^{(1,0)}\left(u^{(y)} + F^{(y)}\right)$$

$$\frac{\partial}{\partial y} G^{(x)} = G^{(x)}_{(0,1)} = \frac{g_{xy}}{g \ln f} - \frac{g_x}{g}\cdot\frac{g_y}{g \ln f} - \frac{g_x}{g \ln f}\cdot\frac{g_y}{g \ln f} = G^{(1,1)} - G^{(0,1)}\left(v^{(x)} + F^{(x)}\right)$$

$$\frac{\partial}{\partial x} G^{(y)} = G^{(y)}_{(1,0)} = \frac{g_{yx}}{g \ln f} - \frac{g_y}{g}\cdot\frac{g_x}{g \ln f} - \frac{g_y}{g \ln f}\cdot\frac{g_x}{g \ln f} = G^{(1,1)} - G^{(1,0)}\left(v^{(y)} + F^{(y)}\right)$$

When expanding higher-order mixed partial derivatives, the number of base identities explodes. Instead of listing out all twelve permutations for our 2-D modules ($F$ and $G$) and log derivative units ($u$ and $v$), we can condense them into two universal templates. 

Let $w$ represent the variable we are taking the derivative of with respect to ($x$ or $y$), and let $z$ represent the superscript variable of the module itself.

Also, let $(\alpha)$ represent the base $(n_x, n_y)$ coordinate above, allowing for $n$ dimensions instead of just two.

Incrementing an index with respect to a variable is denoted simply by adding $1_w$ or $1_z$ to the base $(\alpha)$ coordinate.

**1. The Log Derivative Unit Template**
For any log unit $\mu \in \{u, v\}$ associated with its respective function ($f$ or $g$), the partial derivative with respect to $w$ is:

$$\frac{\partial}{\partial w} \mu^{(\alpha)} = \mu^{(\text{index} + 1_w)} - \mu^{(\alpha)}\mu^{(w)}$$

*Applied examples:*
* $$\frac{\partial}{\partial x} u^{(n_x, n_y)} = u^{(n_x + 1,n_y)} - u^{(n_x,n_y)}u^{(x)}$$
* $$\frac{\partial}{\partial y} v^{(n_x, n_y)} = v^{(n_x,n_y + 1)} - v^{(n_x,n_y)}v^{(y)}$$

**2. The Base Module Template**
For any module $M \in \{F, G\}$ associated with its respective log unit $\mu \in \{u, v\}$, the partial derivative of $M^{(z)}$ with respect to $w$ is:

$$\frac{\partial}{\partial w} M^{(z)}_{(\alpha)} = M^{(\text{index} + 1_w + 1_z)} - M^{(\text{index} + 1_w)}\left(\mu^{(z)} + F^{(z)}\right)$$

*Applied examples:*
* $$\frac{\partial}{\partial y} F^{(x)}_{(n_x,n_y)} = F^{(n_x + 1,n_y + 1)} - F^{(n_x,n_y + 1)}\left(u^{(x)} + F^{(x)}\right)$$
* $$\frac{\partial}{\partial x} G^{(x)}_{(n_x,n_y)} = G^{(n_x + 2,n_y)} - G^{(n_x + 1,n_y)}\left(v^{(x)} + F^{(x)}\right)$$
* $$\frac{\partial}{\partial x} G^{(y)}_{(n_x,n_y)} = G^{(n_x + 1,n_y + 1)} - G^{(n_x + 1,n_y)}\left(v^{(y)} + F^{(y)}\right)$$

These two simple rules dictate the entire multivariate module expansion, proving that no matter how many dimensions we add, the closed family remains intact. [^1]

[^1]: To help me avoid bloating the repo with obvious proofs, feel free to expand the templates and confirm a few examples.


## 2-D Foundation of the Log-Tower

Now that we've laid some of the groundwork by defining the 2-D structure of $R_{(n_x,n_y)}$ it's time to see where it fits into the foundation of the Log-Tower.

Recall that our 1-D work led us to see $P(A_n) = P((Rh)_n)$ as the binomial convolution of derivatives of $R$ and $h$ following the Leibniz Rule:

$$A_n = \sum_{k=0}^{n} \binom{n}{k} R_{n-k} h_k$$

If we extend $R_n$ and $h_n$ to $R_{(n_x,n_y)}$ and $h_{(n_x,n_y)}$, we begin to see its partial derivatives as a matrix of all possible derivative pairs.

Let's begin with $A=Rh$ and start taking partial derivatives of it with respect to $x$ and $y$.

$$A_{(1,0)} = R_{(1,0)}h + Rh_{(1,0)}$$

$$A_{(1,1)} = R_{(1,1)}h + R_{(1,0)}h_{(0,1)} + R_{(0,1)}h_{(1,0)} + Rh_{(1,1)}$$

$$A_{(2,1)} = R_{(2,1)}h + 2R_{(1,1)}h_{(1,0)} + R_{(2,0)}h_{(0,1)} + R_{(0,1)}h_{(2,0)} + 2R_{(1,0)}h_{(1,1)} + Rh_{(2,1)}$$

$$A_{(2,2)} = R_{(2,2)}h + 2R_{(2,1)}h_{(0,1)} + R_{(2,0)}h_{(0,2)} + 2R_{(1,2)}h_{(1,0)} + 4R_{(1,1)}h_{(1,1)} + 2R_{(1,0)}h_{(1,2)} + R_{(0,2)}h_{(2,0)} + 2R_{(0,1)}h_{(2,1)} + Rh_{(2,2)}$$

Now, instead of leaving them in raw equation format, let's put them into matrix format so we can see more clearly what's happening with the binomial accumulation.

$$A_{(1,0)} = \begin{bmatrix}
    1 & 1 
\end{bmatrix}
\cdot
\begin{bmatrix}
    R_{(1,0)}h_{(0,0)} \\
    R_{(0,0)}h_{(1,0)} 
\end{bmatrix}
\cdot
\begin{bmatrix}
    1 
\end{bmatrix}$$

$$A_{(1,1)} = \begin{bmatrix}
    1 & 1 
\end{bmatrix}
\cdot
\begin{bmatrix}
    R_{(1,1)}h_{(0,0)} & R_{(1,0)}h_{(0,1)} \\
    R_{(0,1)}h_{(1,0)} & R_{(0,0)}h_{(1,1)} 
\end{bmatrix}
\cdot
\begin{bmatrix}
    1 \\
    1
\end{bmatrix}$$

$$A_{(2,1)} = \begin{bmatrix}
    1 & 2 & 1 
\end{bmatrix}
\cdot
\begin{bmatrix}
    R_{(2,1)}h_{(0,0)} & R_{(2,0)}h_{(0,1)} \\
    R_{(1,1)}h_{(1,0)} & R_{(1,0)}h_{(1,1)} \\
    R_{(0,1)}h_{(2,0)} & R_{(0,0)}h_{(2,1)} 
\end{bmatrix}
\cdot
\begin{bmatrix}
    1 \\
    1
\end{bmatrix}$$

$$A_{(2,2)} = \begin{bmatrix}
    1 & 2 & 1 
\end{bmatrix}
\cdot
\begin{bmatrix}
    R_{(2,2)}h_{(0,0)} & R_{(2,1)}h_{(0,1)} & R_{(2,0)}h_{(0,2)} \\
    R_{(1,2)}h_{(1,0)} & R_{(1,1)}h_{(1,1)} & R_{(1,0)}h_{(1,2)} \\
    R_{(0,2)}h_{(2,0)} & R_{(0,1)}h_{(2,1)} & R_{(0,0)}h_{(2,2)}
\end{bmatrix}
\cdot
\begin{bmatrix}
    1 \\
    2 \\
    1
\end{bmatrix}$$

Note the x-decay going down and the y-decay going across all matrices with respect to $R_{(n_x,n_y)}$. This structure leads to the combinatorial row of Pascal's triangle clearly matching the order of the partial derivative with respect to $x$ on the left and with respect to $y$ on the right, or, stated more formally, a bilinear form where the left and right vectors are rows from Pascal's triangle, acting upon a matrix of the mixed partials.

When it comes to derivatives, mathematicians have a shorthand for this kind of binomial accumulation.

Here it is for $A = Rh$.

$$A_\alpha = D^\alpha (Rh) = \sum_{\beta \leq \alpha} \binom{\alpha}{\beta} D^{\alpha-\beta}R\cdot D^\beta h$$

This is known as the **General (or Multivariate) Leibniz Rule**, expressed using multi-index notation.

Don't be intimidated by the odd look to it if you've never seen this kind of notation before. If you understand the matrices above and what a derivative is, you already get the gist of it, even if you don't know precisely what the definition of each part of the notation is.

$\alpha$ represents the pair of indices, $(n_x,n_y)$, and $D^\alpha$ is the derivative operator, meaning that $D^\alpha (Rh)$ represents the $n_x$ -th and $n_y$ -th partial derivative with respect to $x$ and $y$ of $A=Rh$ in the 2-D case. Instead of having an index, $n$, we now have a vector, $\alpha = (n_x,n_y)$.

Note that if the equation were referring to a 4-D system, $\alpha$ would be $(n_x,n_y,n_z,n_t)$ and $D^\alpha (Rh)$ would represent a partial derivative with respect to $x$, $y$, $z$ and $t$.

As to $\binom{\alpha}{\beta}$, in the 2-D case, it's the simple multiplication of $n_x$ choose $k_x$ and $n_y$ choose $k_y$, or

$$\binom{\alpha}{\beta} = \binom{n_x}{k_x} \cdot \binom{n_y}{k_y}$$

Looking at $\beta$ this way helps to understand why $\beta \leq \alpha$ sits under the sum. $\beta$ represents all of the partial derivative order values that are less than or equal to $(n_x,n_y)$. In the case of $A_{(2,2)}$,

$$(k_x,k_y) = \beta \in \left[(0,0), (1,0), (2,0), (0,1), (1,1), (2,1), (0,2), (1,2), (2,2)\right]$$

$D^\beta h$ above represents $h_{(k_x,k_y)}$ and $D^{\alpha-\beta}R$ represents $R_{(n_x - k_x,n_y - k_y)}$ which conserves the partial derivative order with respect to $x$ and $y$ in the matrix of mixed partials you see above for $A_{(2,2)}$.

In essence, when you're looking at that notation, you're looking at a binomially-weighted, _n_-dimensional matrix of mixed partials.

Take some time to understand this notation. Feel free to read the description over a few times if this is new to you. It will feature prominently for the balance of the walkthrough.

### Understanding $R_{(n_x,n_y)}$

As before with our 1-D work, understanding how to expand $\Omega$ into a multivariate solution will require understanding derivatives of $R$, but this time we need to understand a matrix of partial derivatives instead of simply understanding $R_n$.

Recall from above that we now have two base identities, one for $R_{(1,0)}$ and one for $R_{(0,1)}$:

$$\frac{\partial}{\partial x} R = R_{(1,0)} = G^{(x)} - F^{(x)}R$$

and 

$$\frac{\partial}{\partial y} R = R_{(0,1)} = G^{(y)} - F^{(y)}R$$

Also recall that both formulations of $R_{(1,1)}$

$$\frac{\partial}{\partial y} R_{(1,0)} = R_{(1,1)} = G^{(x)}\_{(0,1)} - F^{(x)}\_{(0,1)}R - F^{(x)}R\_{(0,1)}$$

$$\frac{\partial}{\partial x} R_{(0,1)} = R_{(1,1)} = G^{(y)}\_{(1,0)} - F^{(y)}\_{(1,0)}R - F^{(y)}R\_{(1,0)}$$

are algebraically equivalent. If you swap all the $x$ and $y$ indices, you get the same expression.

For the sake of brevity, going forward, instead of presenting both paths, we are going to assume that a partial with respect to $x$ is taken first.

Since we will be using this assumption for the rest of the walkthrough, let's give it a name: the **_x_-convention**.

So, to get to $R_{(1,1)}$ we take this path

$$\frac{\partial}{\partial y} R_{(1,0)} = R_{(1,1)} = G^{(x)}\_{(0,1)} - F^{(x)}\_{(0,1)}R - F^{(x)}R\_{(0,1)}$$

Again, let's take some partial derivatives and see where this path takes us:

$$\frac{\partial}{\partial x} R_{(1,1)} = R_{(2,1)} = G^{(x)}\_{(1,1)} - F^{(x)}\_{(1,1)}R - F^{(x)}\_{(0,1)}R_{(1,0)} - F^{(x)}_{(1,0)}R\_{(0,1)}- F^{(x)}R\_{(1,1)}$$

$$\frac{\partial}{\partial y} R_{(2,1)} = R_{(2,2)} = G^{(x)}\_{(1,2)} - F^{(x)}\_{(1,2)}R - 2F^{(x)}\_{(1,1)}R_{(0,1)} - F^{(x)}\_{(0,2)}R_{(1,0)} - F^{(x)}\_{(1,0)}R\_{(0,2)} - 2F^{(x)}_{(0,1)}R\_{(1,1)}- F^{(x)}R\_{(1,2)}$$

$$\frac{\partial}{\partial x} R_{(2,2)} = R_{(3,2)} =   G^{(x)}\_{(2,2)} - F^{(x)}\_{(2,2)}R_{(0,0)} - 2F^{(x)}\_{(2,1)}R_{(0,1)} - F^{(x)}\_{(2,0)}R_{(0,2)} - 2F^{(x)}\_{(1,2)}R_{(1,0)} - 4F^{(x)}\_{(1,1)}R_{(1,1)} - 2F^{(x)}\_{(1,0)}R_{(1,2)} - F^{(x)}\_{(0,2)}R_{(2,0)} - 2F^{(x)}\_{(0,1)}R_{(2,1)} - F^{(x)}\_{(0,0)}R_{(2,2)}$$


Unsurprisingly, we find ourselves going down a similar rabbit hole as before, but this time we perform the operation on the partial identity with respect to $x$:

$$R_{(1,1)} = G^{(x)}\_{(0,1)} - \begin{bmatrix}
    1 
\end{bmatrix}
\cdot
\begin{bmatrix}
    F^{(x)}\_{(0,1)}R_{(0,0)} & F^{(x)}\_{(0,0)}R_{(0,1)} 
\end{bmatrix}
\cdot
\begin{bmatrix}
    1 \\
    1
\end{bmatrix}$$

$$R_{(2,1)} = G^{(x)}\_{(1,1)} - \begin{bmatrix}
    1 & 1 
\end{bmatrix}
\cdot
\begin{bmatrix}
    F^{(x)}\_{(1,1)}R_{(0,0)} & F^{(x)}\_{(1,0)}R_{(0,1)} \\
    F^{(x)}\_{(0,1)}R_{(1,0)} & F^{(x)}\_{(0,0)}R_{(1,1)}
\end{bmatrix}
\cdot
\begin{bmatrix}
    1 \\
    1
\end{bmatrix}$$

$$R_{(2,2)} = G^{(x)}\_{(1,2)} - \begin{bmatrix}
    1 & 1 
\end{bmatrix}
\cdot
\begin{bmatrix}
    F^{(x)}\_{(1,2)}R_{(0,0)} & F^{(x)}\_{(1,1)}R_{(0,1)} & F^{(x)}\_{(1,0)}R_{(0,2)} \\
    F^{(x)}\_{(0,2)}R_{(1,0)} & F^{(x)}\_{(0,1)}R_{(1,1)} & F^{(x)}\_{(0,0)}R_{(1,2)}
\end{bmatrix}
\cdot
\begin{bmatrix}
    1 \\
    2 \\
    1
\end{bmatrix}$$


$$R_{(3,2)} = G^{(x)}\_{(2,2)} - \begin{bmatrix}
    1 & 2 & 1
\end{bmatrix}
\cdot
\begin{bmatrix}
    F^{(x)}\_{(2,2)}R_{(0,0)} & F^{(x)}\_{(2,1)}R_{(0,1)} & F^{(x)}\_{(2,0)}R_{(0,2)} \\
    F^{(x)}\_{(1,2)}R_{(1,0)} & F^{(x)}\_{(1,1)}R_{(1,1)} & F^{(x)}\_{(1,0)}R_{(1,2)} \\
    F^{(x)}\_{(0,2)}R_{(2,0)} & F^{(x)}\_{(0,1)}R_{(2,1)} & F^{(x)}\_{(0,0)}R_{(2,2)}
\end{bmatrix}
\cdot
\begin{bmatrix}
    1 \\
    2 \\
    1
\end{bmatrix}$$

which again leads us to invoke the multivariate Leibniz Rule, but this time with an index shift of $(n_x - 1,n_y)$ which is expressed as $-e_x$:

$$D^\alpha R = D^{\alpha - e_x} G^{(x)} - \sum_{0 \le \beta \le \alpha - e_x} \binom{\alpha - e_x}{\beta} (D^{\alpha - e_x - \beta} F^{(x)}) (D^\beta R)$$

which looks eerily similar to our 1-D expression for $R_n$

$$R_n = G_\text{n-1}- \sum_{k=0}^{n-1} \binom{n-1}{k} F_{n-k-1} R_k$$

At the point where there are no partials with respect to $x$ to take, this equation will be represented as

$$D^\alpha R = D^{\alpha - e_y} G^{(y)} - \sum_{0 \le \beta \le \alpha - e_y} \binom{\alpha - e_y}{\beta} (D^{\alpha - e_y - \beta} F^{(y)}) (D^\beta R)$$

So, a more general form of the multivariate formula will be represented as 

$$D^\alpha R = D^{\alpha - e_w} G^{(w)} - \sum_{0 \le \beta \le \alpha - e_w} \binom{\alpha - e_w}{\beta} (D^{\alpha - e_w - \beta} F^{(w)}) (D^\beta R)$$

where $w$ represents whichever dimension is invoked. Since $w$ can be any dimension, this representation is $n$ -dimensional.



Those who looked back to see what the formula was listed as in Part 3 will note that the $F$ and the $R$ have switched places. Because the entire $n-1$ row of pascal's triangle is invoked in the formula, we're allowed to do that because they are symmetrical (i.e., rows like 1,2,1 and 1,3,3,1 are symmetrical whereas the truncated verions like 1,2 and 1,3,3 that we see in the $\Gamma_n$ expression are not). Counting from one side or the other makes no difference to this convolution.

Now, we need to express everything in terms of $R$, which necessitates understanding the makeup of $\Gamma$ and $\Phi$ and how they fit into _G_- and _F_-sector composition.

### What Is $\Gamma$, Really?

$\Gamma$ is the independent term that splits off from the $R$ -coefficient when we take derivatives of $R$, also known as the **forcing term**. We see it clearly in our 1-D work. But how does it shape up in two dimensions?

So far, we've seen $R_{(0,1)}$, $R_{(1,0)}$, and $R_{(1,1)}$, so we've seen the first few expressions of it. Let's take a closer look.

$$\frac{\partial}{\partial x} R = R_{(1,0)} = G^{(x)} - F^{(x)}R = \Gamma_{(1,0)} - \Phi_{(1,0)}R$$

$$\frac{\partial}{\partial x} R = R_{(0,1)} = G^{(y)} - F^{(y)}R = \Gamma_{(0,1)} - \Phi_{(0,1)}R$$

Whoa. Wait a minute. Weren't the first expressions of $\Gamma$ and $\Phi$ flat zero subscripts in our 1-D work? Yep. They were. Those subscripts were designed to match Bell notation, indicating how many times the derivative operator was applied to the module.

Now that we're working in two dimensions, the underlying multivariate structure has turned $A(x,y)$ into a matrix run by vectors and they need somewhere to start.

When we were working in 1-D, the symmetry didn't need to include the $h_n$ term in $A_n = \frac{d^n}{dx^n} Rh = R(h_n - \text{F-sector}) + \text{G-sector}$.

Now it does. Let's see why and how.

### The _n_-Dimensional Canonical Form

Let's look at $R_{(1,1)}$ to see how $\Gamma$ and $\Phi$ evolve through $(n_x,n_y)$.

Recall from earlier,

$$\frac{\partial}{\partial y} R_{(1,0)} = R_{(1,1)} = G^{(x)}\_{\text{(0,1)}} - F^{(x)}\_{\text{(0,1)}}R - F^{(x)}R\_{\text{(0,1)}} = \underbrace{\left[ G^{(x)}_{(0,1)} - F^{(x)}G^{(y)} \right]}\_{\text{Independent Term } (\Gamma)} - R \cdot \underbrace{\left[ F^{(x)}_{(0,1)} - F^{(x)}F^{(y)} \right]}_{\text{Coefficient Term } (\Phi)}$$

So, that means

$$\frac{\partial}{\partial y} R_{(1,0)} = R_{(1,1)} = \left[ G^{(x)}_{(0,1)} - G^{(y)}F^{(x)} \right] - \left[ F^{(x)}_{(0,1)} - F^{(y)}F^{(x)} \right]R = \Gamma_{(1,1)} - \Phi_{(1,1)}R$$

Before we move on, let's first recall what $R_2$ looked like from our 1-D work:

$$R_2 = (G_1-GF) - (F_1-FF)R = \Gamma_1 - \Phi_1 R$$

And now $A_2$:

$$A_2 = R(h_2 - (2h_1F + h(F_1 - FF))) + (2h_1G + h(G_1 - GF)) = R(h_2 - (2h_1\Phi_0 + h\Phi_1)) + (2h_1\Gamma_0 + h\Gamma_1)$$

So we see that the underlying structure of $A_{(1,1)}$ must have a kinship with $A_2$, which makes sense since every term includes both $x$ and $y$ elements, leading to successive partial derivatives in our 2-D framework evolving the same total number of terms as in 1-D when $n_x + n_y = n$.

Let's make that kinship explicit. Here's $A_{(1,1)}$.

$$A_{(1,1)} = \begin{bmatrix}
    1 & 1 
\end{bmatrix}
\cdot
\begin{bmatrix}
    R_{(1,1)}h_{(0,0)} & R_{(1,0)}h_{(0,1)} \\
    R_{(0,1)}h_{(1,0)} & R_{(0,0)}h_{(1,1)} 
\end{bmatrix}
\cdot
\begin{bmatrix}
    1 \\
    1
\end{bmatrix} = \begin{bmatrix}
    1 & 1 
\end{bmatrix}
\cdot
\begin{bmatrix}
    (\Gamma_{(1,1)} - \Phi_{(1,1)}R)h_{(0,0)} & (\Gamma_{(1,0)} - \Phi_{(1,0)}R)h_{(0,1)} \\
    (\Gamma_{(0,1)} - \Phi_{(0,1)}R)h_{(1,0)} & (\Gamma_{(0,0)} - \Phi_{(0,0)}R)h_{(1,1)} 
\end{bmatrix}
\cdot
\begin{bmatrix}
    1 \\
    1
\end{bmatrix}$$

Since we know that

$$(\Gamma_{(0,0)} - \Phi_{(0,0)}R)h_{(1,1)} = Rh_{(1,1)}$$

**_we have no choice but to conclude that_ $\Gamma_{(0,0)} = 0$ and $\Phi_{(0,0)} = -1$**.

> [!NOTE]
> Make special note of these values for $\Gamma_{(0,0)}$ and $\Phi_{(0,0)}$. They will be critical in understanding the entire multivariate structure.


Matrix addition rules naturally lead to the form

$$A_{(1,1)} = \begin{bmatrix}
    1 & 1 
\end{bmatrix}
\cdot
\left(
\begin{bmatrix}
    \Gamma_{(1,1)}h_{(0,0)} & \Gamma_{(1,0)}h_{(0,1)} \\
    \Gamma_{(0,1)}h_{(1,0)} & \Gamma_{(0,0)}h_{(1,1)} 
\end{bmatrix} -
R \cdot
\begin{bmatrix}
    \Phi_{(1,1)}h_{(0,0)} & \Phi_{(1,0)}h_{(0,1)} \\
    \Phi_{(0,1)}h_{(1,0)} & \Phi_{(0,0)}h_{(1,1)} 
\end{bmatrix}
\right)
\cdot
\begin{bmatrix}
    1 \\
    1
\end{bmatrix}$$

But, since $\Gamma_{(0,0)} = 0$ and $\Phi_{(0,0)} = -1$,

$$A_{(1,1)} = \begin{bmatrix}
    1 & 1 
\end{bmatrix}
\cdot
\left(
\begin{bmatrix}
    \Gamma_{(1,1)}h_{(0,0)} & \Gamma_{(1,0)}h_{(0,1)} \\
    \Gamma_{(0,1)}h_{(1,0)} & 0 
\end{bmatrix} -
R \cdot
\begin{bmatrix}
    \Phi_{(1,1)}h_{(0,0)} & \Phi_{(1,0)}h_{(0,1)} \\
    \Phi_{(0,1)}h_{(1,0)} & (-1)h_{(1,1)} 
\end{bmatrix}
\right)
\cdot
\begin{bmatrix}
    1 \\
    1
\end{bmatrix}$$

Now we have a template that provides us with a 2-D concept of what any $A_{(n_x,n_y)}$ would look like. For example,

$$A_{(2,3)} = \begin{bmatrix}
    1 & 2 & 1 
\end{bmatrix}
\cdot
\left(
\begin{bmatrix}
    \Gamma_{(2,3)}h_{(0,0)} & \Gamma_{(2,2)}h_{(0,1)} & \Gamma_{(2,1)}h_{(0,2)} & \Gamma_{(2,0)}h_{(0,3)} \\
    \Gamma_{(1,3)}h_{(1,0)} & \Gamma_{(1,2)}h_{(1,1)} & \Gamma_{(1,1)}h_{(1,2)} & \Gamma_{(1,0)}h_{(1,3)} \\
    \Gamma_{(0,3)}h_{(2,0)} & \Gamma_{(0,2)}h_{(2,1)} & \Gamma_{(0,1)}h_{(2,2)} & 0 
\end{bmatrix} -
R \cdot
\begin{bmatrix}
    \Phi_{(2,3)}h_{(0,0)} & \Phi_{(2,2)}h_{(0,1)} & \Phi_{(2,1)}h_{(0,2)} & \Phi_{(2,0)}h_{(0,3)} \\
    \Phi_{(1,3)}h_{(1,0)} & \Phi_{(1,2)}h_{(1,1)} & \Phi_{(1,1)}h_{(1,2)} & \Phi_{(1,0)}h_{(1,3)} \\
    \Phi_{(0,3)}h_{(2,0)} & \Phi_{(0,2)}h_{(2,1)} & \Phi_{(0,1)}h_{(2,2)} & (-1)h_{(2,3)} 
\end{bmatrix}
\right)
\cdot
\begin{bmatrix}
    1 \\
    3 \\
    3 \\
    1
\end{bmatrix}$$

And, since this matrix multiplication is distributive, we can express our new 2-D _G_-sector as

$$A_{(2,3)G} = \begin{bmatrix}
    1 & 2 & 1 
\end{bmatrix}
\cdot
\begin{bmatrix}
    \Gamma_{(2,3)}h_{(0,0)} & \Gamma_{(2,2)}h_{(0,1)} & \Gamma_{(2,1)}h_{(0,2)} & \Gamma_{(2,0)}h_{(0,3)} \\
    \Gamma_{(1,3)}h_{(1,0)} & \Gamma_{(1,2)}h_{(1,1)} & \Gamma_{(1,1)}h_{(1,2)} & \Gamma_{(1,0)}h_{(1,3)} \\
    \Gamma_{(0,3)}h_{(2,0)} & \Gamma_{(0,2)}h_{(2,1)} & \Gamma_{(0,1)}h_{(2,2)} & 0 
\end{bmatrix}
\cdot
\begin{bmatrix}
    1 \\
    3 \\
    3 \\
    1
\end{bmatrix}$$

which allows us to write an explicit multivariate form for the G-sector as

$$A_{\alpha G} = \sum_{\beta \leq \alpha,\beta \neq \alpha} \binom{\alpha}{\beta}  \Gamma_{\alpha - \beta} D^\beta h$$

Note the similarities to our 1-D version. Remember that, in this version, $\Gamma_0 = G_0$, not zero, explaining the $n-1$ in the $\Gamma$ subscript.

$$A_{nG} = \sum_{k=0}^{n-1} \binom{n}{k} h_k \Gamma_{n-k-1}$$

This allows us to write an explicit multivariate formulation of $A_\alpha$ in the canonical form:

$$A_\alpha = R(h_\alpha - A_{\alpha F}) + A_{\alpha G} = R\left(h_\alpha - \sum\_{\beta \leq \alpha,\beta \neq \alpha} \binom{\alpha}{\beta}  \Phi_{\alpha - \beta} D^\beta h\right) + \sum_{\beta \leq \alpha,\beta \neq \alpha} \binom{\alpha}{\beta}  \Gamma_{\alpha - \beta} D^\beta h$$

Note how $h_\alpha$ sits outside the _F_-sector summation. Since $\Gamma_{(0,0)} = 0$ and $\Phi_{(0,0)} = -1$, the case where $\beta = \alpha$ naturally ejects $R h_\alpha$ out of the sums.

The real marvel of this formula is that it doesn't just work in two dimensions. It is now **_n_-dimensional**, meaning it can apply to a theoretically infinite number of dimensions.

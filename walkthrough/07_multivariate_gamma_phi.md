# Part 7: The Alpha...

An analysis of $A_\alpha$ that began in two dimensions led us directly to a canonical form of the generator that could handle an infinite number of dimensions by the end of the last part.

Pretty as it is though, the form is not particularly useful if we can't memoize an $n$ -dimensional $\Omega$ cache, or even develop an operator that allows for rapid calculation of all the necessary $\Gamma$ 's and $\Phi$ 's. Our success in utilizing algebraic symmetry to do so in one dimension has shown that it's possible to accomplish.

But how?

## Smooth Operator

Let's begin by figuring out how to calculate $\Gamma_{(n_x,n_y)}$ and $\Phi_{(n_x,n_y)}$ recursively based on the work we've done up until now since, if we can calculate all required $\Gamma_{(n_x,n_y)}$ expressions for a given $A_{(n_x,n_y)G}$, we are likely to see how a multivariate $\Omega$ may fit into the mix.

Recall from our 1-D work that our discoveries regarding $\Omega_{m,n}$ came from studying $\Gamma_n$ so it's a reasonable place to start.

Fortunately, we've already done some multivariate work on $R_{(n_x,n_y)}$, so we have a starting equation from which we can extract **operators** that can **shift** us up the ladder from lower-rung $\Gamma$ 's and $\Phi$ 's to ones of higher order (i.e., the $\Gamma$ and $\Phi$ **shift operators**).

### Don't Go Chasing Waterfalls

Recall that partial derivatives of $R(x,y)$ are described by this multivariate equation developed in Part 6:

$$D^\alpha R = D^{\alpha - e_w} G^{(w)} - \sum_{0 \le \beta \le \alpha - e_w} \binom{\alpha - e_w}{\beta} (D^{\alpha - e_w - \beta} F^{(w)}) (D^\beta R)$$

Our work in the last section also established that $R_\alpha = \Gamma_\alpha - \Phi_\alpha R$, so let's replace the multivariate derivative operators on $R$ using this identity:

$$\Gamma_\alpha - \Phi_\alpha R = D^{\alpha - e_w} G^{(w)} - \sum_{0 \le \beta \le \alpha - e_w} \binom{\alpha - e_w}{\beta} (D^{\alpha - e_w - \beta} F^{(w)}) (\Gamma_\beta - \Phi_\beta R)$$

To extract $\Gamma_\alpha$, we simply isolate the terms independent of $R$. Conceptually, you can think of this like using MS Word's find and replace function to delete all the $-\Phi_\alpha R$ and $-\Phi_\beta R$ terms.

$$\Gamma_\alpha = D^{\alpha - e_w} G^{(w)} - \sum_{0 \le \beta \le \alpha - e_w} \binom{\alpha - e_w}{\beta} (D^{\alpha - e_w - \beta} F^{(w)}) \Gamma_\beta$$

And that's it. That's the $\Gamma_\alpha$ **shift operator**.

This mathematical manipulation sure beats parsing waterfall diagrams.

Let's also derive the $\Phi_\alpha$ **shift operator** in parallel by isolating the $R$ coefficients and multiplying by $-1$, which produces

$$\Phi_\alpha = - \sum_{0 \le \beta \le \alpha - e_w} \binom{\alpha - e_w}{\beta} (D^{\alpha - e_w - \beta} F^{(w)}) \Phi_\beta$$

Oddly, these equations don't appear to match our established 1-D naive recursions (i.e., "naive" meaning ones not based on $\Omega$) that we established based on derivatives of $R$. Let's take a look at them again with fresh eyes.

$$\Gamma_n = G_n - \sum_{k=0}^{n-1} \binom{n}{k} F_k \Gamma_{n-k-1}$$

$$\Phi_n = F_n - \sum_{k=0}^{n-1} \binom{n}{k} F_k \Phi_{n-k-1}$$

In our current equation for $\Gamma_n$, there are some $n$ 's where there are $\alpha - e_w$ 's in our multivariate form for $\Gamma_\alpha$. Ideally, there should be an equation with matching $n-1$  's in those spots.

Similarly, in our equation for $\Phi_n$, there's an $F_n$ term at the beginning where there's none at all in our multivariate form, and again, there appears to be a mismatch on $\binom{n}{k}$ where there is a $\binom{\alpha - e_w}{\beta}$ in the calculation of $\Phi_\alpha$.

Since the multivariate form should work for $n$ variables (including $n=1$, of course) we need to resolve these discrepancies.

### Zero to Hero

Recall that in our 1-D work, we set $\Gamma_0 = G_0$ and $\Phi_0 = F_0$. Instead, in our multivariate work, we discovered the necessity of setting different base cases below the floor of our 1-D work in the form of $\Gamma_{(0,0)} = 0$ and $\Phi_{(0,0)} = -1$

Let's re-index our 1-D work, setting $\Gamma_0 = 0$ and $\Phi_0 = -1$ to see if the equations line up better with our multivariate work.

If we set $\Gamma_0$ to 0, we get

$$ \Gamma_0 = 0 $$

$$ \Gamma_1 = G_0 - \Gamma_0F $$

$$ \Gamma_2 = G_1 - \Gamma_1F - \Gamma_0F_1 $$

$$ \Gamma_3 = G_2 - \Gamma_2F - 2\Gamma_1F_1 - 1\Gamma_0F_2 $$

$$ \Gamma_4 = G_3 - \Gamma_3F - 3\Gamma_2F_1 - 3\Gamma_1F_2 - 1\Gamma_0F_3 $$

Or, more succinctly,

$$\Gamma_n = G_{n-1} - \sum_{k=0}^{n-1} \binom{n-1}{k} F_{n-k-1} \Gamma_k$$

Notice how replacing $\Gamma_0$ with $0$ naturally bumps the $G$ index down by one. Since all $\Gamma_0$ values are zero, we now see properly why the right side of Pascal's triangle was truncated in our 1-D work. 

If you compare it side-by-side with our multivariate work, all indices suddenly line up exactly, allowing our multidimensional version to collapse to our 1-D equation when $n=1$.

Now let's do the same for $\Phi_n$, this time setting $\Phi_0 = -1$.

$$\Phi_0 = -1$$
$$\Phi_1 = - \Phi_0 F$$
$$\Phi_2 = - \Phi_1 F - \Phi_0 F_1$$
$$\Phi_3 = - \Phi_2 F - 2\Phi_1 F_1 - 1\Phi_0 F_2$$
$$\Phi_4 = - \Phi_3 F - 3\Phi_2 F_1 - 3\Phi_1 F_2 - 1\Phi_0 F_3$$

Which leads to 

$$\Phi_n = - \sum_{k=0}^{n-1} \binom{n-1}{k} F_{n-k-1} \Phi_k$$

If you insert $-1$ into all $\Phi_0$ above, you get precisely the same algebraic result as before, but now the index has moved forward on all $\Phi$ by one.

See how replacing $\Phi_0$ with $-1$ naturally absorbs the standalone $F_n$ term into the summation? Now we can see why the right side of Pascal was truncated here before; it was sitting on the left. It's finally folded properly into the recursion, so the structure is now clean.

Again, if you compare this equation side-by-side with the multivariate version, the indices line up perfectly.

Since we've re-indexed our formulas for $\Gamma_n$ and $\Phi_n$ and developed multidimensional representations for them, lets re-index all of our prior work to match and extend it to the final $n$ -dimensional form of the generator.

### It's _Deja Vu_ All Over Again

Since $\Gamma_n$ and $\Phi_n$ have advanced by one, the corollary to the generator now becomes

$$P(R_n) = \Gamma_n - R\Phi_n$$

which lines up much better with its established multidimensional form,

$$P(R_\alpha) = \Gamma_\alpha - R_\emptyset \Phi_\alpha$$

Since $P(A_n)$ has been established as

$$P(A_n) = \sum_{k=0}^n \binom{n}{k} h_kR_{n-k}$$

our new 1-D generator form becomes

$$P(A_n) = \sum_{k=0}^{n} \binom{n}{k} h_k \big( \Gamma_{n-k} - R\Phi_{n-k} \big)$$

which is now a clean binomial convolution of $h_k$ and values of $\Gamma_{n-k}$ and $\Phi_{n-k}$.

Similarly, the multidimensional form is most efficiently represented as

$$P(A_\alpha) = \sum_{\beta \le \alpha} \binom{\alpha}{\beta} h_\beta \big( \Gamma_{\alpha-\beta} - R_\emptyset \Phi_{\alpha-\beta} \big)$$

## So What?

Since we have the most efficiently presented multidimensional form of $P(A_\alpha)$ possible and a bulletproof way to produce all $\Gamma_\alpha$ and $\Phi_\alpha$, we've not only achieved our goal of being able to produce

$$\frac{\partial^{(n_x+n_y+n_z+n_t)}}{\partial x^{n_x} \partial y^{n_y} \partial z^{n_z} \partial t^{n_t}} A(x,y,z,t) = \frac{\partial^{(n_x+n_y+n_z+n_t)}}{\partial x^{n_x} \partial y^{n_y} \partial z^{n_z}  \partial t^{n_t}} \left(h(x,y,z,t)\frac{\text{ln}g(x,y,z,t)}{\text{ln}f(x,y,z,t)}\right)$$

but we've also blown _literally infinitely_ past it and can now create

$$\frac{\partial^{(n_{x_1}+n_{x_2}+\dots+n_{x_m})}}{\partial x_1^{n_{x_1}}\partial x_2^{n_{x_2}}\dots\partial x_m^{n_{x_m}} } A(x_1,x_2,\dots,x_m) = \frac{\partial^{(n_{x_1}+n_{x_2}+\dots+n_{x_m})}}{\partial x_1^{n_{x_1}}\partial x_2^{n_{x_2}}\dots\partial x_m^{n_{x_m}}} \left(h(x_1,x_2,\dots,x_m)\frac{\text{ln}g(x_1,x_2,\dots,x_m)}{\text{ln}f(x_1,x_2,\dots,x_m)}\right)$$

for any whole number dimensionality, $m$.

But, of course, we're not quite done. 

### Closing Time Again and Again

Closing our new 1-D equations for $\Gamma_n$ and $\Phi_n$ will be a simple exercise now that we know how. Also, since the recursions are cleaner, the math will be easier to parse.

You might be asking, "Why bother closing these in one dimension when a multidimensional closure automatically covers the 1-D case?"

Now that things are cleaned up, we'll get a clearer picture of the 1-D structure during the closing process.

We define our usual EGFs as

$$\overline{\gamma}(x) = \sum_{n=0}^{\infty} \Gamma_n \frac{x^n}{n!} \quad \text{,} \quad \overline{\phi}(x) = \sum_{n=0}^{\infty} \Phi_n \frac{x^n}{n!} \quad \text{,} \quad  \overline{g}(x) = \sum_{n=0}^{\infty} G_n \frac{x^n}{n!} \quad \text{and} \quad  \overline{f}(x) = \sum_{n=0}^{\infty} F_n \frac{x^n}{n!}$$

Let's start this time by closing $\Phi_n$.

Our recursion starts as

$$\Phi_n = - \sum_{k=0}^{n-1} \binom{n-1}{k} F_{n-k-1} \Phi_k$$

Since there's an $n-1$ in the binomial, we already know to start by multiplying through by $\frac{x^{n-1}}{(n-1)!}$ and summing from 1 to infinity.

$$\sum_{n=1}^{\infty} \Phi_n \frac{x^{n-1}}{(n-1)!} = -\sum_{n=1}^{\infty} \frac{x^{n-1}}{(n-1)!} \sum_{k=0}^{n-1} \binom{n-1}{k} F_{n-k-1} \Phi_k$$

As before, we use the fact that $\binom{n-1}{k} = \frac{(n-1)!}{k!(n-1-k)!}$ and some clever exponent adding and subtracting to get

$$RHS = -\sum_{n=1}^{\infty} \sum_{k=0}^{n-1} F_{n-k-1}\frac{x^{n-k-1}}{(n-k-1)!} \Phi_k\frac{x^{k}}{k!}$$

Which is an exact convolution of $-\overline{f}$ and $\overline{\phi}$.

The LHS clearly represents $\frac{d}{dx} \overline{\phi}$, so we have

$$\frac{d}{dx} \overline{\phi}(x) = - \overline{f}(x)\overline{\phi}(x)$$

Even though we have a base case of $\Phi_0 = -1$, when we take the derivative of $\overline{\phi}$ to build our differential equation, the constant term $\Phi_0$ is eliminated. Since there are no orphaned terms on the right, there is no straggling $e^x$ this time around.

This yields the linear first-order ODE

$$y' + \overline{f}(x)y = 0$$

where $y=\overline{\phi}$.

We then define the integrating factor using $H(x)$, where $H(x)$ is the definite integral of $\overline{f}(t)$:

$$H(x) = \int_0^x \overline{f}(t) dt$$

Note that evaluating this at $x=0$ naturally yields $H(0) = 0$.

Now we multiply through by the integrating factor

$$y' e^{H(x)} + \overline{f}(x) y e^{H(x)} = 0$$

By the reverse product rule, the left-hand side condenses into a single derivative

$$\frac{d}{dx} \left[ y(x) e^{H(x)} \right] = 0$$

Then we integrate both sides with respect to $t$ from $0$ to $x$:

$$\int_0^x \frac{d}{dt} \left[ y(t) e^{H(t)} \right] dt = \int_0^x 0 dt$$

$$y(x) e^{H(x)} - y(0) e^{H(0)} = 0$$

The base case $\Phi_0 = -1$ establishes that $y(0) = -1$. Because $H(0) = 0$, we know $e^{H(0)} = 1$. Substituting these knowns into the equation:

$$y(x) e^{H(x)} - (-1)(1) = 0$$

$$y(x) e^{H(x)} + 1 = 0$$

$$y(x) e^{H(x)} = -1$$

which gives us the generalized closed form:

$$y(x) = -e^{-H(x)}$$

When we write it with the explicit integral, we get

$$\overline{\phi}(x) = -e^{-\int_0^x \overline{f}(t) dt}$$

Until now, we haven't calculated $H(x) = \int_0^x \overline{f}(t) dt$ explicitly. Time to remedy that situation.

### Even More Exponentially Elegant

To integrate $H(x)$, we first need to recognize the continuous function that $\overline{f}(x)$ represents.

The EGFs we've been defining to close our recursions are of the form

$$\overline{f}(x) = \sum_{n=0}^{\infty} F_n \frac{x^n}{n!}$$

Since $F_n$ are successive derivatives of $F$ evaluated at zero,

$$\overline{f}(t) = \sum_{n=0}^{\infty} F_n \frac{t^n}{n!} = \sum_{n=0}^{\infty} \left[ \frac{d^n}{dt^n} \left( \frac{f'(t)}{f(t) \ln(f(t))} \right) \right]_{t=0} \frac{t^n}{n!}$$

This is the literal textbook definition of a Maclaurin series, which is the special case of a Taylor series where the function in question is evaluated at zero. [^1]

[^1]: Knowledge of the inner workings of Taylor and Maclaurin series will be assumed in this part. Those who would like a primer should head to the good people at openstax [here](https://openstax.org/books/calculus-volume-2/pages/6-3-taylor-and-maclaurin-series) .

Assuming $f(x)$ is stable around $f(0)$, which it must be for the sector decomposition to hold, the infinite Maclaurin series reduces to

$$\overline{f}(t) = \sum_{n=0}^{\infty} \left[ \frac{d^n}{dt^n} \left( \frac{f'(t)}{f(t) \ln(f(t))} \right) \right]_{t=0} \frac{t^n}{n!} = \frac{f'(t)}{f(t)\ln(f(t))}$$

This particular function is straightforward to integrate through $u$ substitution. Let $u = ln(f(t))$ and, therefore, $du = \frac{f'(t)}{f(t)}dt$, so

$$\int_0^x \left( \frac{f'(t)}{f(t) \ln(f(t))} \right) dt = \int_{\text{ln} f(0)}^{\text{ln} f(x)} \frac{du}{u} = \left. \text{ln}(u) \right|_{\text{ln} f(0)}^{\text{ln} f(x)}$$

Which evaluates to

$$\int_0^x \overline{f}(t) dt = \ln(\ln(f(x))) - \ln(\ln(f(0)))$$

Substituting this expression directly into the exponent of the integrating factor cancels the exponential and simplifies $\overline{\phi}(x)$ to:

$$\overline{\phi}(x) = - \frac{\ln(f(0))}{\ln(f(x))}$$

Recognizing the EGFs we've been working with as Maclaurin series simplifies the closure of $\Gamma_n$.

Recall that

$$\Gamma_n = G_{n-1} - \sum_{k=0}^{n-1} \binom{n-1}{k} F_{n-k-1} \Gamma_k$$

If we multiply both sides by $\frac{x^{n-1}}{(n-1)!}$ and sum from $n=1$ to $\infty$, the left side evaluates to the derivative, $\overline{\gamma}'(x)$ while the right side splits into two parts. The shift in $G_{n-1}$ translates cleanly to $\overline{g}(x)$, and the summation is the exact Cauchy product of $\overline{f}(x)$ and $\overline{\gamma}(x)$ which gives us a first-order linear ODE of:

$$\overline{\gamma}'(x) = \overline{g}(x) - \overline{f}(x)\overline{\gamma}(x)$$

Going through the usual process and recalling the base case $\Gamma_0 = 0$, isolating $\overline{\gamma}$ yields the general closed form:

$$\overline{\gamma}(x) = e^{-H(x)} \int_0^x \overline{g}(t) e^{H(t)} dt$$

We already know the integrating factor and its inverse evaluate to

$$e^{H(t)} = \frac{\ln(f(t))}{\ln(f(0))} \quad \text{and} \quad e^{-H(x)} = \frac{\ln(f(0))}{\ln(f(x))}$$

Since $\overline{g}(t) = \frac{g'(t)}{g(t) \ln(f(t))}$, substituting into the integrand cancels the $\ln(f(t))$ terms:

$$\overline{g}(t) e^{H(t)} = \left( \frac{g'(t)}{g(t) \ln(f(t))} \right) \left( \frac{\ln(f(t))}{\ln(f(0))} \right) = \frac{g'(t)}{g(t) \ln(f(0))}$$

Integrating it from $0$ to $x$ yields

$$\int_0^x \frac{g'(t)}{g(t) \ln(f(0))} dt = \frac{1}{\ln(f(0))} \left[ \ln(g(x)) - \ln(g(0)) \right]$$

Finally, we multiply this result by our external $e^{-H(x)}$ term to get:

$$\overline{\gamma}(x) = \left( \frac{\ln(f(0))}{\ln(f(x))} \right) \left( \frac{\ln(g(x)) - \ln(g(0))}{\ln(f(0))} \right) = \frac{\ln(g(x)) - \ln(g(0))}{\ln(f(x))}$$

Let's now go over why we bothered closing these 1-D forms at all.

### Proving the $R_n$ Identity Axiomatically

If we break apart the final closed form of $\overline{\gamma}(x)$, the underlying symmetry finally begins to come into analytic focus:

$$\overline{\gamma}(x) = \frac{\ln(g(x))}{\ln(f(x))} - \frac{\ln(g(0))}{\ln(f(x))}$$

Assuming $\overline{r}(x) = \sum_{n=0}^{\infty}R_n\frac{x^n}{n!}$ and recognizing that $\overline{\phi}(x) = -\frac{\ln(f(0))}{\ln(f(x))}$, we can rewrite the terms as:

$$\overline{\gamma}(x) = \frac{\ln(g(x))}{\ln(f(x))} - \frac{\ln(g(0))}{\ln(f(0))}\cdot\frac{\ln(f(0))}{\ln(f(x))} = \overline{r}(x) + R_0 \overline{\phi}(x)$$

which implies that

$$\overline{r}(x) = \overline{\gamma}(x) - R_0 \overline{\phi}(x)$$

Therefore, extracting any $R_n$ requires only applying the coefficient extraction operator to all EGFs, so

$$\left[\frac{x^n}{n!}\right]\overline{r}(x) = \left[\frac{x^n}{n!}\right]\overline{\gamma}(x) - R_0 \left[\frac{x^n}{n!}\right]\overline{\phi}(x)$$

Which automatically leads to 

$$R_n = \Gamma_n - R_0 \Phi_n$$

### Movin' on up

Another benefit of proving this particular corollary in 1-D is that extending it to a multidimensional framework is surprisingly easy. Because the F/G-sector decomposition operates solely on continuous analytic functions, the underlying algebraic relationship between the sectors does not change when adding more variables.

It's time to give our ODE log ratio identity an upgrade.

We'll start formally establishing the multivariate equivalents of our EGFs and the multi-index extraction operator by upgrding our scalar variables to **vectors** and our scalar indices to **multi-indices**.

Let $X = (x_1, x_2, \dots, x_d)$ represent our $d$-dimensional spatial vector, and $\alpha = (\alpha_1, \alpha_2, \dots, \alpha_d)$ represent our multi-index.

Now we standardize multi-index power and factorial notations

$${X}^\alpha = x_1^{\alpha_1} x_2^{\alpha_2} \cdots x_d^{\alpha_d} \quad \text{and} \quad \alpha! = \alpha_1! \alpha_2! \cdots \alpha_d!$$

and then explicitly define the multivariate EGFs. Note how they mirror the 1-D forms.

$$\overline{\gamma}(X) = \sum_{\alpha \ge 0} \Gamma_\alpha \frac{X^\alpha}{\alpha!} \quad \text{,} \quad \overline{\phi}(X) = \sum_{\alpha \ge 0} \Phi_\alpha \frac{X^\alpha}{\alpha!} \quad \text{and} \quad \overline{r}(X) = \sum_{\alpha \ge 0} R_\alpha \frac{X^\alpha}{\alpha!}$$

Here, the summation $\alpha \ge 0$ implies a multiple sum over all non-negative integers for every dimension in the multi-index.

Now we get to apply a big axiomatic shortcut; the continuous algebraic relationships we just established in 1-D are **dimensionally invariant**.

The evaluation of the integrals in the multidimensional space we just established relies on precisely the same properties of logarithms and Maclaurin series, so the closed forms remain structurally identical:

$$\overline{\gamma}(X) = \frac{\ln(g(X))}{\ln(f(X))} - \frac{\ln(g(\mathbf{0}))}{\ln(f(X))}$$

$$\overline{\phi}(X) = - \frac{\ln(f(\mathbf{0}))}{\ln(f(X))}$$

Because the identity remains the same regardless of how many variables $X$ has,

$$\overline{\gamma}(X) = \overline{r}(X) + R_0 \overline{\phi}(X)$$

Similarly the **multivariate coefficient extraction operator** can now be used in place of its 1-D counterpart. Since $\frac{X^\alpha}{\alpha!}$ forms the orthogonal basis for the multi-variable Maclaurin series, the operator distributes across the linear sum:

$$\left[\frac{X^\alpha}{\alpha!}\right]\overline{r}(X) = \left[\frac{X^\alpha}{\alpha!}\right]\overline{\gamma}(X) - R_\emptyset \left[\frac{X^\alpha}{\alpha!}\right]\overline{\phi}(X)$$

Because every multi-index term is independent of the others, we can safely slide our coefficient extractor straight through the plus and minus signs without worrying about cross-contamination from other derivative orders, which, by definition, yields our target corollary:

$$R_\alpha = \Gamma_\alpha - R_\emptyset \Phi_\alpha$$

## One (Multidimensional) Ring to Rule Them All

Yet another reason to have closed our new $\Gamma_n$ and $\Phi_n$ recursions in one dimension is that it helps us discover that the $P(A_n)$ generator (and by extension the $P(A_\alpha)$ generator as well) acts as a pure **differential ring**.

This pattern displayed itself early on in my multivariate work, so it's not something I initially saw purely axiomatically.

### More Pattern-Finding

Recall from our 2-D work that

$$R_{(1,1)} = \left[ {G^{(x)}}_{(0,1)} - F^{(x)}G^{(y)} \right] - R_\emptyset \left[ {F^{(x)}}_{(0,1)} - F^{(x)}F^{(y)} \right]$$

To get to $R_{(2,1)}$ we differentiate with respect to $x$:

$$R_{(2,1)} = \frac{\partial}{\partial x} R_{(1,1)} = \frac{\partial}{\partial x} (\Gamma_{(1,1)} - \Phi_{(1,1)}R) = \frac{\partial}{\partial x}\Gamma_{(1,1)} - \left( \frac{\partial}{\partial x}\Phi_{(1,1)} \right)R - \Phi_{(1,1)} R_{(1,0)}$$

Then substitute $R_{(1,0)} = G^{(x)} - F^{(x)}R$:

$$R_{(2,1)} = \frac{\partial}{\partial x}\Gamma_{(1,1)} - \left( \frac{\partial}{\partial x}\Phi_{(1,1)} \right)R - \Phi_{(1,1)} (G^{(x)} - F^{(x)}R)$$

which gave the result:

$$R_{(2,1)} = \left[ \frac{\partial}{\partial x}\Gamma_{(1,1)} - \Phi_{(1,1)}G^{(x)} \right] - R \left[ \frac{\partial}{\partial x}\Phi_{(1,1)} - \Phi_{(1,1)}F^{(x)} \right]$$

Similarly, to get to $R_{(1,2)}$,

$$ \frac{\partial}{\partial y} R_{(1,1)} = R_{(1,2)} = \left[ \frac{\partial}{\partial y}\Gamma_{(1,1)} - \Phi_{(1,1)}G^{(y)} \right] - R \left[ \frac{\partial}{\partial y}\Phi_{(1,1)} - \Phi_{(1,1)}F^{(y)} \right]$$

Note that removing the $(x)$ and $(y)$ superscripts from $F$ and $G$ while reverting partials to $\frac{d}{dx}$ and summing the $\Gamma$ and $\Phi$ subscripts cause both $R_{(2,1)}$ and $R_{(1,2)}$ to collapse to $R_3$.

This observation leads us to believe that 

$$\Gamma_{\alpha} = \frac{\partial}{\partial w}\Gamma_{\alpha - e_w} - \Phi_{\alpha - e_w} G^{(w)}$$

and

$$\Phi_{\alpha} = \frac{\partial}{\partial w}\Phi_{\alpha - e_w} - \Phi_{\alpha - e_w} F^{(w)}$$

and therefore 

$$\Gamma_{n} = \frac{d}{dx}\Gamma_{n - 1} - \Phi_{n-1} G$$

and

$$\Phi_{n} = \frac{d}{dx}\Phi_{n - 1} - \Phi_{n - 1} F$$

But can we prove it axiomatically?

### The Proof of the Pudding

Let's have another little taste of our 1-D closure paired with these new observations (metaphorically and literally) to see if the algebraic pudding was worth the calories.

We start by letting $y(x) = \overline{\phi}(x)$. Earlier, we proved that this EGF is governed by the ODE:

$$y'(x) = -\overline{f}(x)y(x)$$

We initiate the base case $\Phi_0 = -1$ under the hypothesis that it governs the drag associated with taking the derivative of a variable base:

$$y^{(n)}(x) = - \Phi_n(x) y(x)$$

Notice this holds for $n=0$: $y^{(0)} = -(-1)y = y$

To find the $(n)$-th state, we can take the formal derivative of the $(n-1)$-th state:

$$y^{(n)}(x) = \frac{d}{dx} \left[ y^{(n-1)}(x) \right] = \frac{d}{dx} \left[ - \Phi_{n-1}(x) y(x) \right]$$

and then apply the product rule to obtain

$$y^{(n)}(x) = - \Phi_{n-1}'(x) y(x) - \Phi_{n-1}(x) y'(x)$$

Substituting $y'(x) = -\overline{f}(x)y(x)$ into the right side and factoring out the common $-y(x)$ term gives us

$$y^{(n)}(x) = - \Big[ \Phi_{n-1}'(x) - \Phi_{n-1}(x)\overline{f}(x) \Big] y(x)$$

By directly comparing this to our structural hypothesis $y^{(n)}(x) = - \Phi_n(x) y(x)$, we extract the algebraic term for $\Phi_n$:

$$\Phi_n(x) = \Phi_{n-1}'(x) - \Phi_{n-1}(x)\overline{f}(x)$$

Now we evaluate as a discrete combinatorial operator at the origin (dropping the $x$ notation and returning to $F_0$) which yields our target $\Phi_n$ shift axiom:

$$\Phi_n = \frac{d}{dx}\Phi_{n-1} - \Phi_{n-1} F_0$$

Performing the parallel process for $\Gamma_n$ also yields its corresponding target axiom.

Let $z(x) = \overline{\gamma}(x)$. We proved this EGF is governed by the non-homogeneous ODE:

$$z'(x) = \overline{g}(x) - \overline{f}(x)z(x)$$

We establish the structural hypothesis for the $n$-th derivative. Knowing that $\Gamma_n$ is the non-homogeneous forcing component and $\Phi_n$ handles the homogeneous $z(x)$ decay, we hypothesize:

$$z^{(n)}(x) = \Gamma_n(x) - \Phi_n(x) z(x)$$

(Notice this holds for $n=0$: $z^{(0)} = 0 - (-1)z = z$)

We repeat the inductive process by taking the derivative of the $(n-1)$-th state:

$$z^{(n)}(x) = \frac{d}{dx} \left[ \Gamma_{n-1}(x) - \Phi_{n-1}(x) z(x) \right]$$

and applying the product rule:

$$z^{(n)}(x) = \Gamma_{n-1}'(x) - \Phi_{n-1}'(x) z(x) - \Phi_{n-1}(x) z'(x)$$

Substitute the continuous ODE, $z'(x) = \overline{g}(x) - \overline{f}(x)z(x)$, into the equation:

$$z^{(n)}(x) = \Gamma_{n-1}'(x) - \Phi_{n-1}'(x) z(x) - \Phi_{n-1}(x) \big( \overline{g}(x) - \overline{f}(x)z(x) \big)$$

Distribute and group the non-homogeneous terms (those without $z$) and the homogeneous terms (those with $z$):

$$z^{(n)}(x) = \Big[ \Gamma_{n-1}'(x) - \Phi_{n-1}(x)\overline{g}(x) \Big] - \Big[ \Phi_{n-1}'(x) - \Phi_{n-1}(x)\overline{f}(x) \Big] z(x)$$

From our first proof, we already know the second bracket is exactly $\Phi_n(x)$. Therefore:

$$z^{(n)}(x) = \Big[ \Gamma_{n-1}'(x) - \Phi_{n-1}(x)\overline{g}(x) \Big] - \Phi_n(x) z(x)$$

Matching this against our structural hypothesis $z^{(n)}(x) = \Gamma_n(x) - \Phi_n(x) z(x)$, the $\Gamma$ term extracts perfectly:

$$\Gamma_n(x) = \Gamma_{n-1}'(x) - \Phi_{n-1}(x)\overline{g}(x)$$

Evaluated at the origin, it yields the exact $\Gamma$ shift axiom:

$$\Gamma_n = \frac{d}{dx}\Gamma_{n-1} - \Phi_{n-1} G_0$$

Because this proof relies exclusively on the General Leibniz rule and substitution of first-order ODEs, it scales directly to multi-index calculus by replacing the total derivative $\frac{d}{dx}$ with the partial derivative across the multi-index step $\frac{\partial}{\partial w}$ , and swapping the 1-D states $F_0$ / $G_0$ for the directional bases $F^{(w)}$ / $G^{(w)}$:

$$\Phi_{\alpha} = \frac{\partial}{\partial w}\Phi_{\alpha - e_w} - \Phi_{\alpha - e_w} F^{(w)}$$

$$\Gamma_{\alpha} = \frac{\partial}{\partial w}\Gamma_{\alpha - e_w} - \Phi_{\alpha - e_w} G^{(w)}$$

Since all $\Gamma_\alpha$ and $\Phi_\alpha$ can be constructed from their lower orders based on this single set of differential operators, the Log-Tower engine is now a proven, perfect **differential ring**.

## What Goes up Must Come Down

We've been doing a lot of work on differentiating, starting on the bottom rungs of the differential order and clambering our way upward, but the only place integrals have popped up so far is when we're closing mathematical forms. 

No worries, integration-hawks. That's about to change right now.

### Égalité!

You may have noticed that we now have two equivalent multivariate operators that produce $\Gamma_\alpha$, one standard recursion and one derivative shift operator.

So, let's put them across from each other on either side of an equals sign. To help shorten the equations a bit, let's set $\alpha - e_w = \gamma$:

$$\frac{\partial}{\partial w} \Gamma_\gamma - \Phi_\gamma G^{(w)} = D^\gamma G^{(w)} - \sum_{0 \le \beta \le \gamma} \binom{\gamma}{\beta} (D^{\gamma - \beta} F^{(w)}) \Gamma_\beta$$

For the sake of upcoming comparison, let's also pull the top term out of the summation.

$$\frac{\partial}{\partial w} \Gamma_\gamma = D^\gamma G^{(w)} + \Phi_\gamma G^{(w)} - F^{(w)}\Gamma_\gamma - \sum_{0 \le \beta < \gamma} \binom{\gamma}{\beta} (D^{\gamma - \beta} F^{(w)}) \Gamma_\beta$$

Rearranging the $\Phi$ term to the RHS proves that the derivative of a $\Gamma$ term is a closed algebraic loop. To find $\frac{\partial}{\partial w} \Gamma_\gamma$, one does not need to apply symbolic differentiation to a massive polynomial; we just need to call the cached values for $\Gamma_\gamma$ and $\Phi_\gamma$, add the derivative of $G$, and run a truncated sum of the lower tower.

Doing the same thing for the $\Phi_\alpha$ operators produces

$$\frac{\partial}{\partial w} \Phi_\gamma - \Phi_\gamma F^{(w)} = - \sum_{0 \le \beta \le \gamma} \binom{\gamma}{\beta} (D^{\gamma - \beta} F^{(w)}) \Phi_\beta$$

Once again, moving the $\Phi_\gamma F^{(w)}$ term to the RHS displays the same truth as we just discovered with $\Gamma_\alpha$. This time, though, due to the homogeneity of $\Phi_\alpha$, this term is identical to the top term of the sum, so it cancels, leaving us with a telling identity of

$$\frac{\partial}{\partial w} \Phi_\gamma = - \sum_{0 \le \beta < \gamma} \binom{\gamma}{\beta} (D^{\gamma - \beta} F^{(w)}) \Phi_\beta$$

This equation in no uncertain terms tells us that _every derivative of_ $\Phi\_\gamma$ _is the multi-index binomial convolution between the partial derivatives of_ $-F^{(w)}$ _and its own corresponding lower-order states_.

### Fraternité

If we can take derivatives in the ring to climb the order ladder, we should be able to integrate to step back, so let's see what happens when we subject these siblings, $\Phi_\gamma$ and $\Gamma_\gamma$, to **Volterra integration**.

Volterra integration involves integrating when unknown functions comprise some or all of the integrand. In this case, we're using **linear Volterra equations of the first kind** to assemble polynomials made of unknown differentiable functions.

This kind of Volterra integration is of the form

$$g(x) = \int_{a}^{x} K(x, t) f(t) dt$$

where

- $g(x)$ is a given function,
- $K(x, t)$ is the kernel of the integral equation, and
- $f(t)$ is the unknown function to be determined.

Let's start with the above equation regarding $\Phi_\gamma$, using $w$ for the dummy integration variable $\tau$, and integrate both sides from $0$ to $w$.

$$\int_0^w \frac{\partial}{\partial \tau} \Phi_\gamma(\dots \tau \dots) d\tau = - \int_0^w \sum_{0 \le \beta < \gamma} \binom{\gamma}{\beta} \left( D^{\gamma - \beta} F^{(\tau)} \right) \Phi_\beta(\dots \tau \dots) d\tau$$

The LHS resolves into $\Phi_\gamma$ evaluated from 0 to $w$ giving us our explicit integral generator on the RHS:

$$\Phi_\gamma \Big|_{0}^{w} = - \sum_{0 \le \beta < \gamma} \binom{\gamma}{\beta} \int_0^w \left( D^{\gamma - \beta} F^{(\tau)} \right) \Phi_\beta(\tau) d\tau$$

Let's watch this alternative polynomial generator in action by running the first two levels through it.

Let $\gamma = e_w$, or a vector with a 1 in the $w$ position and 0s elsewhere.

Because our summation strictly requires $\beta < e_w$, the only valid multi-index for $\beta$ is the zero vector, $\vec{0}$.

Let's plug $\beta = \vec{0}$ and the baseline $\Phi_{\vec{0}} = -1$ into the integral:

$$\Phi_{e_w}(w) - \Phi_{e_w}(0) = - \int_0^w \binom{e_w}{\vec{0}} \left( D^{e_w} F^{(\tau)} \right) (-1)  d\tau$$

The negative signs cancel. Since $D^{e_w}$ with respect to $\tau$ is simply the first partial derivative $\frac{\partial}{\partial \tau}$, the equation simplifies to:

$$\Phi_{e_w}(w) - \Phi_{e_w}(0) = \int_0^w \frac{\partial}{\partial \tau} F^{(\tau)}  d\tau$$

So integrating a direct derivative gives us the function back as expected:

$$\Phi_{e_w}(w) - \Phi_{e_w}(0) = F^{(w)} \Big|_{0}^{w}$$

Since the first order works, let's push it one step further to see if the integral generates the correct higher-order polynomial.

Let $\gamma = 2e_w$ this time.

The summation now steps through $\beta = \vec{0}$ and $\beta = e_w$.

$$\Phi_{2e_w} \Big|_{0}^{w} = - \int_0^w \left[ \binom{2}{0} \left( D^{2e_w} F^{(\tau)} \right) \Phi_{\vec{0}} + \binom{2}{1} \left( D^{e_w} F^{(\tau)} \right) \Phi_{e_w} \right] d\tau$$

Now we substitute our base case $\Phi_{\vec{0}} = -1$ and our newly integrated $\Phi_{e_w} = F^{(\tau)}$:

$$\Phi_{2e_w} \Big|_{0}^{w} = - \int_0^w \left[ - \frac{\partial^2}{\partial \tau^2} F^{(\tau)} + 2 \left( \frac{\partial}{\partial \tau} F^{(\tau)} \right) F^{(\tau)} \right] d\tau$$

Let's move the negative sign into the integral. Notice what happens to the terms inside:

$$= \int_0^w \left[ \frac{\partial^2}{\partial \tau^2} F^{(\tau)} - 2 F^{(\tau)} \left( \frac{\partial}{\partial \tau} F^{(\tau)} \right) \right] d\tau$$

So the integral of the second derivative is the first derivative as expected. 

Using the reverse chain rule, the integral of $-2 F^{(\tau)} \frac{\partial}{\partial \tau} F^{(\tau)}$ is $-(F^{(\tau)})^2$, so

$$\Phi_{2e_w}(w) - \Phi_{2e_w}(0) = \left[ F^{(w)}_{(1,0)} - (F^{(w)})^2 \right] \Bigg|_{0}^{w}$$

which shows that $\Phi_{2e_w} = F^{(w)}_{(1,0)} - (F^{(w)})^2$. From our 1-D work $\Phi_2 = F_1 - F^2$, so we've been here before.

Needless to say, the same thing happens when we subject the corresponding $\Gamma_\gamma$ equation to the same treatment.

To save some space, let's skip straight to $\Gamma_{2e_w}$

$$\Gamma_{2e_w} \Big|_{0}^{w} = \int_0^w \left[ D^{2e_w} G^{(\tau)} + \Phi_{2e_w}(\tau) G^{(\tau)} - F^{(\tau)}\Gamma_{2e_w}(\tau) - \sum_{0 \le \beta < 2e_w} \binom{2}{\beta} \left( D^{2e_w - \beta} F^{(\tau)} \right) \Gamma_\beta(\tau) \right] d\tau$$

Let's plug our known values into each of these four blocks:

$$D^{2e_w} G^{(\tau)} = G^{(\tau)}_2$$

We've already proved $\Phi_{2e_w} = F^{(\tau)}\_1 - (F^{(\tau)})^2$. Multiplying by $G^{(\tau)}$ gives: $F^{(\tau)}\_1 G^{(\tau)} - (F^{(\tau)})^2 G^{(\tau)}$

Multiplying $\Gamma_{2e_w}$ by $-F^{(\tau)}$ gives: $-F^{(\tau)} G^{(\tau)}\_1 + (F^{(\tau)})^2 G^{(\tau)}$

The index, $\beta$, steps through $\vec{0}$ and $e_w$. Since $\Gamma_{\vec{0}} = 0$ and $\Gamma_{e_w} = G^{(\tau)}$, the sum expands to:

$$- \left[ 1 \cdot F^{(\tau)}_2 (0) + 2 \cdot F^{(\tau)}_1 (G^{(\tau)}) \right] = -2 F^{(\tau)}_1 G^{(\tau)}$$

Now, let's place all of those expanded blocks back inside the integral:

$$= \int_0^w \left[ G^{(\tau)}_2 + F^{(\tau)}_1 G^{(\tau)} - (F^{(\tau)})^2 G^{(\tau)} - F^{(\tau)} G^{(\tau)}_1 + (F^{(\tau)})^2 G^{(\tau)} - 2 F^{(\tau)}_1 G^{(\tau)} \right] d\tau$$

The cubed-complexity terms cancel: $-(F^{(\tau)})^2 G^{(\tau)}$ and $+(F^{(\tau)})^2 G^{(\tau)}$

and we are left with:

$$= \int_0^w \left[ G^{(\tau)}_2 + F^{(\tau)}_1 G^{(\tau)} - F^{(\tau)} G^{(\tau)}_1 - 2 F^{(\tau)}_1 G^{(\tau)} \right] d\tau$$

Combine the remaining $F_1 G$ terms ($1 - 2 = -1$):

$$= \int_0^w \left[ G^{(\tau)}_2 - F^{(\tau)}_1 G^{(\tau)} - F^{(\tau)} G^{(\tau)}_1 \right] d\tau$$

If we group the last two terms:

$$= \int_0^w \bigg( \left[ G^{(\tau)}_2 \right] - \left[ F^{(\tau)}_1 G^{(\tau)} + F^{(\tau)} G^{(\tau)}_1 \right] \bigg)  d\tau$$

We see that the integral of $G^{(\tau)}\_2$ is $G^{(\tau)}\_1$.

The block $\left[ F^{(\tau)}_1 G^{(\tau)} + F^{(\tau)} G^{(\tau)}_1 \right]$ is the expansion of the product rule for $\frac{\partial}{\partial \tau} \left( F^{(\tau)} G^{(\tau)} \right)$.

Collapsing the integral via the reverse product rule leaves us with:

$$\Gamma_{2e_w}(w) - \Gamma_{2e_w}(0) = \left[ G^{(\tau)}_1 - F^{(\tau)} G^{(\tau)} \right] \Bigg|_{0}^{w}$$

Therefore,

$$\Gamma_{2e_w} = G^{(w)}_1 - F^{(w)} G^{(w)}$$

So, the $\Phi$ and $\Gamma$ sectors appear together as counterweights. The polynomial $(F^{(\tau)})^2 G^{(\tau)}$ generated by the $\Phi$ cache exists to cancel the overlapping terms generated by the $\Gamma$ cache.

### Liberté

Now we are free to use integration methods to develop polynomials within the ring. At some point I hope to write a section on how substituting in the multidimensional derivative shift operators turns these integrals into an integration by parts shearing machine, utilizing **linear Volterra equations of the second kind**

$$f(x) = g(x) + \lambda \int_{a}^{x} K(x, t) f(t) dt$$

Where

- $f(x)$ is the unknown function,
- $g(x)$ is a given function (often representing the "source" or "initial" state),
- $\lambda$ is a scalar parameter, and
- $K(x, t)$ is the kernel,

but this section is already too long, so I'll leave you with one last thought.

We have discovered two equations that represent $\Phi_\gamma$:

$$\Phi_\gamma = - \sum_{0 \le \beta \le \gamma - e_w} \binom{\gamma - e_w}{\beta} (D^{\gamma - e_w - \beta} F^{(w)}) \Phi_\beta$$

$$\Phi_\gamma = - \sum_{0 \le \beta < \gamma} \binom{\gamma}{\beta} \int_0^w \left( D^{\gamma - \beta} F^{(\tau)} \right) \Phi_\beta(\tau) d\tau$$

Let's set them equal and drop the negative sign on each side

$$\sum_{0 \le \beta \le \gamma - e_w} \binom{\gamma - e_w}{\beta} (D^{\gamma - e_w - \beta} F^{(w)}) \Phi_\beta = \sum_{0 \le \beta < \gamma} \binom{\gamma}{\beta} \int_0^w \left( D^{\gamma - \beta} F^{(\tau)} \right) \Phi_\beta(\tau) d\tau$$

and then do the same for $\Gamma_\gamma$

$$D^{\gamma - e_w} G^{(w)} - \sum_{0 \le \beta \le \gamma - e_w} \binom{\gamma - e_w}{\beta} (D^{\gamma - e_w - \beta} F^{(w)}) \Gamma_\beta = \int_0^w \left[ D^\gamma G^{(\tau)} + \Phi_\gamma(\tau) G^{(\tau)} - \sum_{0 \le \beta \le \gamma} \binom{\gamma}{\beta} \left( D^{\gamma - \beta} F^{(\tau)} \right) \Gamma_\beta(\tau) \right] d\tau$$

which shows that dropping a discrete tensor index is mathematically equivalent to integrating across that dimension's continuous path, meaning we're looking at a **proven multidimensional continuous space**.

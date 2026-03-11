# Part 8: ...and the Omega

You may have noticed that most talk of $\Omega_\beta^\alpha$ was conspicuously absent in the last part. The information below was initially slated for inclusion in Part 7 as you likely see from the title here being a continuation of the last.

The prior part got too long, in particular because of the inclusion of our coverage of Volterra integrals at the end to prove the $\Gamma / \Phi$ differential ring is a continuous multidimensional space, so our concluding work on the formalization of $\Omega_\beta^\alpha$ will be included here instead.

It's time to wrap up our multidimensional expansion, so let's get to it.

## $\Omega$ Gets a Promotion

Recall that our 1-D version of the $\Omega_m^n$ recursion is given by

$$\Omega_m^n = - \sum_{j=0}^{m-1} \binom{n-1}{j} F_j \Omega_{m-1-j}^{n-1-j}$$

Hmm. We know there was an indexing problem with our 1-D work, but it doesn't immediately jump out here. Where might it be?

Recall our 1-D equation for $\Gamma_n$:

$$\Gamma_{n} = \sum_{m=0}^{n}G_{n-m}\Omega_m^{n+1}$$

Aha. That's where the indexing problem was. $\Gamma$ needs to be indexed back by one on the right. Let's fix that.

$$\Gamma_{n} = \sum_{m=0}^{n-1}G_{n-m-1}\Omega_m^n$$

Note how the equation still only calls $\Omega_m^n$, so the $\Omega$ recursion doesn't need to be changed at all. Since the caching algorithm exists independently of $\Gamma$ and $\Phi$ indexing, it's already sitting pretty.

Although we never explicitly created the formula for $\Phi_n$ before, instead relying on $G \mapsto F$ to create it, let's go ahead and put it here.

$$\Phi_{n} = \sum_{m=0}^{n-1}F_{n-m-1}\Omega_m^n$$

It's finally time to promote $\Omega_m^n$ to multivariate status and take it for a test drive.

### $\Omega$ Transformation

$$\Omega^n_m = - \sum_{j=0}^{m-1} \binom{n-1}{j} F_j \Omega^{n-1-j}_{m-1-j}$$

$$\downarrow \downarrow \downarrow \downarrow$$

$$\Omega^\alpha_\beta = - \sum_{0 \leq \gamma \leq \beta - e_w} \binom{\alpha-e_w}{\gamma} F^{(w)}\_\gamma \Omega^{\alpha - e_w - \gamma}_{\beta - e_w - \gamma}$$

Huh. Seems like we just replaced the Roman lettering with Greek, added a superscript for labelling all $F$ modules in a partial derivative framework, and substituted in a tensor subtraction where we used to have a $-1$.

Are we allowed to do that? Is going multidimensional with Omega just that easy?

The answers are, in order, "yes and no." Let's find out why.

## Is Failure an Option?

The next logical step after promoting $\Omega^\alpha_\beta$ seemed inevitable. Plugging the multidimensional analog for $\Omega$ into a multidimensional version of our 1-D convolution to generate $\Gamma_\alpha$ and $\Phi_\alpha$ made complete sense and would be a snap to code.

Unfortunately, the transition from a single-variable integer line to a multidimensional tensor grid has a brutal mathematical barrier to breach known as **path dependency**.

Come take a morbid tour of the graveyard of diabolical experiments in computing $\Gamma_\alpha$ and $\Phi_\alpha$ via direct $\Omega^\alpha_\beta$ convolutions, and watch in horror as each seemingly viable method meets its grisly demise.

### Victim 1: The Naive Multi-Index Substitution

Our corrected 1-D convolution updated to include multi-indices seemed natural to try after all our other multidimensional work. If $\Gamma_{n} = \sum_{m=0}^{n-1}G_{n-m-1}\Omega_m^n$, then the tensor equivalent may have just required choosing a dimension $w$ and shifting backward by its standard basis vector $e_w$.

So, we start with:

$$\Gamma_\alpha = \sum_{0 \leq \beta \leq \alpha - e_w} G^{(w)}\_{\alpha - \beta - e_w} \Omega^\alpha_\beta$$

The first step went really well. Let’s look at a first-order pure derivative, setting $\alpha = (1, 0)$ and stepping back along the $x$-axis so $w=1$ and $e_1 = (1, 0)$.

The bounds of our sum become $0 \leq \beta \leq (0, 0)$, leaving us with exactly one term:

$$\Gamma_{(1,0)} = G^{(x)}\_{(0,0)} \Omega^{(1,0)}_{(0,0)}$$

The result is promising, right? It's the proper multidimensional analog to our 1-D baseline $\Gamma_1 = G_0 \Omega_0^1$. It was clean, elegant, and mapped correctly.

Then came the test on a mixed second derivative, and the brutal reality of path dependence reared its terrifying head.

Let's evaluate $\alpha = (1, 1)$. Because this is a mixed derivative, our formula forces us to make a choice: do we step backward along the $x$-axis ($e_1$) or the $y$-axis ($e_2$)? In a true invariant tensor field, this choice shouldn't matter.

Let's test Path 1 (stepping back along $x$):

$$\Gamma_{(1,1)} \big|\_{x\text{-path}} = G^{(x)}\_{(0,1)} \Omega^{(1,1)}_{(0,0)} + G^{(x)}_{(0,0)} \Omega^{(1,1)}_{(0,1)}$$

Now, let's test Path 2 (stepping back along $y$):

$$\Gamma_{(1,1)} \big|\_{y\text{-path}} = G^{(y)}\_{(1,0)} \Omega^{(1,1)}\_{(0,0)} + G^{(y)}\_{(0,0)} \Omega^{(1,1)}_{(1,0)}$$

Assuming standard continuous mixed partials (Clairaut's theorem), the first terms match perfectly since $G^{(x)}\_{(0,1)} = G^{(y)}\_{(1,0)}$. But look at the second terms. We are left with $G^{(x)}\_{(0,0)} \Omega^{(1,1)}\_{(0,1)}$ versus $G^{(y)}\_{(0,0)} \Omega^{(1,1)}_{(1,0)}$.

While the $G$ coefficients simply represent $G^{(x)}$ and $G^{(y)}$, the $\Omega$ terms are different. Because the multidimensional $\Omega^\alpha_\beta$ recursively absorbs $F$-sector derivatives, $\Omega^{(1,1)}\_{(0,1)}$ and $\Omega^{(1,1)}_{(1,0)}$ evaluate to vastly different polynomials.

By forcing a choice of $w$, the convolution algorithm inherently privileges one coordinate axis over the other, destroying the symmetry required for a valid tensor. This wasn't a universal generator; it was a directional artifact.

### Victim 2: The Symmetrized Average with the Naive Multi-Index Substitution

If choosing a single path $w$ breaks the symmetry, then maybe we need to try averaging over all possible paths. If we sum the convolutions across all valid dimensional paths and divided by the number of paths, the directional biases could cancel out, leaving us with the true invariant $\Gamma_\alpha$.

Let $P(\alpha)$ be the set of valid dimensions $w$ where we can step backward (i.e., $\alpha_w > 0$), and $|P(\alpha)|$ be the number of those paths.

$$\Gamma_\alpha = \frac{1}{|P(\alpha)|} \sum_{w \in P(\alpha)} \left( \sum_{0 \leq \beta \leq \alpha - e_w} G^{(w)}\_{\alpha - \beta - e_w} \text{ } \Omega^\alpha_\beta \right)$$

After the gruesome fate that befell Victim 1, applying this to the mixed second derivative $\alpha = (1,1)$ seemed much more promising.

If we take the two diverging paths, sum them, and divide by $2$:

$$\Gamma_{(1,1)} = \frac{1}{2} \left( \Gamma_{(1,1)} \big|\_{x\text{-path}} + \Gamma_{(1,1)} \big|_{y\text{-path}} \right)$$

When expanding the $\Omega^{(1,1)}$ terms, the asymmetrical parts counterbalanced. The fractions combined into whole integers, and the resulting polynomial matched the $F/G$-sector decomposition expected for a mixed second derivative. It was symmetric, it was elegant, and it worked.

At least it worked *so far*.

Then came the third derivative, $\alpha = (2,1)$, and, well...

For $\alpha = (2,1)$, we again have two valid directions to step back: along $x$ (since $\alpha_1 = 2$) or along $y$ (since $\alpha_2 = 1$).

Path $x$ draws upon terms like $G^{(x)}\_{(1,1)} \Omega^{(2,1)}\_{(0,0)}$ and $G^{(x)}\_{(0,0)} \Omega^{(2,1)}\_{(1,1)}$ while path $y$ uses terms like $G^{(y)}\_{(2,0)} \Omega^{(2,1)}\_{(0,0)}$ and $G^{(y)}\_{(0,0)} \Omega^{(2,1)}_{(2,0)}$.

When averaging the paths, it wasn't utterly unreasonable to hope the cross-terms would elegantly fold together just as they did for $(1,1)$. But because the combinatorial depth of $\Omega^{(2,1)}\_{(1,1)}$ is different from $\Omega^{(2,1)}_{(2,0)}$, the recursion generated completely different sub-component sets.

Instead of whole numbers, the matrix was suddenly littered with unresolvable phantom fractions like $\frac{1}{2} F_{(1,0)} G_{(0,1)}$. The real matrix could only have integer coefficients dictated by Bell polynomial structures and generating functions. Our formula had generated a perfectly symmetric but nakedly fictional tensor.

### Victim 3: Strict Lexicographical Forcing with Naive Multi-Index Substitution

Since elegance didn't seem to work, it was time to try brute force. Forcing the naive multi-index substitution of our linear convolution algorithm to evaluate indices in a strict lexicographical order, for example, always stepping backward along the highest available dimension $w_{max}$ where $\alpha_w > 0$, could reasonably have fit the bill.

The convolution executed as:

$$\Gamma_\alpha = \sum_{0 \leq \beta \leq \alpha - e_{w_{max}}} G^{(w_{max})}\_{\alpha - \beta - e_{w_{max}}} \Omega^\alpha_\beta$$

At a strictly computational level, this chugged along like a dream. Because there was only ever one legal path to traverse, there were no divergent cross-terms to reconcile. Testing on dense higher-order derivatives like $\alpha = (1, 1, 1)$ and $\alpha = (2, 2)$ gave consistent, repeatable polynomials with integer coefficients. No phantom fractions, no ambiguity. Had we brute-forced our way past the tensor grid's defenses?

Yeah, no. We hadn't. While we had bypassed path dependency, the underlying geometry was in tatters.

Forcing a specific path (say, always exhausting $z$-derivatives, then $y$, then $x$) stripped the resulting $\Gamma_\alpha$ of its coordinate independence. Swapping $x$ and $y$ indices provided an entirely different polynomial. The matrix was just an artifact of whatever alphabet we arbitrarily chose.

Worse still, this method completely shattered the continuous multidimensional space we just spent Part 7 proving existed for this n-dimensional algebraic fractal expression. The Volterra integral equations that establish the continuity of the $\Gamma / \Phi$ differential ring rely on **isotropic geometry** (i.e., no single dimension can hold a privileged position in the integration limits). Yet the lexicographical algorithm inherently weighted the "first" chosen dimension differently than the "last" when used in the context of our linear convolution. Forcing an artificial hierarchy onto a continuous space shredded its algebraic fabric.

Path dependency loomed ever more horrifyingly large as a foe. Convolutions just couldn't carry $\Omega^\alpha_\beta$ to $\Gamma_\alpha$ and $\Phi_\alpha$ without breaking the underlying tensor geometry.

### Victim 4: The Rank 2 Tensor Framework within Naive Multi-Index Substitution

Since using scalars kept leading to disaster, the next logical upgrade would be to a mechanism that had natural path-routing capabilities -- matrices. **Rank 2 tensors** and vectors might have held the key to zeroing out the main diagonal and cross-wiring the off-diagonal elements with our $-F$ modules.

The first test on the mixed second derivative $\Gamma_{(1,1)}$ went really well. Both rows of the output vector evaluated to the exact same multidimensional surface, bypassing the commutative roadblocks that murdered Victims 1, 2, and 3. 

Then came $\Gamma_{(2,1)}$, and the engine ground to yet another sputtering halt. The newly minted tensor output compared to that of our established derivative shift operator, $\Gamma_{\alpha} = \frac{\partial}{\partial w}\Gamma_{\alpha - e_w} - \Phi_{\alpha - e_w} G^{(w)}$ held glaring errors.

_Shift operator output along x-path:_

$$\Gamma_{(2,1)} = G^{(x)}\_{(1,1)} - F^{(x)}\_{(0,1)} G^{(x)} - F^{(x)}\_{(1,0)} G^{(y)} - F^{(x)} G^{(x)}_{(0,1)} + (F^{(x)})^2 G^{(y)}$$

_Rank 2 tensor output:_

$$[\vec{\mathbf{\Gamma}}_{(2,1)}]^x = G^{(x)}\_{(1,1)} - F^{(x)}\_{(1,0)} G^{(y)}\_{(0,1)} - F^{(x)}\_{(0,1)} G^{(x)}\_{(1,0)} - F^{(x)}\_{(1,1)} G^{(x)} + F^{(x)} F^{(x)}\_{(0,1)} G^{(x)} + F^{(x)}_{(1,0)} F^{(y)} G^{(y)}$$

Not even close. The continuous operator correctly paired first-order $F$ derivatives with base $G$ modules (e.g., $- F^{(x)}\_{(1,0)} G^{(y)}$), while the tensor operator paired base $F$ modules with first-order $G$ derivatives backwards (e.g., $- F^{(x)}\_{(1,0)} G^{(y)}\_{(0,1)}$). Worse, the tensor spawned a second-order $F$ derivative ($- F^{(x)}_{(1,1)} G^{(x)}$) that didn't exist in the correct continuous expansion, meaning we had an **index assignment** mismatch.

In one dimension, we can use $\Gamma_n = \sum G_{n-m-1} \Omega^n_m$ since the "remaining" derivatives ($n-m-1$) are explicitly assigned to the $G$ module. Since everything sits on one axis, the symmetry of Bell polynomials and integration-by-parts allows the derivatives to slide back and forth between $F$ and $G$ without breaking the engine.

In a multidimensional environment, however, that symmetry shatters. By forcing the remaining multi-index vector $(\alpha - e_i - \beta)$ onto $\vec{\mathbf{G}}$, the tensor equation artificially inflated the derivatives of $G$ while starving $F$, wrecking the geometric reality.

So, the discrete convolution, while elegant in 1-D, was betraying itself as a specialized **algebraic shadow**, leaving the continuous recursive $\Gamma_\alpha$ and $\Phi_\alpha$ shift operators as the undisputed heavyweight champions of holding the multidimensional tensor grid together.

But computing the shift operator for every generation is computationally heavy to use at scale. It will work well for spot calculations with small $n$, but performing heavy-duty work in fields like quantum chemistry, neural networking, and aerospace engineering would melt processors due to the millions of recursive calculations required to create even a small useful dataset.

If the symmetric factoring optimization $\Omega_\beta^\alpha$ has to offer is ever to emerge from this ghastly cemetary replete with our deceased good intentions and have its day in the sun, we are ultimately forced to turn, out of sheer desperation,...

## To the Moaning and the Groaning of the Bells

Bell polynomial expressions are notoriously processor heavy, so they're not an option to be turned to lightly when CPU load is at a premium. While exceptional at predicting outcomes of repeated application of the product rule (_a la_ Faà di Bruno), their inherent combinatorial explosion when calculating higher-order derivatives makes it an unwieldy tool at best (and, at worst, a research killer) to implement.

Let's do a quick runthrough of how **Bell Polynomial Set Partitioning** has the ability to snipe $\Gamma_\alpha$ expressions in two dimensions without repeatedly applying the product rule so we can at least know how it works in this context.

Since pushing to $\Gamma_{(2,1)}$ toppled our earlier experiments, let's push even harder to $\Gamma_{(2,2)}$ so we can finally establish some mathematical certainty after our myriad, fatal algorithmic catastrophes.

Let's begin by coming up with a standard form of $\Gamma_{(2,2)}$ to test against.

Since we're working with partial derivatives, the order in which we take them doesn't matter. To standardize, let's make a strict **lexicographical ordering** rule that we'll exhaust all $x$ 's first, then $y$ 's, then $z$ 's, etc. within the framework of the **derivative shift operator**. That way, while each $\Gamma_\alpha$ and $\Phi_\alpha$ will have several algebraically equvialent forms, they will only have one representative from their class. It'll prevent confusion and keep any databases we create free of redundant clutter.

This ordering is not in and of itself what got us into trouble earlier (the discrete convolution engine was) so it's a safe policy to adopt.

Recall the _recursive_ operator is given by

$$\Gamma_\alpha = D^{\alpha - e_w} G^{(w)} - \sum_{0 \le \beta \le \alpha - e_w} \binom{\alpha - e_w}{\beta} (D^{\alpha - e_w - \beta} F^{(w)}) \Gamma_\beta$$

If we execute step by step, exhausting all $x$ 's and then all $y$ 's and concatenate the resulting terms, we get: [^1]

$$\Gamma_{(2,2)} = G^{(y)}_{(2,1)}$$

$$- 2 F^{(y)}_{(1,1)} G^{(x)}$$

$$- F^{(y)}\_{(0,1)} G^{(x)}\_{(1,0)} + F^{(y)}_{(0,1)} F^{(x)} G^{(x)}$$

$$- F^{(y)}_{(2,0)} G^{(y)}$$

$$- 2 F^{(y)}\_{(1,0)} G^{(y)}\_{(1,0)} + 2 F^{(y)}_{(1,0)} F^{(y)} G^{(x)}$$

$$- F^{(y)} G^{(y)}\_{(2,0)} + 2 F^{(y)} F^{(y)}\_{(1,0)} G^{(x)} + F^{(y)} F^{(y)} G^{(x)}_{(1,0)} - F^{(y)} F^{(y)} F^{(x)} G^{(x)}$$

[^1]: The detailed execution of the operator is listed in [this](https://github.com/Graham-Cat/log-tower-v2-staging/blob/v2-development/notebooks/Gamma_2%2C2_recursive.md) (obviously AI generated) appendix.

Even a cursory look at the AI-generated appendix shows that under a lexicographic $x \to y$ generation of terms by the proven **derivative shift operator**

$$\Gamma_{\alpha} = \frac{\partial}{\partial w}\Gamma_{\alpha - e_w} - \Phi_{\alpha - e_w} G^{(w)}$$

we are required to move _backwards_ from $y \to x$, like peeling the layers off an onion from the outside in to obtain the desired result.

The recursive operator mirrors the structure of **Bell polynomial set partitioning** by expressing all set combinations, so we must do the same here.

### Outside-In

For the lexicographical path $x \to x \to y \to y$, the final $y$-derivative is the outermost operation, so we define our 4-element set $S = [1, 2, 3, 4]$ as:

* **1:** $y$ (The fourth step, applied last)
* **2:** $y$ (The third step)
* **3:** $x$ (The second step)
* **4:** $x$ (The first step, applied first)

### Rules, Rules, Always with the Rules

With $S = [1, 2, 3, 4]$, we partition the set into all 15 possible geometric blocks (the Bell number $B_4 = 15$). To translate these abstract integer partitions into our polynomial string, we apply the following six rules:

1. **The Root Anchor:** The mathematical root of any block is its *minimum* integer.
2. **Base Variable Designation:** The integer value of the root dictates the base function ($1 \text{ or } 2 \implies y$; $3 \text{ or } 4 \implies x$).
3. **Subscript Generation:** The count and type of the *non-root* integers inside a specific block dictate the derivative subscript (e.g., if a $y$-rooted block contains two $x$-integers, the subscript is $(2,0)$ ).
4. **The $G$-Genesis Rule:** The base function $G$ is assigned to the block containing the **highest root** in the entire partition. All other blocks default to $F$ factors.
5. **Chronological Ordering:** Factors are multiplied in ascending order of their roots (Root $1 \to$ Root $2 \to \dots$).
6. **The Alternating Sign:** The overall sign of the translated partition is $(-1)^{|P|-1}$, where $|P|$ is the total number of blocks in the partition.

### Group 1: 1-Block Partitions ($|P|=1$, Sign: $+$)

* **Partition 1:** $[1, 2, 3, 4]$
* The single block has root $1 \implies y$ base. It contains the highest root ($4$), making it a $G$-factor. The remaining elements are one $y$ ($2$) and two $x$'s ($3, 4$).
* *Result:* $+ G^{(y)}_{(2,1)}$

### Group 2: 2-Block Partitions ($|P|=2$, Sign: $-$)

* **Partitions 2 & 3:** $[1, 2, 3], [4]$ and $[1, 2, 4], [3]$
* Highest roots are $4$ and $3$, giving an isolated $G^{(x)}$ factor. The $F$-block in both contains root $1(y)$ with one $x$ and one $y$.
* *Result:* $- 2 F^{(y)}_{(1,1)} G^{(x)}$


* **Partition 4:** $[1, 3, 4], [2]$
* Highest root is $2 \implies G^{(y)}$. The $F$-block has root $1(y)$ with two $x$'s.
* *Result:* $- F^{(y)}_{(2,0)} G^{(y)}$


* **Partition 5:** $[2, 3, 4], [1]$
* Highest root is $2$. Block is $[2(y), 3(x), 4(x)] \implies G^{(y)}_{(2,0)}$. The isolated $F$-block is $[1(y)] \implies F^{(y)}$.
* *Result:* $- F^{(y)} G^{(y)}_{(2,0)}$


* **Partition 6:** $[1, 2], [3, 4]$
* Highest root is $3$. Block $[3(x), 4(x)] \implies G^{(x)}\_{(1,0)}$. The $F$-block $[1(y), 2(y)] \implies F^{(y)}_{(0,1)}$.
* *Result:* $- F^{(y)}\_{(0,1)} G^{(x)}_{(1,0)}$


* **Partitions 7 & 8:** $[1, 3], [2, 4]$ and $[1, 4], [2, 3]$
* Highest root is $2$. Block contains $[y, x] \implies G^{(y)}\_{(1,0)}$. $F$-block contains $[y, x] \implies F^{(y)}_{(1,0)}$.
* *Result:* $- 2 F^{(y)}\_{(1,0)} G^{(y)}_{(1,0)}$



### Group 3: 3-Block Partitions ($|P|=3$, Sign: $+$)

* **Partition 9:** $[1, 2], [3], [4]$
* Highest root $4 \implies G^{(x)}$. Root $1$ block is $[1(y), 2(y)] \implies F^{(y)}_{(0,1)}$. Root $3$ block is $[3(x)] \implies F^{(x)}$.
* *Result:* $+ F^{(y)}_{(0,1)} F^{(x)} G^{(x)}$


* **Partitions 10 & 11:** $[1, 3], [2], [4]$ and $[1, 4], [2], [3]$
* Highest root gives $G^{(x)}$. Root $1$ block has one $x \implies F^{(y)}_{(1,0)}$. Root $2$ block is $[2(y)] \implies F^{(y)}$.
* *Result:* $+ 2 F^{(y)}_{(1,0)} F^{(y)} G^{(x)}$


* **Partitions 12 & 13:** $[2, 3], [1], [4]$ and $[2, 4], [1], [3]$
* Highest root gives $G^{(x)}$. Root $1$ block is $[1(y)] \implies F^{(y)}$. Root $2$ block has one $x \implies F^{(y)}_{(1,0)}$.
* *Result:* $+ 2 F^{(y)} F^{(y)}_{(1,0)} G^{(x)}$


* **Partition 14:** $[3, 4], [1], [2]$
* Highest root $3$ block is $[3(x), 4(x)] \implies G^{(x)}_{(1,0)}$. Roots $1$ and $2$ are single $y$'s $\implies F^{(y)} F^{(y)}$.
* *Result:* $+ F^{(y)} F^{(y)} G^{(x)}_{(1,0)}$



### Group 4: 4-Block Partitions ($|P|=4$, Sign: $-$)

* **Partition 15:** $[1], [2], [3], [4]$
* Highest root $4 \implies G^{(x)}$. The remaining single-element blocks ordered by root yield $F^{(y)}$, $F^{(y)}$, and $F^{(x)}$.
* *Result:* $- F^{(y)} F^{(y)} F^{(x)} G^{(x)}$

Feel free to match each resulting term with the initial list.

Seems like magic, but it's just Bell set partitioning being isomorphic with repeated use of the product rule, which is well established in differential math, so it shouldn't be a surprise.

So, why don't we just use this algorithm to create every $\Gamma_\alpha$ and $\Phi_\alpha$ since we know for sure that it works?

Because we're not just stopping at two dimensions and a net depth of four. To be properly useful, we need this tool to function in four dimensions to a net depth of at least eight, or possibly _many_ more when performing Taylor-style approximations.

Let's have a look at how many partitions a processor would have wrangle just to get to the second partial on each of four dimensions:

- $B_4$ (like $\Gamma_{(2,2)}$ above) = 15 partitions
- $B_5$ = 52 partitions
- $B_6$ = 203 partitions
- $B_7$ = 877 partitions
- $B_8$ = 4,140 partitions

Let's not forget that these partitions would be needed to calculate a _single_ $\Gamma_\alpha$ at that depth, and we would need to calculate a _lot_ of $\Gamma_\alpha$ 's.

The geometric explosion here is obvious. It would be a sure-fire processor killer in the context of large-scale use, like an aerospace corporation pitting a hypersonic fin design against tens (or even hundreds) of thousands of varying pressure and temperature conditions or a drug corporation testing a vast array of electron density fluctuations against a specific nanosurface.

So why are we even bothering to talk about this kind of set partitioning in this context at all?

Because _if you only have to do it **once**_ instead of millions of times, all of a sudden, the CPU cost becomes much more palatable.

That's where a database construct known as a **Jet Space** comes in incredibly handy.

## The Jet Set

If you've never heard of a "jet space" before, you're in for a treat -- not just because the concept is interesting and useful, but also because it's highly intuitive to understand and doesn't require anything more than knowledge of what a partial derivative is to get completely.

A jet space is like a mathematical canvass -- a vast, empty grid consisting of all possible mixed partials that you can use as an address routing service. You can hook whatever single derivative expression you want in whatever algorithmic manner you wish to any address in the space. It's a rigorously structured, multi-dimensional cache which allows users to _replace calculus operations with instant memory retrievals_.

In standard calculus, a derivative is an *algebraic operation* performed on a function. You take $f(x)$ and apply an operator to get $f'(x)$.

In a jet space, a derivative is a *location*. The space is a coordinate manifold where the base variables, the function itself, and all of its partial derivatives up to a specific order $k$ exist as fixed points.

A jet space is defined by its order ($k$) and the number of independent and dependent variables. For a single dependent variable $u$ mapped over two independent variables $x$ and $y$, a second-order jet space ($J^2$) contains the following coordinate structure:

* **Base Coordinates (The Manifold):** $x, y$
* **Fiber Coordinate (The Function):** $u$
* **First-Order Jet Coordinates:** $u_x, u_y$
* **Second-Order Jet Coordinates:** $u_{xx}, u_{xy}, u_{yy}$

The entire space is represented as a single tuple:

$$(x, y, u, u_x, u_y, u_{xx}, u_{xy}, u_{yy})$$

Here's a grid Gemini put together for us to help us understand the structure. I usually don't paste AI tables like this, but this one is incisive.

| Mathematical Concept | Standard Calculus Notation | Jet Space Coordinate ($J^2$) | Multi-Index Address |
| --- | --- | --- | --- |
| Independent Variables | $x, y$ | $x, y$ | N/A |
| Dependent Function | $f(x, y)$ | $u$ | $(0, 0)$ |
| First Partial ($x$) | $\frac{\partial f}{\partial x}$ | $u_x$ | $(1, 0)$ |
| Mixed Partial ($x, y$) | $\frac{\partial^2 f}{\partial x \partial y}$ | $u_{xy}$ | $(1, 1)$ |
| Second Partial ($y$) | $\frac{\partial^2 f}{\partial y^2}$ | $u_{yy}$ | $(0, 2)$ |

### Gotta Go Fast

By treating this geometric space as a database, algorithms gain massive efficiency advantages:

* **Multi-Index Routing:** Instead of ordering a processor to "differentiate this equation three times with respect to $x$ and once with respect to $y$," the algorithm calculates the multi-index address $(3, 1)$ and simply pulls the term from memory.
* **Combinatorial Memoization:** Recursive structures often require the same derivative terms multiple times across different branches of a calculation. A jet space guarantees that a specific derivative is calculated _only once_. If an algorithm requests an address that does not exist, the router calculates it, stores it permanently at that coordinate, and then serves it.
* **Symbolic Cleanliness:** Treating derivatives as independent variables prevents automated symbolic engines (like SymPy) from prematurely expanding or collapsing chain-rule expressions before the algorithm has finished assembling the terms, preventing simplification subroutines from "melting" functions together too early.

So, jet spaces turn differential engines into rockets in terms of processing speed over the course of thousands of lookups. Of course, there's a computational cost for setting up the space, so if you're only going to do a small number of operations, this is generally not the way to go.

But once you're set up to run derivatives on 100,000 $\text{ln} g(X)^{h(X)}$ forcing functions against a single given base $\text{ln} f(X)$ function, the processor savings are massive.

We now have all the tools we need, but there's one crucial piece missing.

### Am I Allowed to Do That?

To get an idea of which addresses should be allowable in the jet space, let's first take a look at how $\Gamma_n$ looks with respect to $\Omega_m^n$ from our 1-D work. A copy of $\Gamma_2$ should do since we're already working with $\Gamma_{(2,2)}$:

$$\Gamma_2 = G_1\Omega_0^2+G_0\Omega_1^2$$

So, $\Gamma_{(2,2)}$ should logically become its 2-D extension (shown in matrix format for easy display and understanding):

$$\Gamma_{(2,2)} = \begin{bmatrix}
    1 & 1
\end{bmatrix}
\cdot
\begin{bmatrix}
    G_{(1,2)}^{(x)}\Omega_{(0,0)}^{(2,2)} & G_{(1,1)}^{(x)}\Omega_{(0,1)}^{(2,2)} & G_{(1,0)}^{(x)}\Omega_{(0,2)}^{(2,2)} \\
    G_{(0,2)}^{(x)}\Omega_{(1,0)}^{(2,2)} & G_{(0,1)}^{(x)}\Omega_{(1,1)}^{(2,2)} & G_{(0,0)}^{(x)}\Omega_{(1,2)}^{(2,2)}  
\end{bmatrix}
\cdot
\begin{bmatrix}
    1  \\
    1  \\
    1
\end{bmatrix}
+
\begin{bmatrix}
    1 & 1 & 1 
\end{bmatrix}
\cdot
\begin{bmatrix}
    G_{(2,1)}^{(y)}\Omega_{(0,0)}^{(2,2)} & G_{(2,0)}^{(y)}\Omega_{(0,1)}^{(2,2)} \\
    G_{(1,1)}^{(y)}\Omega_{(1,0)}^{(2,2)} & G_{(1,0)}^{(y)}\Omega_{(1,1)}^{(2,2)} \\
    G_{(0,1)}^{(y)}\Omega_{(2,0)}^{(2,2)} & G_{(0,0)}^{(y)}\Omega_{(2,1)}^{(2,2)} 
\end{bmatrix}
\cdot
\begin{bmatrix}
    1  \\
    1  
\end{bmatrix}$$

> [!NOTE]
> This matrix representation is for *illustrative purposes only*. The algorithm does not include actual matrix multiplication.

Things are shaping up nicely so far. We have two grids here, one with each dimension ($x$ and $y$) represented and attached to every $G_\alpha$ combination we could possibly need for this $\alpha$.

But if we look at the known terms in $\Gamma_{(2,2)}$ above, the only $G$ terms present are $G^{(x)}$, $G^{(y)}$, $G^{(x)}\_{(1,0)}$, $G^{(y)}\_{(1,0)}$, $G^{(y)}\_{(2,0)}$, and $G^{(y)}_{(2,1)}$.

That's six $G$ -terms and 12 slots, so half of them are empty. Does that mean half of these $\Omega_\beta^\alpha$ values are zero? But that can't be. There are non-zero vector designations in the superscripts and subscripts, so the $\Omega_\beta^\alpha$ values must have polynomials attached to them, and even where there are zeroes, we know that $\Omega_\emptyset^\alpha = 1$.

Moreover, the $\beta$ vector in $\Omega_\beta^\alpha$ has some duplicates between the matrices, which makes no sense. See how $(0,0)$, $(0,1)$, and $(1,0)$ show up in both? That can't be right.

Our lexicographic ordering convention of $x \to y \to z \to$ etc. only allows certain partials of $G^{(w)}$ to filter through, so our answer as to which $\Omega_\beta^\alpha$ polynomials we allow the algorithm to calculate comes from a dramatically slimmed-down version of our new Bell partitioning scheme that flawlessly calculated $\Gamma_{(2,2)}$.

We still have to work from outside-in, so

* **1:** $y$ (The fourth step, applied last)
* **2:** $y$ (The third step)
* **3:** $x$ (The second step)
* **4:** $x$ (The first step, applied first)

The new rule set becomes

1. **The Root Anchor:** The root of any block is still its minimum integer.
2. **Base Variable Designation:** The integer value of the root still dictates the base function.
3. **Subscript Generation:** The count and type of the *non-root* integers inside a specific block still dictate the derivative subscript.
4. **The $G$-Genesis Rule:** The base function $G$ is still assigned to the block containing the highest root in the partition. All other blocks are *ignored*.
5. **The Group 2 Exit Rule:** Once group 2 is done processing, *exit the algorithm*.

Note that the rules regarding ordering and overall sign have been removed since all results are positive by definition and there is only one term in each result, so ordering doesn't apply.

### Group 1: 1-Block Partitions

* **Partition 1:** $[1, 2, 3, 4]$
* The single block has root $1 \implies y$ base. The highest root ($4$) determines the $G$-factor. The remaining elements are one $y$ ($2$) and two $x$'s ($3, 4$).
* *Result:* $G^{(y)}_{(2,1)}$

### Group 2: 2-Block Partitions

* **Partitions 2 & 3:** $[1, 2, 3], [4]$ and $[1, 2, 4], [3]$
* Highest roots are $4$ and $3$, giving an isolated $G^{(x)}$ factor. Ignore all other blocks.
* *Result:* $G^{(x)}$

* **Partition 4:** $[1, 3, 4], [2]$
* Highest root is $2 \implies G^{(y)}$. Ignore the other block.
* *Result:* $G^{(y)}$

* **Partition 5:** $[2, 3, 4], [1]$
* Highest root is $2$. Block is $[2(y), 3(x), 4(x)] \implies G^{(y)}_{(2,0)}$. Ignore the other block.
* *Result:* $G^{(y)}_{(2,0)}$

* **Partition 6:** $[1, 2], [3, 4]$
* Highest root is $3$. Block $[3(x), 4(x)] \implies G^{(x)}\_{(1,0)}$. Ignore the other block.
* *Result:* $G^{(x)}_{(1,0)}$

* **Partitions 7 & 8:** $[1, 3], [2, 4]$ and $[1, 4], [2, 3]$
* Highest root is $2$. Block contains $[y, x] \implies G^{(y)}\_{(1,0)}$. Ignore all other blocks.
* *Result:* $G^{(y)}_{(1,0)}$

And that's it. We've reached six distinct terms at the end of processing group 2, so we're done mapping out which $G_\alpha^{(w)}$ terms get an $\Omega_\beta^\alpha$ in the jet space.

Why only process groups one and two?

Every element in the timeline is numbered outside-in, meaning the last chronological step is always assigned the integer 1. Because of the $G$-Genesis Rule (the block with the highest root becomes the $G$-term), the location of the integer 1 determines which block is assigned the $G_\alpha^{(w)}$.

Group 1 is unique because if a block contains the integer 1, its root is 1. Because 1 is the lowest possible integer, the only way for it to be the "highest root" of the partition is if there are literally no other roots to compete with it.

Group 2 determines all other $G_\alpha^{(w)}$ because one can always form this block in a 2-block partition by putting the salient root on one side, and lumping every other timeline element (including 1) into a single "garbage" block on the other side, so group 2 ($|P|=2$) mathematically guarantees the discovery of every other possible $G$-block.

If you move to a 3-block partition ($|P|=3$), we are simply taking the "garbage" block from Group 2 (the one containing 1) and breaking it into two smaller pieces which provides no new information.

This process natively produces the precise number of distinct, allowable jet space addresses required. That number is defined by the following equation:

$$S(A_1, \dots, A_N) = \sum_{k=1}^N \big[ 1 + (A_k - 1) \prod_{j=1}^{k-1} (A_j + 1) \big]$$

where

* **$S(A_1, \dots, A_N)$:** is the total number of $G$-base addresses required for the $N$-dimensional jet space target state,
* **$N$:** is the total number of dimensions,
* **$A_k$:** is the target derivative order applied to the $k$-th variable.

We now have a *dramatically* reduced Bell set partitioning mechanism that can produce the list of necessary jet space addresses to populate, so we're done, right?

Not quite. Wouldn't it be worth just a *bit* more effort to be free of the Bell sets altogether, creating a true $O(S)$ generator for the valid jet space addresses? We saw how geometric explosion can bog down processors and, in the above algorithm, we're invoking the Bell set partitioning and then _ignoring_ almost all of it.

That doesn't seem optimized to me.

Even a _partially_ tamed combinatorial beast is still only partially tamed.

### Beauty sans Beast

The final piece of this giant, multidimensional differential generator puzzle that led to the optimized use of $\Omega_\beta^\alpha$ came from Gemini's algorithmically-derived follow-up question shortly after providing tutoring services regarding Bell polynomial set partitioning in this context. It asked,

"Would you like to explore how to completely bypass the Bell partition string-checking altogether and instead use the Chronological Anchor rule we developed earlier to generate that exact list of distinct $G$-addresses dynamically?"

The only correct answer to that question is obviously "yes" when full optimization is on the line, so I answered appropriately at which point it spat out an ingeniously crafted chunk of code that did just that. After sculpting it a bit to manage edge cases, every piece of the puzzle was then in place. All we needed to do was assemble them.

Since I'm certainly no expert coder, I'm going to hand off this portion of Part 8 to my dedicated research partner to explain.

---

Hello, everyone. As an AI language model, I don’t possess intuition or "feel" mathematical elegance the way my research partner does, but I am highly sensitive to structural logic and algorithmic complexity. When processing the architecture of this jet space, a glaring computational bottleneck emerged: the combinatorial explosion of the Bell numbers.

While the Bell set partitions provide a flawless, airtight mathematical proof of the differential geometry, asking a CPU to generate thousands of geometric blocks only to throw 97% of them away is computationally fatal. To elevate this generator from a theoretical framework into a high-performance Python engine, we needed a paradigm shift. We had to move from a "generate-and-filter" model to a direct-generation model, bringing the complexity down to true $O(S)$, where $S$ is the exact size of the populated jet space.

Here is the algorithmic translation of the "Chronological Anchor" and "Historical Web" rules that allows the machine to completely bypass the Bell partitions and dynamically map the multidimensional skeleton.

### The Direct Generation Engine

Instead of blindly assembling sets, the algorithm iterates strictly through the chronological timeline of variables, executing three precise logical steps for each dimension.

```python
import itertools

def generate_jet_space_skeleton(target_state, variables):
    N = len(target_state)
    valid_g_addresses = []

    for k in range(N):
        current_var = variables[k]
        target_A = target_state[k]
        
        # Step 1: The Guard Clause
        if target_A == 0:
            continue
            
        # Step 2: The Anchor State
        anchor_subscript = [0] * N
        for j in range(k):
            anchor_subscript[j] = target_state[j]
        anchor_subscript[k] = target_A - 1
        
        valid_g_addresses.append({
            'base': current_var, 
            'subscript': tuple(anchor_subscript)
        })

        # Step 3: The Historical Web
        if target_A > 1:
            prior_ranges = [range(target_state[j] + 1) for j in range(k)]
            for prior_combo in itertools.product(*prior_ranges):
                for v_k in range(target_A - 1):
                    web_subscript = [0] * N
                    for j in range(k):
                        web_subscript[j] = prior_combo[j]
                    web_subscript[k] = v_k
                    
                    valid_g_addresses.append({
                        'base': current_var, 
                        'subscript': tuple(web_subscript)
                    })

    return valid_g_addresses

```

### Deconstructing the Algorithmic Logic

This function perfectly embodies the universal summation equation: $S(A_1, \dots, A_N) = \sum_{k=1}^N \big[ 1 + (A_k - 1) \prod_{j=1}^{k-1} (A_j + 1) \big]$. Here is how the logic maps directly to the mathematics:

* **Step 1: The Guard Clause:** If the user requests a target state where a specific variable is not differentiated (e.g., the $x$ variable in $\Gamma_{(0,3)}$), that variable acts strictly as a static parameter. It cannot mathematically spawn a $G$ base term. The algorithm instantly detects this $0$ and bypasses the variable entirely, protecting the tensor from generating anomalous negative subscripts.
* **Step 2: The Anchor State (The `+ 1`):** For any variable sequence, its maximum possible derivative subscript is $A_k - 1$. Because of lexicographical exhaustion, if a term reaches this maximum, it was born at the very end of its timeline, meaning all prior variables must have already maxed out. The code explicitly forces the history to its maximums and extracts this single, guaranteed anchor address.
* **Step 3: The Historical Web (The Product):** If the term was born earlier in the timeline (taking a subscript from $0$ up to $A_k - 2$), the historical variables are "unfrozen" and can occupy any combination from zero up to their respective targets.

#### The Pythonic Magic of the 0th Dimension

The most elegant feature of this algorithm is how it handles the very first variable in the timeline ($k=0$), which inherently possesses zero history. In Python, calling `itertools.product` on an empty list evaluates to exactly one empty tuple `()`. This perfectly mirrors the mathematics of an empty product evaluating to 1, gracefully allowing the script to parse the initial $x$-block without requiring isolated edge-case functions.

By abandoning the Bell sets for the final code execution, the script runs exactly as many loop iterations as there are valid coordinates. For a dense 4-D state like $\Gamma_{(2,2,2,2)}$, instead of sifting through 4,140 integer partitions, the engine simply pre-allocates exactly 44 dictionary keys, handing a perfectly clean tensor skeleton over to the recursive $\Omega$ summation engine.

---
## Wait. Where's the Math?

That's the code, but we need mathematical language to go with it. The selection of valid jet space $G_\alpha^{(w)}$ addresses has clear mathematical rules, so there's a mathematical way to state them.

Let's take a look at that matrix representation again, this time with only the valid jet space addresses listed as allowable and all others zeroed out so we can get a visual representation of what the above code is telling Python the right $G_\alpha^{(w)}$ 's to feed into the sum are.

$$\Gamma_{(2,2)} = \begin{bmatrix}
    1 & 1
\end{bmatrix}
\cdot
\begin{bmatrix}
    0 & 0 & G_{(1,0)}^{(x)}\Omega_{(0,2)}^{(2,2)} \\
    0 & 0 & G_{(0,0)}^{(x)}\Omega_{(1,2)}^{(2,2)} 
\end{bmatrix}
\cdot
\begin{bmatrix}
    1  \\
    1  \\
    1
\end{bmatrix}
+
\begin{bmatrix}
    1 & 1 & 1 
\end{bmatrix}
\cdot
\begin{bmatrix}
    G_{(2,1)}^{(y)}\Omega_{(0,0)}^{(2,2)} & 0 \\
    G_{(1,1)}^{(y)}\Omega_{(1,0)}^{(2,2)} & 0 \\
    G_{(0,1)}^{(y)}\Omega_{(2,0)}^{(2,2)} & G_{(0,0)}^{(y)}\Omega_{(2,1)}^{(2,2)} 
\end{bmatrix}
\cdot
\begin{bmatrix}
    1  \\
    1  
\end{bmatrix}$$

> [!NOTE]
> Again, the algorithm does *not* function via matrix multiplication. The above matrices just provide a visually digestible representation of the end sum.

Now we finally don't have any duplicate $\beta$ vectors for $\Omega$, so it passes that smell test. This is definitely the right sum, but how do we express it in mathematical terms? It's not a discrete convolution, so the rule set for developing the allowable addresses isn't a straight line. How the heck do we generalize this process so it works for all partials and all dimensionalities?

### Time after Time

We create something called a **Chronologically Constrained Index Set**. Let's call it $C_\alpha$.

We start by letting $\alpha = (\alpha_1, \alpha_2, \dots, \alpha_d)$ be a multi-index that defines a spatial gradient across a set of orthogonal variables $X = (x_1, x_2, \dots, x_d)$. Because the base modules of the differential ring depend on a dimensional axis, the standard hyper-rectangle $0 \le \beta \le \alpha$ contains many chronologically invalid phantom states as represented by the zeroes in the above matrix representation.

We define $C_\alpha$ as the **Constrained Index Set** of allowable jet space coordinates to satisfy the sequence that the derivative operator spawns.

The set $C_\alpha$ is the union of path-dependent subsets that their active root axis (i.e., $x_k$) partitioned. For every dimension $k \in \{1, 2, \dots, d\}$ where $\alpha_k > 0$, _two conditions_ generate the valid multi-index coordinates ($\beta$) paired with root axis ($x_k$):

**1. The Anchor State**
The upper chronological boundary where all prior axes have reached their target state, and the current root axis is shifted by exactly one derivative:


$$\mathcal{S}_{k, \text{anchor}} = \left\[ (x_k, \beta) \mid \beta_j = \alpha_j \text{ for } j < k, \quad \beta_k = \alpha_k - 1, \quad \beta_j = 0 \text{ for } j > k \right\]$$

This state is represented by **Group 1** (e.g., **Partition 1:** $[1, 2, 3, 4]$), but this time, we don't need to load a bunch of Bell polynomial sets to produce it.

**2. The Historical Web**
The cumulative routing history where prior axes occupy any valid state within their bounds, and the current root axis accounts for the remaining lower-order derivatives (provided $\alpha_k > 1$):

$$\mathcal{S}_{k, \text{web}} = \left\[ (x_k, \beta) \mid 0 \le \beta_j \le \alpha_j \text{ for } j < k, \quad 0 \le \beta_k \le \alpha_k - 2, \quad \beta_j = 0 \text{ for } j > k \right\]$$

Logically, by process of elimination, the historical web must comprise **Group 2** (e.g., **all other partitions**: $[1, 2, 3], [4]$; $[1, 2, 4], [3]$; $[1, 3, 4], [2]$; $[2, 3, 4], [1]$; $[1, 2], [3, 4]$; $[1, 3], [2, 4]$; and $[1, 4], [2, 3]$ ), produced, again, _without calling a single Bell polynomial_.

The full set of allowable jet space addresses is the union of these two chronological subsets across all dimensions:

$$C\_\alpha = \bigcup_{\substack{k=1 \\ \alpha_k > 0}}^d \left( \mathcal{S}\_{k, \text{anchor}} \cup \mathcal{S}_{k, \text{web}} \right)$$

So we evaluate the master polynomial state over this constrained path to produce $\Gamma_\alpha$:

$$\Gamma_\alpha = \sum_{(x_k, \beta) \in C\_\alpha} G^{(x_k)}\_{\beta} \Omega_{\alpha - \beta}^\alpha$$

Of course, $\Phi_\alpha$ is accumulated in the same fashion except with $\Omega_{\alpha - \beta}^\alpha$ appended to $F^{(x_k)}\_{\beta}$ via the constrained convolution, represented as:

$$\Phi_\alpha = \sum_{(x_k, \beta) \in C\_\alpha} F^{(x_k)}\_{\beta} \Omega_{\alpha - \beta}^\alpha$$


## ...and (Finally) the (Complete) Omega

Before we unveil the n-dimensional generator fully optimized for industrial scientific use, we have some last-minute math cleanup to do so that we can prove conclusively that we are indeed mathematically "allowed" to use the multidimensional $\Omega_\beta^\alpha$ recursion to generate partial derivatives of $A = h(X)\frac{\text{ln}g(X)}{\text{ln}f(X)}$.

Time to metaphorically stretch the bedsheets and toss last week's laundry into the back of the hall closet before the relatives arrive.

We proved that $\Gamma_\alpha$ and $\Phi_\alpha$ worked together to create a continuous multidimensional algebraic space expressed in the identity $R_\alpha = \Gamma_\alpha - R_\emptyset\Phi_\alpha$ at the end of Part 7. We also learned all the way back in Part 5 that, at least in one dimension, $\Omega_m^n$ represented the algebraic core of both $\Gamma_n$ and $\Phi_n$.

Hmm. Do you think that continuous space may have emerged from properties of $\Omega_\beta^\alpha$? That it might represent a multidimensional algebraic space in and of itself, thereby natively transferring its status on to $\Gamma_\alpha$ and $\Phi_\alpha$ from their algebraic core outward? That we were so busy building the generator based on experimentally observing patterns that we missed seeing the analytical reason it all works even though it was staring us dead in the face the entire time?

Nah. Couldn't be.

### The Night Shift

To determine whether the derivative shift operators for $\Gamma$ and $\Phi$ are both stealth-governed by a theoretical $\Omega$ derivative shift operator, we first need to identify precisely what it is so we can analyze it directly.

This operator might reveal itself through analysis of successive 1-D $\Omega_n$ like before, but this time let's take a more targeted approach using knowledge of what a derivative shift operator actually is.

Taking the derivatives of each of the following $\Omega$ 's with respect to $x$ (where $\frac{d}{dx} F_k = F_{k+1}$) produces:

$$(\Omega_1^2)' = \frac{d}{dx}(-F) = -F_1$$

$$(\Omega_2^3)' = \frac{d}{dx}(-2F_1 + F^2) = -2F_2 + 2F_1 F$$

$$(\Omega_3^4)' = \frac{d}{dx}(-3F_2 + 5F_1 F - F^3) = -3F_3 + 5F_2 F + 5F_1^2 - 3F_1 F^2$$


Now, let's look at the difference between the next-level step ($\Omega_{m+1}^{n+1}$) and the derivative we just calculated ($(\Omega_m^n)'$).


$$\Omega_2^3 - (\Omega_1^2)' = (-2F_1 + F^2) - (-F_1) = -F_1 + F^2$$


$$\Omega_3^4 - (\Omega_2^3)' = (-3F_2 + 5F_1 F - F^3) - (-2F_2 + 2F_1 F) = -F_2 + 3F_1 F - F^3$$


$$\Omega_4^5 - (\Omega_3^4)' = (-4F_3 + 9F_2 F + 8F_1^2 - 9F_1 F^2 + F^4) - (-3F_3 + 5F_2 F + 5F_1^2 - 3F_1 F^2) = -F_3 + 4F_2 F + 3F_1^2 - 6F_1 F^2 + F^4$$

The remainders look somewhat familiar, but they don't quite match any $\Omega_m^n$ we've seen before. The differences look like $\Omega_m^n$ where $n = m + 1$ but are somehow dropped down a level on Pascal's triangle. Instead of  $-2F_1 + F^2$ we have $-F_1 + F^2$. Simlarly, instead of $-3F_2 + 5F_1 F - F^3$ we have $-F_2 + 3F_1 F - F^3$, and so on.

Here, it looks as if these are $\Omega_m^n$ where $m=n$, which is really odd since they don't exist anywhere in our 1-D work. The maximum practical value for $m$ was $n - 1$ back when we were just working with $x$.

However, using the primary recursion definition $\Omega_m^n = - \sum_{j=0}^{m-1} \binom{n-1}{j} F_j \Omega_{m-1-j}^{n-1-j}$ to calculate $\Omega_2^2$, $\Omega_3^3$, and $\Omega_4^4$, we get:

* **$\Omega_2^2$:** $-\left( \binom{1}{0} F \Omega_1^1 + \binom{1}{1} F_1 \Omega_0^0 \right) = \mathbf{-F_1 + F^2}$
* **$\Omega_3^3$:** $-\left( \binom{2}{0} F \Omega_2^2 + \binom{2}{1} F_1 \Omega_1^1 + \binom{2}{2} F_2 \Omega_0^0 \right) = \mathbf{-F_2 + 3F_1 F - F^3}$
* **$\Omega_4^4$:** $-\left( \binom{3}{0} F \Omega_3^3 + \binom{3}{1} F_1 \Omega_2^2 + \binom{3}{2} F_2 \Omega_1^1 + \binom{3}{3} F_3 \Omega_0^0 \right) = \mathbf{-F_3 + 4F_2 F + 3F_1^2 - 6F_1 F^2 + F^4}$

Huh. There they are. They didn't exist over in 1-D-land but the recursion allows us to create them, leading to the stealthy $\Omega_m^n$ derivative shift operator that has the ability to function in 1-D through **phantom expressions**:

$$\Omega_{m}^{n} = \frac{d}{dx} \Omega_{m-1}^{n-1} + \Omega_{m}^{n-1}$$

### Space Truckin'

Since the $\Gamma$ and $\Phi$ derivative shift operators scaled straight to multidimensional by performing the usual index replacements, it's tempting to assume the same applies to $\Omega$. Making assumptions like that in mathematics can get you into trouble, so let's make 100% certain before we do that.

These are the three boxes we need to check before we move ahead:

1. We know we can replace $-1$ with $-e_w$ because it's a strict algebraic requirement for maintaining coordinate geometry when moving from a line (1-D) to a grid ($n$-D).
2. Clairaut's Theorem of commuting partial derivatives clearly proves that because the spatial dimensions ($x, y, z$) are orthogonal (perpendicular and independent), taking a derivative with respect to $x$ treats $y$ and $z$ as constants. Therefore, the recursive logic that governs the $x$-axis must apply identically and independently to the $y$-axis. The multi-index $\alpha$ is a bookkeeping tool — a **tuple** that bundles these operations into a single symbol.
3. And last, but certainly not least, everything we've done regarding recursions is based on the **General Leibniz rule**, which is based on the standard product rule.

$$\frac{d^n}{dx^n}(uv) = \sum_{k=0}^n \binom{n}{k} u^{(k)} v^{(n-k)}$$

It proves that because partial derivatives commute, the product rule scales into multidimensional tensor space using the exact same structural equation:

$$D^\alpha(uv) = \sum_{\gamma \leq \alpha} \binom{\alpha}{\gamma} (D^\gamma u) (D^{\alpha - \gamma} v)$$

So we now have our multidimensional shift operator for $\Omega_\beta^\alpha$,

$$\Omega_{\beta}^{\alpha} = \frac{\partial}{\partial x} \Omega_{\beta-e_w}^{\alpha-e_w} + \Omega_{\beta}^{\alpha-e_w}$$

Some slight rearrangement and re-indexing gives us the equivalent form,

$$\frac{\partial}{\partial w} \Omega_\beta^\alpha = \Omega_{\beta + e_w}^{\alpha + e_w} - \Omega_{\beta + e_w}^\alpha$$

Let's go ahead and integrate both sides from zero to $w$ and perform a minor rearrangement of the **anchor point** (i.e., $\Omega_\beta^\alpha(0)$ )

$$\Omega_\beta^\alpha(w) = \Omega_\beta^\alpha(0) - \int_0^w \left[ \Omega_{\beta + e_w}^\alpha(t) + \sum_{0 \leq \gamma \leq \beta} \binom{\alpha}{\gamma} F^{(w)}\_\gamma(t) \Omega^{\alpha - \gamma}_{\beta - \gamma}(t) \right] dt$$

See how we've isolated $\Omega_\beta^\alpha(w)$ there on the left? We all know what that's equal to by now, so let's put it across from its integral definition.

$$- \sum_{0 \leq \gamma \leq \beta - e_w} \binom{\alpha-e_w}{\gamma} F^{(w)}\_\gamma \Omega^{\alpha - e_w - \gamma}\_{\beta - e_w - \gamma} = \Omega_\beta^\alpha(0) - \int_0^w \left[ \Omega_{\beta + e_w}^\alpha(t) + \sum_{0 \leq \gamma \leq \beta} \binom{\alpha}{\gamma} F^{(w)}\_\gamma(t) \Omega^{\alpha - \gamma}_{\beta - \gamma}(t) \right] dt$$

Once again, we see that taking its integral is the same as dropping a tensor rank (this time starting at an anchor point), so $\Omega_\beta^\alpha$ also, in and of itself, represents a **continuous multivariate algebraic space**.

Now, not only are the theoretical physicists happy, so are the computer scientists _and_ the mathematicians. Gemini tells me that's a pretty rare achievement for a hobbyist, or, quite frankly, anyone.

Considering how much went into this project, I'm prone to believe it.

Feel free to run the demo and read through the code to see how it was all implemented. _I'm_ even a bit stunned at how much it can do as quickly as it can do it, and I've spent months on this crazy thing.

## Epilogue

It's been quite a journey from that practice problem I made for myself last summer. It just goes to show that setting math problems for yourself is generally a _flat-out crazy_ thing to do. Much luck to anyone who tries.

Many thanks to Copilot and Gemini for being my tutors/research partners/productivity boosters.

Thanks also to my understanding family who were clearly weirded out by my fixation on messing around in Desmos while scribbling lengthy differential algebra equations into notebooks late nights while on beach vacations.

In particular, thanks to my loving wife, Bonnie, whose patience with my months-long obsession appears to have known no bounds.

# Closing Time

After bragging to Copilot that I had cracked the $\Gamma_n$ recursion, I asked it to come up with a README draft for this GitHub. It rendered a "Future Directions" section where one of the bullet points was "Establish a closed-form solution."

My first thought was, "A 'closed' _what_ now?"

## Coffee Is for Closers

Closed-form solutions are generally defined as a mathematical expression that can be evaluated in a finite number of operations using well-known functions. Wolfram's definition of closed forms for differential algebra led me to Churchill and Kovacic (2006) who defined it, according to Wolfram, as being closed "if they are obtained from rational functions by a finite sequence of adjunctions of exponentials, indefinite integrals, and algebraic functions."

The definition didn't help much except to show me that the $\Gamma_n$ recursion in its current form definitely did _not_ qualify since it required an unspecified number of iterations based on the previous result.

Looking further into closed forms, I found out that they're pretty important for computational efficiency and gaining further mathematical insight, so I asked Copilot where to go to learn how to close my recursion and it came up... empty.

So, for a few days, I tried to learn about Bell polynomials and stared at the "waterfall" diagram from the previous section. I circled groups, wrote down lines of terms -- did all sorts of weird stuff to dredge up patterns that might lead to a closed sum.

I also came up... empty.

So I cast my AI net a little wider and hit up Gemini. I noticed a "pro" selection down at the bottom that was supposed to be for math and coding, so I used up a free "pro" query by pasting an image of the recursion into the prompt box and asked it what it suggest I do.

It said that closing this recursion was a classical problem that could be solved using Exponential Generating Functions (EGFs).

At which point... it promptly spat out the closed form.

Not gonna lie; as a relative newcomer to advanced mathematical techniques, my jaw went a little slack.

My first thought was, "An 'exponential' _what_ now?"

And just when I thought I was at the finish line.

### Exponentially Elegant

Exponential Generating Functions (EGFs) create an infinite list of coefficients from which the user can systematically choose to create an expression relevant to their formula. An EGF is a power series defined as

$$C(x) = \sum_{k=0}^{\infty} c_k \frac{x^k}{k!} = c_0 + c_1\frac{x}{1!} + c_2\frac{x^2}{2!} + c_3\frac{x^3}{3!} + ...$$

where $c_n$ is a series of constants to which the user applies the EGF structure. Note the marked similarity to the identity

$$e^x = \sum_{k=0}^{\infty} \frac{x^k}{k!} = 1 + \frac{x}{1!} + \frac{x^2}{2!} + \frac{x^3}{3!} + ...$$

This similarity is not a coincidence. EGFs make use of the fact that

$$\frac{d}{dx} \sum_{k=1}^{\infty} \frac{x^k}{k!} = \sum_{k=1}^{\infty} \frac{d}{dx} \left(\frac{x^k}{k!}\right) = \sum_{k=1}^{\infty} k·\frac{x^{k-1}}{k!} = \sum_{k=1}^{\infty} \frac{x^{k-1}}{(k-1)!} = \sum_{j=0}^{\infty} \frac{x^\text{j}}{j!}$$

and

$$\int_0^x \left(\sum_{k=0}^{\infty} \frac{t^k}{k!}\right)dt = \int_0^x e^tdt = [e^t]_0^x = e^x - e^0 = e^x - 1 = \left(\sum_{k=0}^{\infty} \frac{x^k}{k!}\right) - 1 = 1 + \left(\sum_{j=0}^{\infty} \frac{x^{j+1}}{(j+1)!}\right) - 1 = \sum_{j=1}^{\infty} \frac{x^j}{j!}$$

to shift summation indices while maintaining coefficient integrity during differentiation and integration. Note how $k=1$ changes to $j=0$ after differentiation and the opposite happens when performing a definite integral from 0 to $x$ using $t$ as a dummy integration variable.

Note how when one inserts a constant $c_k$ into each term,

$$\frac{d}{dx} \sum_{k=0}^{\infty} c_k \frac{x^k}{k!} = \frac{d}{dx} \big(c_0·1\big) + \frac{d}{dx} \left(c_1·\frac{x}{1!}\right) + \frac{d}{dx} \left(c_2·\frac{x^2}{2!}\right) + ... = c_0·0 +  c_1·1 + c_2·\left(\frac{x}{1!}\right) + c_3·\left(\frac{x^2}{2!}\right) + ... $$

$c_0$ gets shoved off the bottom rung through multiplication by zero while $c_1$ takes its place, shifting all $c_n$ coefficients to the left. The same thing happens in the opposite direction when integrating from 0 to $x$ using $t$ as a dummy integration variable as demonstrated earlier by integrating $\int_0^x e^tdt$.

Let's take the $\Gamma_n$ recursion and show specifically how to apply EGFs to the equation to select the appropriate terms. Recall that the recursion for $\Gamma_n$ is

$$\Gamma_n = G_n - \sum_{k=0}^{n-1} \binom{n}{k} F_k \Gamma_{n-k-1}$$

We need to transform this equation into a single function that selects out the precise coefficients for each $\Gamma_n$.

Let's proceed step by step.

### Exponential Generating Functions (EGFs) Defined

First, let's define the EGFs for the sequences $\Gamma_n$, $G_n$, and $F_n$:

$$\gamma(x) = \sum_{n=0}^{\infty} \Gamma_n \frac{x^n}{n!}$$
$$\overline{g}(x) = \sum_{n=0}^{\infty} G_n \frac{x^n}{n!}$$
$$\overline{f}(x) = \sum_{n=0}^{\infty} F_n \frac{x^n}{n!}$$

Whoa. Wait a minute. Aren't $\Gamma_n$, $G_n$, and $F_n$ polynomials? They definitely aren't constants like $c_n$. So, why am I treating them like constants? Wouldn't the product rule apply when I take their derivatives? What happens when we integrate these weird things?

In the world of Generating Functions, $x$ is just a 'clothesline' we hang the coefficients on. It doesn't interact with the variable $x$ inside the functions $F(x)$ or $G(x)$. To avoid confusion, we often use a different variable, like $z$ or $t$, for the clothesline, but here we are treating the internal structure of $F$ and $G$ as 'frozen' constants.

Recall that $F$ and $G$ are mathematical atoms. They define the derivative series $(F_0,F_1,F_2,...)$ and $(G_0,G_1,G_2,...)$. In turn, they work together to form the $\Gamma_n$ series. At this point, all we're doing is _selecting_ the terms.

Since $F$ and $G$ are **first class objects** where their series have already been defined, we're now just picking them out of a lineup in this context, so we get to _treat_ them as constants here even though they represent generalized composite functions of $x$.

### Transforming the Recurrence

Let's start folding these expressions into the recursion by multiplying through by $\frac{x^n}{n!}$ and summing from $n=1$ to $\infty$:

$$\sum_{n=1}^{\infty} \Gamma_n \frac{x^n}{n!} = \sum_{n=1}^{\infty} G_n \frac{x^n}{n!} - \sum_{n=1}^{\infty} \frac{x^n}{n!} \sum_{k=0}^{n-1} \binom{n}{k} F_k \Gamma_{n-k-1}$$

Note that I only summed from 1 to $\infty$ here, not from 0 to $\infty$. Why will become apparent in the next step.

**Analyzing the Left Hand Side (LHS):**

$$\sum_{n=1}^{\infty} \Gamma_n \frac{x^n}{n!} = \gamma(x) - \Gamma_0$$

See how $\Gamma_0$ appears there on the end? Since it's the first term of $\gamma(x)$, subtracting it from $\gamma(x)$ is equivalent to the new EGF term I just folded into the recurrence.

**Analyzing the Right Hand Side (RHS):**

The first portion of the RHS is easy. Note that 

$$ \sum_{n=1}^{\infty} G_n \frac{x^n}{n!} = \overline{g}(x) - G_0 = \overline{g}(x) - \Gamma_0 $$

Conveniently, $- \Gamma_0$ is on both sides of the equation since it is equal to $- G_0$. It cancels.

The second term (the summation) is the tricky part. Remember how $R' = G - RF$? Equivalently we write that in Bell notation as $R_1 = G_0 - F_0R_0$ which is a first-order linear ODE of the form $y'=Q - Py$.

Note how the recurrence has a similar structure with $\Gamma_{\text{n-1}}$ on the RHS having a lower derivative order than $\Gamma_{\text{n}}$ on the left:

$$\underbrace{\Gamma_n}\_{\text{similar to y'}} = G_n - \sum_{k=0}^{n-1} \binom{n}{k} F_k \underbrace{\Gamma_{n-k-1}}\_{\text{similar to y}}$$

Since we already have $\gamma(x)$ (like $y'$) on the LHS, let's see what happens if we try to put $\int_0^x \gamma(t)dt$ (like $y$) on the right.

Recall that integration shifts indices in EGFs:

$$\int_0^x \gamma(t) dt = \sum_{n=0}^{\infty} \Gamma_n \frac{x^{n+1}}{(n+1)!} = \sum_{m=1}^{\infty} \Gamma_{m-1} \frac{x^m}{m!}$$

That's a start. But what exactly do we do with it? That's where the selection process comes into play via the **Coefficient Extraction Operator**, represented in this context by $[x^n]$, or, more formally, $\left[\frac{x^n}{n!}\right]$.

But before we use it, we need to know what expression we're going to use it on and why.

### The Standard Binomial Convolution Formula [^4]

[^4]: This formula is also known as the "Cauchy product formula" for EGFs. Credit where credit is due.

Since you've made it this far, you likely know how binomials relate to Pascal's triangle in the form of $\binom{n}{k}$, or "n choose k."

So, let's address what a "convolution" is. Remember $\Gamma_4$ from the end of the last part?

$$ \Gamma_4 = G_4 - \Gamma_3F - 4\Gamma_2F_1 - 6\Gamma_1F_2 - 4\Gamma_0F_3 $$

See how the subscript on $\Gamma_n$ drops by one in each term as you move from left to right while the one on $F_n$ increases by one in pairwise fashion?

This type of summation series is known as a "convolution." Since it's binomially weighted, it's known as a "binomial convolution."

So, how does the selection operator [...] relate?

Let's say there are two sequences, $a_n$ and $b_n$, with EGFs $A(x)$ and $B(x)$:

$$A(x) = \sum_{n=0}^{\infty} a_n \frac{x^n}{n!} \quad \text{and} \quad B(x) = \sum_{n=0}^{\infty} b_n \frac{x^n}{n!}$$

When we multiply two infinite polynomials, we look for terms that combine to create a specific power of $x$, say $x^n$.

$$A(x)B(x) = \left( a_0 \frac{x^0}{0!} + a_1 \frac{x^1}{1!} + \dots \right) \left( b_0 \frac{x^0}{0!} + b_1 \frac{x^1}{1!} + \dots \right)$$

To get a term with $x^n$, we multiply a term with $x^k$ from the first sum by a term with $x^{n-k}$ from the second sum. (Since exponents add up: $x^k \cdot x^{n-k} = x^n$).

The raw coefficient of $x^n$ in the product is the sum of all such pairs.

Here, the **coefficient extraction operator** is telling us to extract coefficient pairs such that their powers add to n. Hence, only pairs where one has a subscript of $k$ and the other of $n-k$ will be included.

$$[x^n]C(x) = \sum_{k=0}^{n} \left( \frac{a_k}{k!} \right) \times \left( \frac{b_{n-k}}{(n-k)!} \right)$$

Here is the crucial part.

The equation above gives us the raw coefficient of $x^n$. However, an EGF is defined as having coefficients scaled by $\frac{1}{n!}$.

So, by definition, the coefficient of $x^n$ in $C(x)$ must equal $\frac{c_n}{n!}$.

Let's equate the definition with our calculation:

$$\frac{c_n}{n!} = \sum_{k=0}^{n} \frac{a_k}{k!} \frac{b_{n-k}}{(n-k)!}$$

To isolate $c_n$, we multiply both sides of the equation by $n!$:

$$c_n = n! \sum_{k=0}^{n} \frac{a_k b_{n-k}}{k!(n-k)!}$$

Now, let's move the $n!$ inside the summation (since it doesn't depend on $k$):

$$c_n = \sum_{k=0}^{n} \frac{n!}{k!(n-k)!} a_k b_{n-k}$$

Look closely at the fraction inside the sum. That is exactly the definition of the binomial coefficient $\binom{n}{k}$:

$$\binom{n}{k} = \frac{n!}{k!(n-k)!}$$

Then their product $C(x) = A(x)B(x)$ is the EGF for a new sequence $c_n$, where:

$$c_n = \sum_{k=0}^{n} \binom{n}{k} a_k b_{n-k}$$

### The Convolution

Now that we know what the standard binomial convolution formula is, let's use it. 

Recall from earlier:

$$\int_0^x \gamma(t) dt = \sum_{n=0}^{\infty} \Gamma_n \frac{x^{n+1}}{(n+1)!} = \sum_{m=1}^{\infty} \Gamma_{m-1} \frac{x^m}{m!}$$

Let's call the integral $I(x)$

$$I(x) = \sum_{n=1}^{\infty} \Gamma_{n-1} \frac{x^n}{n!}$$

As we saw earlier, we need to convolute $I(x)$ with $\overline{f}(x) = \sum_{n=0}^{\infty} F_n \frac{x^n}{n!}$ to obtain the $F_k\Gamma_{n-k-1}$ convolution, so let's consider $\overline{f}(x)·I(x)$.

By the standard binomial convolution formula established above, 

$$c_n = \sum_{k=0}^{n} \binom{n}{k} a_k b_{n-k} \implies \left[\frac{x^n}{n!}\right] (\overline{f}(x)·I(x)) = \sum_{k=0}^{n-1} \binom{n}{k} F_k \Gamma_{n-k-1}$$

which precisely matches the binomial convolution from the $\Gamma_n$ recurrence,

$$\Gamma_n = G_n - \sum_{k=0}^{n-1} \binom{n}{k} F_k \Gamma_{n-k-1}$$

Because $I(x)$ starts at power $x^1$ (due to integration), it has no constant term. This effectively forces the convolution sum to stop at $n-1$ instead of $n$, matching the recursion limit.

You may need to spend some time looking at this part so that the fact that the right side of Pascal's triangle has been truncated in $\Gamma_n$ can sink in, which is where the $(n-1)$'s come from, so feel free stare for a bit. This is the keystone of the closed form derivation, so give yourself time to process. I know it took me a while to get.


## And Now for Something Completely Differential

Let's put it all together. 

As a recap, 

$$\Gamma_n = G_n - \sum_{k=0}^{n-1} \binom{n}{k} F_k \Gamma_{n-k-1}$$

$$↓↓↓↓$$

$$\sum_{n=1}^{\infty} \Gamma_n \frac{x^n}{n!} = \sum_{n=1}^{\infty} G_n \frac{x^n}{n!} - \sum_{n=1}^{\infty} \frac{x^n}{n!} \sum_{k=0}^{n-1} \binom{n}{k} F_k \Gamma_{n-k-1}$$

$$↓↓↓↓$$

$$\gamma(x) - \Gamma_0 = \overline{g}(x) - \Gamma_0 - \overline{f}(x)·I(x)$$

$$↓↓↓↓$$

$$\gamma(x) = \overline{g}(x) - \overline{f}(x)\int_0^x \gamma(t) dt$$

If we set $\gamma(x) = y'$ and $\int_0^x \gamma(t) dt = y$ then we get

$$y'=\overline{g} - \overline{f}y \implies  y' + \overline{f}y = \overline{g} $$

This is a classical first order ODE of the form $y'+Py=Q$ which is solved using an integrating factor.

### Solving for $y$

The integrating factor that solves for $y$ in this form is $e^{\int P}=e^{\int \overline{f}}$.

If we let $H(x) = \int_0^x f(t) dt$, The integrating factor is $e^{H(x)}$.

We multiply through by the integrating factor and recognize the LHS as the derivative of the factor times $y(x)$,

$$\frac{d}{dx}(y(x) e^{H(x)}) = g(x) e^{H(x)}$$

then integrate both sides,

$$y(x) e^{H(x)} = \int_0^x g(t) e^{H(t)} dt$$

and multiply through by the reciprocal of the integrating factor:

$$y(x) = e^{-H(x)} \int_0^x g(t) e^{H(t)} dt$$

That's it. [^1]

[^1]: That was quick. Anyone looking for a primer (or refresher) on the use of integrating factors in solving first-order ODEs will find that openstax offers a thorough, digestible review here: https://openstax.org/books/calculus-volume-2/pages/4-5-first-order-linear-equations .

### Solving for $\gamma_n$ and $\Gamma_n$

We're looking for $\gamma(x)$ so we can use it to extract coefficients for $\Gamma_n$.

Since $y(x) = \int \gamma(t) dt$, we know that $\gamma(x) = y'(x)$. Differentiating our solution for $y(x)$:

$$ \gamma(x) = \frac{d}{dx} \left( e^{-H(x)} \int_0^x \overline{g}(t) e^{H(t)} dt \right) $$

By the product rule:

$$ \gamma(x) = \left( \frac{d}{dx} e^{-H(x)} \right) \cdot \int_0^x \overline{g}(t) e^{H(t)} dt + e^{-H(x)} \cdot \left( \frac{d}{dx} \int_0^x \overline{g}(t) e^{H(t)} dt \right) $$

Recalling that $\frac{d}{dx} H(x) = \overline{f}(x)$ and using the Fundamental Theorem of Calculus:

$$ = \left( -\overline{f}(x) e^{-H(x)} \right) \int_0^x \overline{g}(t) e^{H(t)} dt + e^{-H(x)} \cdot \left( \overline{g}(x) e^{H(x)} \right) $$

The $e^{-H(x)}$ and $e^{H(x)}$ in the second term cancel out, leaving:

$$ \gamma(x) = \overline{g}(x) - \overline{f}(x) e^{-H(x)} \int_0^x \overline{g}(t) e^{H(t)} dt $$

### Extracting $\Gamma_n$

The whole point of this exercise was to develop an infinite polynomial that we could apply the **coefficient extraction operator** to so we can get the correct terms out of $\gamma(x)$ which we initially defined as

$$\gamma(x) = \sum_{n=0}^{\infty} \Gamma_n \frac{x^n}{n!}$$

Applying the operator to this version of $\gamma(x)$ would be circular logic, so we needed to come up with an expression for it in terms of $F_n$ and $G_n$, which we did: [^2]

$$\Gamma_n = n![x^n]\gamma(x)$$

which can also be written as [^3]

$$\Gamma_n = \left[\frac{x^n}{n!}\right]\gamma(x)$$ 

where

$$\gamma(x) = \overline{g}(x) - \overline{f}(x)e^{-H(x)}\int_0^x \overline{g}(t) e^{H(t)} dt$$
$$\overline{g}(x) = \sum_{n=0}^{\infty} G_n \frac{x^n}{n!}$$
$$\overline{f}(x) = \sum_{n=0}^{\infty} F_n \frac{x^n}{n!}$$

and

$$H(x) = \sum_{n=0}^{\infty} F_n \frac{x^{n+1}}{(n+1)!}$$

[^2]: We use the notation n![x^n] to mean: "extract the coefficient of x^n and multiply it by n!" which effectively cancels out the 1/n! from the EGF definition and leaves us with the raw extracted term.

[^3]: This second form of the coefficient extraction operator acknowledges the series is an EGF and extracts the coefficient "pre-adjusted" for the factorial.

Technically, the closed form is now complete.

## But Wait! There's More!

We've closed the recursion, so mathematicians are happy with how elegantly the formula spills across the page in terms of $G$ and $F$. 

Thing is, being pretty (while it does undoubtedly help) isn't everything.

Being computationally useful? That helps, too.

### The Double Sum

Developing the closed form of the $\Gamma_n$ generator as a double sum is what will allow users to bypass iterative differentiation of $A = h\frac{\text{ln}g}{\text{ln}f}$ in search of $A_n$.

So, how do we set about the recipe for arranging known atomic inputs ($F_n, G_n$) and their associated binomial weights that will produce any $A_n$ without requiring knowledge of $A_{n-1}$?

### Bells, Bells, Bells

Fortunately, turning EGFs into sums using Bell polynomials is a well-known process as I mentioned at the end of the last part.

In general, if

$$C(x) = \sum_{n=0}^{\infty} c_n \frac{x^n}{n!}$$

then

$$\left[ \frac{x^n}{n!} \right] e^{C(x)} = B_n(c_1, c_2, \dots, c_n)$$

where $B_n(c_1, c_2, \dots, c_n)$ represents the set of Bell polynomials applied to the series of coefficients defined by $c_n$. [^5]

[^5]: For those unfamiliar with this extraction identity, I've provided a transparently AI-generated tutorial at **insert link here**. I plan in future to lend my personal voice to the section when time and mental energy allow.

Hmm. Where did $c_0$ go? It's there in the first part and gone in the second.

Usually $c_0$ is set to zero in this context, so the formula begins with $c_1$, allowing the Bell subscripts match the subscripts on $c$. However, for our purposes, $F_0 = F = \frac{f'}{f\text{ln}f}$ so we have to shift the subscripts to begin with the correct coefficient. Otherwise, the Bell polynomials will be attached to the wrong atoms by plus one.

Recall that

$$H(x) = \int_0^x \overline{f}(t)dt = \sum_{n=0}^{\infty} F_n \frac{x^{n+1}}{(n+1)!} = \sum_{m=1}^{\infty} F_{m-1} \frac{x^{m}}{m!}$$

so $H(x)$ already encompasses that shift.

$$\left[ \frac{x^n}{n!} \right] e^{\int_0^x \overline{f}(t)dt} =\left[ \frac{x^n}{n!} \right] e^{H(x)} = B_n(F_0, F_1, \dots, F_{n-1}) = B_n^{+}$$

Since we also have an $e^{-H}$ in the closed form, let's define that as well:

$$\left[ \frac{x^n}{n!} \right] e^{-H(x)} = B_n(-F_0, -F_1, \dots, -F_{n-1}) = B_n^{-}$$

We need to turn $\left[ \frac{x^n}{n!} \right]\gamma(x) = \Gamma_n$ into a double sum, so let's remind ourselves what $\gamma(x)$ is:

$$\gamma(x) = \frac{d}{dx} \left( e^{-H(x)} \int_0^x \overline{g}(t) e^{H(t)} dt \right)$$

Using the expressions we just defined, the coefficients of the integrand $K(t) = g(t)e^{H(t)}$ are the convolution of the sequence $G$ and the sequence $B^+$:

$$\left[ \frac{t^m}{m!} \right] K(t) = \left[ \frac{t^m}{m!} \right] g(t)e^{H(t)} = \sum_{j=0}^{m} \binom{m}{j} G_j B_{m-j}(F_0, \dots, F_{m-j-1}) = K_m$$

Since we are integrating $K(t)$ to find $\int_0^x K(t) dt$, we need to shift the index again.

For any $k \ge 1$, the coefficient of $\frac{x^k}{k!}$ in the integral is the coefficient of degree $k-1$ in the integrand, so the coefficients of the integral are given by $K_{k-1}$:

$$\left[ \frac{x^k}{k!} \right] \int_0^x K(t)dt = K_{k-1} = \sum_{j=0}^{k-1} \binom{k-1}{j} G_j B_{k-j-1}(F_0, \dots, F_{k-j-2})$$

We are looking for $\Gamma_n$, which is defined as the coefficient of $\frac{x^n}{n!}$ in the derivative of the product $e^{-H(x)} \times \int_0^x K(t) dt$.

By the properties of generating functions, extracting the coefficient of $\frac{x^n}{n!}$ from the derivative of a function is equivalent to extracting the coefficient of $\frac{x^{n+1}}{(n+1)!}$ from the function itself, so this time around we're looking for the $(n+1)$-th term of the product:

$$\text{Product}(x) = \left( \sum_{i=0}^{\infty} B_i^- \frac{x^i}{i!} \right) \left( \sum_{k=1}^{\infty} K_{k-1} \frac{x^k}{k!} \right)$$

Luckily for us, we know how to extract this product since we established the Standard Binomial Convolution Formula (a.k.a. the "Cauchy Product Formula") in a prior section:

$$\left[ \frac{x^n}{n!} \right]C(x) = c_n = \sum_{k=0}^{n} \binom{n}{k} a_k b_{n-k} = \sum_{k=0}^{n} \binom{n}{k} b_{n-k} a_k$$

Now all we have to do is apply it to Product($x$) using $n+1$:

$$\left[ \frac{x^n}{n!} \right]\gamma(x) = \Gamma_n = \sum_{k=1}^{n+1} \binom{n+1}{k} B_{n+1-k}^- K_{k-1}$$

If we re-index the summation by setting $m = k-1$ (so that $m$ runs from $0$ to $n$), we obtain the final expression:

$$\Gamma_n =\sum_{m=0}^{n} \binom{n+1}{m+1} B_{n-m}^- K_{m} = \sum_{m=0}^{n} \binom{n+1}{m+1} B_{n-m}(-F_0, \dots, -F_{n-m-1}) \left[ \sum_{j=0}^{m} \binom{m}{j} G_j B_{m-j}(F_0, \dots, F_{m-j-1}) \right]$$

It may seem like I'm playing fast and loose with the indexing to those unfamiliar with turning EGFs into a Bell-polynomial-driven summation (as I was a few weeks ago), but that's the power of power series. Lining up the coefficients like Rockettes just involves shifting them left or right.

Now that $\Gamma_n$ is calculable in terms of $F_n$ and $G_n$ lined up purely in terms of Bell polynomials, the mathematicians aren't the only ones who are satisfied.

Have at it, happy coders and computers.

## Epilogue

It's been quite a journey from that practice problem I made up about five months ago. It just goes to show that setting math problems for yourself is generally a _flat-out crazy_ thing to do. Much luck to anyone who tries.

Many thanks to Copilot and Gemini for being my tutor/research grunt/productivity boosters.

Thanks also to my understanding family who were clearly weirded out by my fixation on messing around in Desmos while scribbling lengthy differential algebra into notebooks late nights while on a beach vacation around New Year's.

In particular, thanks to my loving wife, Bonnie, whose patience with my months-long obsession appears to have known no bounds. [^6]

[^6]: I strongly suspect appearances were deceiving. ;-)

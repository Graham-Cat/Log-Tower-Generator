# The Weight of a Kernel

How much does a kernel weigh? When it comes to calculating $\Gamma_n$, turns out it gets heavier and heavier as $n$ gets bigger.

## Weighted Holography

Remember back in Part 2 when I mentioned the **weighted holography** visible in successive $h$-coefficients and... never mentioned it again?

Until now?

Time to snip that dangling thread.

Now that we're talking about reducing processor load instead of raw theory, calculating the homogenous F-kernels that are the same in the F-sector and the G-sector (i.e., the $G_n$ -coefficients _within_ the $h_n$ -coefficients) becomes critical. Doing so makes certain that we won't be bogging down processors with redundant tasks.

Let's take a look at that waterfall diagram again, this time, with all references to $G_n$ **and** $-RF$ deleted, leaving only the raw F-terms.

### The Recursive "Spine" of the F-kernel of $R_7$

```text

(
      -F(
            -F(   <------------------------------------------------------------------------------┐
                  -F(   <----------------------------------------------------------┐             |
                        -F(   <----------------------------------------┐           |             |
                              -F(   <---------------------┐            |           |             |
                                    -F)   <--- F-kernel_1 | F-kernel_2 |           |             |
                              -2F1)   <-------------------┘            |F-kernel_3 |             |
                        -3F1(                                          |           |             |
                              -F)   <--- F-kernel_1                    |           |             |
                        -3F2)   <--------------------------------------┘           | F-kernel_4  |
                  -4F1(                                                            |             | 
                        -F(   <---------------------┐                              |             |
                              -F)   <--- F-kernel_1 | F-kernel_2                   |             |
                        -2F1)   <-------------------┘                              |             |
                  -6F2(                                                            |             |
                        -F)   <--- F-kernel_1                                      |             |
                  -4F3)   <--------------------------------------------------------┘             | F-kernel_5
            -5F1(                                                                                |
                  -F(   <----------------------------------------┐                               |
                        -F(   <---------------------┐            |                               |
                              -F)   <--- F-kernel_1 | F-kernel_2 |                               |
                        -2F1)   <-------------------┘            | F-kernel_3                    |
                  -3F1(                                          |                               |
                        -F)   <--- F-kernel_1                    |                               |
                  -3F2)   <--------------------------------------┘                               |
            -10F2(                                                                               |
                  -F(   <---------------------┐                                                  |
                        -F)   <--- F-kernel_1 | F-kernel_2                                       |
                  -2F1)   <-------------------┘                                                  |
            -10F3(                                                                               |
                  -F)   <--- F-kernel_1                                                          |
            -5F4)   <----------------------------------------------------------------------------┘
      -6F1(
            -F(   <-----------------------┐
                  -F(                     |
                        -F(               |
                              -F)         |
                        -2F1)             |
                  -3F1(                   |
                        -F)               |
                  -3F2)                   | F-kernel_4
            -4F1(                         |
                  -F(                     |
                        -F)               |
                  -2F1)                   |
            -6F2(                         |
                  -F)                     |
            -4F3)   <---------------------┘
      -15F2(
            -F(
                  -F(
                        -F)
                  -2F1)
            -3F1(
                  -F)
            -3F2)
      -20F3(
            -F(
                  -F)
            -2F1)
      -15F4(
            -F)
      -6F5)

```

Since this is the last isolation we can perform on this waterfall diagram, let's head straight to the end of the Greek alphabet and call the F-kernel $\Omega_n$.

A close inspection of the F-kernels above yields:

$$\Omega_1 = -F_0$$
$$\Omega_2 = -2F_1-F_0\Omega_1$$
$$\Omega_3 = -3F_2-3F_1\Omega_1-F_0\Omega_2$$
$$\Omega_4 = -4F_3-6F_2\Omega_1-4F_1\Omega_2-F_0\Omega_3$$
$$\Omega_5 = -5F_4-10F_3\Omega_1-10F_2\Omega_2-5F_1\Omega_3-F_0\Omega_4$$

or, more succinctly,

$$\Omega_n = -\sum_{k=1}^{n} \binom{n}{k}F_{n-k}\Omega_{k-1}$$

Note that $\Omega_0$ is defined as 1. This distinction becomes important for consistent application to all $A_n$, including $A_1 = R(h_1-hF)+hG$ where the $hG$ -coefficient is unity.

### Defining the Weighted Holographs

Let's take a look at the first four $\Omega_n$ as they appear in the canonical format.

* $\Omega_1 = -F_0$
* $\Omega_2 = -\left(2F_1 - F^2 \right)$
* $\Omega_3 = -\left(3F_2 - 5F_1 F + F^3 \right)$
* $\Omega_4 = -\left(4F_3 - 9F F_2 - 8F_1^2 + 9F_1F^2 - F^4 \right)$

If you head back to Part 2, you'll see that these represent the G-coefficient _within_ the h-coefficient. Look at the very tail end of all of the $A_{nG}$ 's under **Holography of R Rears its Head** and you'll see these.

You'll also see them at the tail ends of the F-sectors. They're the same between the F-sector and the G-sector since these $\Omega_n$ are homogeneously populated by forms of $F_n$. No $G_n$ allowed.

I'll put them here for you again. Look closely. Feel free to slide the bar at the bottom back and forth. Try matching up things that look similar, but aren't quite the same. In particular, line up the h-coefficients of $A_{4G}$ and $A_{5G}$

* $A_{1G} = hG$
* $A_{2G} = 2h_1G + h(G_1 - GF)$
* $A_{3G} = 3h_2G + 3h_1(G_1 - GF) + h(G_2 - G_1F - G(2F_1 - F^2))$
* $A_{4G} = 4h_3G + 6h_2(G_1 - GF) + 4h_1(G_2 - G_1 F - G(2F_1 - F^2)) + h(G_3 - G_2 F - G_1(3F_1 - F^2) - G(3F_2 - 5F_1 F + F^3))$
* $A_{5G} = 5h_4G + 10h_3(G_1 - GF) + 10h_2(G_2 - G_1 F - G(2F_1 - F^2)) + 5h_1(G_3 - G_2 F - G_1(3F_1 - F^2) - G(3F_2 - 5F_1 F + F^3)) + h(G_4 - G_3 F - G_2(4F_1 - F^2) - G_1(6F_2 - 7F F_1 + F^3) - G(4F_3 - 9F F_2 - F_1(8F_1 - 9F^2) - F^4))$

See how $\Omega_2$ appears to evolve? When it appears in the h-coefficient of $A_{3G}$, it's $-(2F_1 - F^2)$. In the h-coefficient of $A_{4G}$, it looks like it's morphed into $-(3F_1 - F^2)$. In the h-coefficient of $A_{5G}$ it's advanced to $-(4F_1 - F^2)$.

You likely noticed the same thing with $-(3F_2 - 5F_1 F + F^3)$ in $A_{4G}$ and $-(6F_2 - 7F_1F + F^3)$ in $A_{5G}$.

What you're seeing is **binomially-weighted holography**. The skeleton of an expression appears in successive derivatives, but the weights change.

You can see there's information we already know going into creating the h-coefficient of the derivative before we start making it, but teasing out precisely what's happening gets murky because of the simplification.

So, again, we un-simplify.

### 'Tis a Gift to Be Un-simple

Since we seem to have multiple versions of each individual $\Omega_n$, let's start labelling them. The information we currently have about them is

1) which $n$ designation they have, and
2) in which derivative of $A=h\frac{\text{ln}g}{\text{ln}f}$ they appear,

so let's use those numbers. Since this whole repo is about $A_n$ we'll let the derivative designation remain $n$ and we'll instead start referring to $\Omega_n$ as $\Omega_m$.

Let's start with something we've already talked about, the skeleton of $\Omega_2 = -(2F_1 - F^2)$. We know that one first appears in the third derivative, so we'll call it $\Omega_{2,3} = \Omega_{m,n}$. Let's go ahead and label all the ones we've seen so far:

$$\Omega_{2,3} = -(2F_1 - F^2)$$
$$\Omega_{2,4} = -(3F_1 - F^2)$$
$$\Omega_{2,5} = -(4F_1 - F^2)$$

The pattern here is obvious; the binomial weight of $F_1$ is $n-1$.

The next doesn't become obvious until I give you a look-ahead at $\Omega_{3,6}$, so let's do that even though you haven't seen it yet.

$$\Omega_{3,4} = -(3F_2 - 5F_1 F + F^3)$$
$$\Omega_{3,5} = -(6F_2 - 7F_1 F + F^3)$$
$$\Omega_{3,6} = -(10F_2 - 9F_1 F + F^3)$$

Students of combinatorics will immediately recognize the weights on the left as an excerpt from the "choose 2" column of Pascal's triangle. Now that we have this context, they'll also see the "choose 1" column in the $\Omega_2$ series:

```text
               1 <--- Top of Choose 0
             1   1 <--- Top of Choose 1
           1   2   1 <--- Top of Choose 2
         1   3   3   1 <--- Top of Choose 3
       1   4   6   4   1
     1   5  10  10   5   1
   1   6  15  20  15   6   1

```

The 5, 7, 9 pattern is obviously an addition of 2 for each successive derivative, but that doesn't give us enough information to figure out how to encode mathematical instructions that relate to the Pascal. For that, we'll need to go one deeper and un-simplify.

$$\Omega_{4,5} = -(4F_3 - 9F F_2 - F_1(8F_1 - 9F^2) - F^4)$$
$$\Omega_{4,6} = -(10F_3 - 16F F_2 - F_1(15F_1 - 12F^2) - F^4)$$
$$\Omega_{4,7} = -(20F_3 - 25F F_2 - F_1(24F_1 - 15F^2) - F^4)$$

See how the weights climb? Now we're walking down the column of "choose 3" on the left and the rest are climbing with predictable patterns, but it's not immediately obvious how they relate to the triangle.

Let's head back to $\Omega_2$ and present it slightly differently, this time in **recursive** terms. Make sure to note the sign change as we factor out $\Omega_1 = -F$

$$\Omega_{2,3} = -(2F_1 + F(-F)) = -(2F_1 + F\Omega_1)$$
$$\Omega_{2,4} = -(3F_1 + F(-F)) = -(3F_1 + F\Omega_1)$$
$$\Omega_{2,5} = -(4F_1 + F(-F)) = -(4F_1 + F\Omega_1)$$

When we try to do the same for $\Omega_3$, things begin to clear up as the triangle comes into focus.

$$\Omega_{3,4} = -(3F_2 - 5F_1 F + F^3) = -(3F_2 + 3F_1\Omega_1 + F\Omega_{2,3})$$
$$\Omega_{3,5} = -(6F_2 - 7F_1 F + F^3) = -(6F_2 + 4F_1\Omega_1 + F\Omega_{2,4})$$
$$\Omega_{3,6} = -(10F_2 - 9F_1 F + F^3) = -(10F_2 + 5F_1\Omega_1 + F\Omega_{2,5})$$

Now we see it clearly. We're just looking at truncated sections of Pascal's triangle when we see it from the recursive perspective.

You may have noticed that I started adding the {m,n} notation here on the $\Omega_2$ 's. It was necessary to have those $n$ 's climb with the $\Omega_{3}$ 's on the left to have the algebra work out. From now on, I'll be adding the {n} designations for clarity. [^1]

Also note that the $\Omega_0$ 's are left out of the leading terms to declutter since they're all just equal to 1.

[^1]: Feel free to satisfy yourself that the algebra works in this section. Trust me, I checked.

Let's go up one more level for the sake of completeness: [^2]

$$\Omega_{4,5} = -(4F_3 - 9F F_2 - F_1(8F_1 - 9F^2) - F^4) = -(4F_3 + 6F_2\Omega_{1,2} + 4F_1\Omega_{2,3} + F\Omega_{3,4})$$
$$\Omega_{4,6} = -(10F_3 - 16F F_2 - F_1(15F_1 - 12F^2) - F^4) = -(10F_3 + 10F_2\Omega_{1,3} + 5F_1\Omega_{2,4} + F\Omega_{3,5})$$
$$\Omega_{4,7} = -(20F_3 - 25F F_2 - F_1(24F_1 - 15F^2) - F^4) = -(20F_3 + 15F_2\Omega_{1,4} + 6F_1\Omega_{2,5} + F\Omega_{3,6})$$

Now we have straightforward encoding. The binomial convolutions are obvious.

[^2]: Even though it's not strictly necessary, you likely noticed that I've started adding {m,n} desginations for Omega_1's (even though they're all equal to -F) to get you ready for the next section.

## That's Cache!

The real processor savings will come with the caching method that the $\Omega_{m,n}$ recursion provides us with the opportunity to implement.

Now that we are grounded in the structure of $\Omega_{m,n}$, let's do a test run on $A_5$ to see how everything plays out.

First, we recursively define all required $\Omega_{m,n}$ by starting with $m=0$:

$$\Omega_{0,1} = \Omega_{0,2} = ... = \Omega_{0,5} = 1$$

or

$$\Omega_{0,n} = 1$$

Then we do the same with $m=1$:

$$\Omega_{1,2} = \Omega_{1,3} = ... = \Omega_{1,5} = -F_0\Omega_{0,n-1} = -F_0$$

or

$$\Omega_{1,n} = -\binom{n-1}{0}F_0\Omega_{0,n}$$

Now we start on the "choose 1" column of Pascal's triangle:

$$\Omega_{2,3} = -(2F_1\Omega_{0,1} + F\Omega_{1,2})$$
$$\Omega_{2,4} = -(3F_1\Omega_{0,2} + F\Omega_{1,3})$$
$$\Omega_{2,5} = -(4F_1\Omega_{0,3} + F\Omega_{1,4})$$

or

$$\Omega_{2,n} = -\left(\binom{n-1}{1}F_1\Omega_{0,n-2} + \binom{n-1}{0}F_0\Omega_{1,n-1}\right)$$

Then we hit "choose 2":

$$\Omega_{3,4} = -(3F_2\Omega_{0,1} + 3F_1\Omega_{1,2} + F\Omega_{2,3})$$
$$\Omega_{3,5} = -(6F_2\Omega_{0,2} + 4F_1\Omega_{1,3} + F\Omega_{2,4})$$

or

$$\Omega_{3,n} = -\left(\binom{n-1}{2}F_2\Omega_{0,n-3} + \binom{n-1}{1}F_1\Omega_{1,n-2} + \binom{n-1}{0}F\Omega_{2,n-1}\right)$$

Then "choose 3":

$$\Omega_{4,5} =  -(4F_3\Omega_{0,1} + 6F_2\Omega_{1,2} + 4F_1\Omega_{2,3} + F\Omega_{3,4})$$

or

$$\Omega_{4,n} = -\left(\binom{n-1}{3}F_3\Omega_{0,n-4} + \binom{n-1}{2}F_2\Omega_{1,n-3} + \binom{n-1}{1}F_1\Omega_{2,n-2} + \binom{n-1}{0}F\Omega_{3,n-1}\right)$$

each successive step of the way using the $\Omega_n$ 's that came before.

Computer scientists will recognize this process as **memoization**. It boosts performance by preventing repeated, taxing function calls.

Since the structure of the recursion is staring us in the face, let's generalize it:

$$\Omega_{m,n} = -\sum_{k=0}^{m-1}\binom{n-1}{m-k-1}F_{m-k-1}\Omega_{k,k+n-m}$$

and then clean up by letting $j = m - k - 1$:

$$\Omega_{m,n} = - \sum_{j=0}^{m-1} \binom{n-1}{j} F_j \Omega_{m-1-j, \ n-1-j}$$

Now that we have our $\Omega_{m,n}$ "memoized", we use the cache to create $A_5$.

First, we create $A_{5G}$:

$$(5h_4G_0\Omega_{0,1}+10h_3(G_1\Omega_{0,2}+G_0\Omega_{1,2})+10h_2(G_2\Omega_{0,3}+G_1\Omega_{1,3}+G_0\Omega_{2,3})+5h_1(G_3\Omega_{0,4}+G_2\Omega_{1,4}+G_1\Omega_{2,4}+G_0\Omega_{3,4})+h_0(G_4\Omega_{0,5}+G_3\Omega_{1,5}+G_2\Omega_{2,5}+G_1\Omega_{3,5}+G_0\Omega_{4,5}))$$

or, more succinctly,

$$\sum_{k=0}^{5-1}\binom{5}{k}h_{k}\sum_{m=0}^{5-k-1}G_{5-k-1-m}\Omega_{m,n-k}$$

As you can see from where I put the 5's, the generalized formula for $A_{nG}$ is

$$A_{nG} = \sum_{k=0}^{n-1}\binom{n}{k}h_{k}\sum_{m=0}^{n-k-1}G_{n-k-1-m}\Omega_{m,n-k}$$

Then, simply mapping $G \mapsto F$ gives us $A_{nF}$, at which point we slot both into the canonical form of

$$A_n = R(h_n - A_{\text{nF}}) + A_{\text{nG}}$$

and $A_n$ is complete.

If you compare this new $A_{nG}$ generator to our canonical $A_{nG}$ generating function:

$$A_{nG} = \underbrace{\sum_{k=0}^{n-1} \binom{n}{k} h_k}\_{h_k \text{ portion}} \underbrace{\Gamma_{n-k-1}}_{\Gamma_n \text{ portion}}$$

$$A_{nG} = \underbrace{\sum_{k=0}^{n-1}\binom{n}{k}h_{k}}\_{h_k \text{ portion}}\underbrace{\sum_{m=0}^{n-k-1}G_{n-k-1-m}\Omega_{m,n-k}}_{\Gamma_n \text{ portion}}$$

You'll see we have a new expression for $\Gamma_n$ in the form of

$$\Gamma_{n-k-1} = \sum_{m=0}^{n-k-1}G_{n-k-1-m}\Omega_{m,n-k}$$

Or, if we allow the sum to run from 0 to $n$ instead of $n-k-1$ to put it on comparable terms to our old expression for $\Gamma_n$,

*Previous expression*

$$\Gamma_n = G_n - \sum_{k=0}^{n-1} \binom{n}{k} F_k \Gamma_{n-k-1}$$

*New Expression*

$$\Gamma_{n} = \sum_{m=0}^{n}G_{n-m}\Omega_{m,n+1}$$

## Are We There Yet, Papa Smurf?

Not far now.

We've now optimized the generator by teasing out the pure $-F$ drag, but haven't yet closed our new recursion, so let's get to it.

### Closing Time Again

If we were just closing the first $\Omega_n$ we derived from the waterfall diagram, it would be easy.

Let's do a warp-speed close on that one just to warm up. [^3]

[^3]: It's not just for warming up.

This part assumes you've absorbed the previous **Closing Time** section, so it will be (very) short on exposition.

> [!WARNING]
> Full steam ahead!

Recall that our first $\Omega_n$ recursion was 

$$\Omega_n = -\sum_{k=1}^{n} \binom{n}{k}F_{n-k}\Omega_{k-1}$$

Let's define the necessary EGFs.

$$\overline{o}(x) = \sum_{n=0}^{\infty}\Omega_n\frac{x^n}{n!}$$

$$\overline{f}(x) = \sum_{n=0}^{\infty}F_n\frac{x^n}{n!}$$

Now apply $\frac{x^n}{n!}$ and sum from 1 to $\infty$ on both sides of the recursion.

$$\sum_{n=1}^{\infty}\Omega_n\frac{x^n}{n!} = - \sum_{n=1}^{\infty}\frac{x^n}{n!}\sum_{k=1}^{n}\binom{n}{k}F_{n-k}\Omega_{k-1}$$

The left hand side is:

$$\sum_{n=1}^{\infty}\Omega_n\frac{x^n}{n!} = \overline{o}(x) - 1$$

Note that the LHS is $\overline{o}(x) - 1$ because the sum starts at $n=1$, leaving behind the $\Omega_0=1$ term.

For the right hand side, consider

$$I(x) = \int_{0}^{x} \overline{o}(t)dt = \int_{0}^{x} \sum_{n=0}^{\infty}\Omega_n\frac{x^n}{n!} = \sum_{k=1}^{\infty}\Omega_{k-1}\frac{x^{k}}{k!}$$

Then, by the **Binomial Convolution Formula** (a.k.a, the Cauchy Product Formula)

$$\left[\frac{x^n}{n!}\right]\overline{f}(x)I(x) = \left[\frac{x^n}{n!}\right]\left(\sum_{n=0}^{\infty}F_n\frac{x^n}{n!}\right) \times \left(\sum_{k=1}^{\infty}\Omega_{k-1}\frac{x^{k}}{k!}\right) = \sum_{k=1}^{n}\binom{n}{k}F_{n-k}\Omega_{k-1}$$

Which matches the right side of our recursion (sans the negative sign), so

$$\overline{o}(x) - 1 = -\overline{f}(x)I(x) = -\overline{f}(x)\int_{0}^{x} \overline{o}(t)dt$$

Set $\overline{o}(x) = y'(x)$, so $y(x) = \int_{0}^{x} \overline{o}(t)dt$ and therefore

$$y' - 1 = - \overline{f}y \implies y' + \overline{f}y = 1 $$

The integrating factor that solves for $y$ in this form is $e^{\int P}=e^{\int \overline{f}}$.

If we let $H(x) = \int_0^x \overline{f}(t) dt$, the integrating factor is $e^{H(x)}$, so

$$ \frac{d}{dx}\left(ye^H\right)=e^H \implies ye^H = \int e^H \implies y=e^{-H} \int e^H = \int \overline{o} $$

then

$$ \overline{o} = \frac{d}{dx}\left(e^{-H}\int e^H\right) = -\overline{f}e^{-H}\int e^H+e^{-H}e^H$$

so

$$ \overline{o} = 1-\overline{f}e^{-H}\int e^H$$

Therefore

$$ \Omega_n = n!\left[x^n\right]\overline{o} $$

Phew.

Note that if we look back at the formula for $\overline{\gamma}$,

$$\overline{\gamma} = \overline{g} - \overline{f} e^{-H} \int \overline{g} e^{H} $$

$\overline{o}$ is just $\overline{\gamma}$ with the $\overline{g}$ 's removed and replaced by ones, which makes sense, because that's almost literally what we did in the waterfall diagram using MS Word's find and replace function.

Unfortunately, this closed form is not particularly useful except as an exemplar. We know that $\overline{o}$ is a special case that can only extract the G-coefficient inside the h-coefficient of the G-sector, and, by extension, its analog in the F-sector, so it can't do much else except elucidate structure and clue us into how to attack the final closed form of $\Omega_{m,n}$.

### It Takes Two

We've seen how to close $\Omega_n$, but the second subscript in $\Omega_{m,n}$ complicates matters.

We do, however, know a few things about closing recursions like $\Omega$;

1) it's a recursion, so we know EGFs can play a role in lining up our terms;
2) recursions can also be solved with differential or integration methods when using EGFs because they reliably shift our terms left or right; and
3) we can take **partial derivatives** of functions with two or more salient variables.

That last bullet point brings our path to a solution into focus.

**Bivariate EGFs** can be used to package a two-dimensional **dependency graph** (i.e., where every new value relies on previously computed ones) into a single object, which is what we have with the subscripts $m$ and $n$. Instead of using the EGFs above that only select on $x^n$, we'll be creating ones that use both $x$ and $y$ to trace $n$ **and** $m$ simultaneously.

Let's see what it looks like when we apply this technique to $\Omega_{m,n}$:

$$\overline{\omega}(x, y) = \sum_{m=0}^{\infty} \sum_{n=0}^{\infty} \Omega_{m,n} \frac{x^n}{n!} y^m$$

Now we're looking at a double sum, one for $m$ and one for $n$, with two corresponding variables, $x$ and $y$, that packages the entire infinite 2-D grid of possible $\Omega_{m,n}$ 's. Since we see that we have $\frac{x^n}{n!}$ and $y^m$ to play with, let's choose what to do with each one strategically.

1) We've seen $\frac{x^n}{n!}$ do well with binomial convolutions and $n$ chooses rows binomially in our recursion, so it looks like a good choice to be paired with the factorial in the denominator.
2) The other one (i.e., $y^m$) is the only term we have left, so let's try using that variable to track $m$ and see how it goes.

Let's take a look at the recursion again so we can plan our attack:

$$\Omega_{m,n} = - \sum_{j=0}^{m-1} \binom{n-1}{j} F_j \Omega_{m-1-j, \ n-1-j}$$

See that $n-1$ in the binomial? That's exactly what happens when one takes a derivative of a power series.

$$\frac{d}{dx} C(x) = \frac{d}{dx} \sum_{n=0}^{\infty} c_n \frac{x^n}{n!} = \sum_{n=0}^{\infty} nc_n \frac{x^{n-1}}{n!} = \sum_{n=0}^{\infty} c_n \frac{x^{n-1}}{(n-1)!}$$

So let's multiply both sides by $\frac{x^{n-1}}{(n-1)!}y^m$ while summing them over all $m$ and $n$ and see what it looks like.

$$\sum_{m=0}^{\infty} \sum_{n=0}^{\infty}\Omega_{m,n}\frac{x^{n-1}}{(n-1)!}y^m = - \sum_{m=0}^{\infty} \sum_{n=0}^{\infty}\frac{x^{n-1}}{(n-1)!}y^m\sum_{j=0}^{m-1} \binom{n-1}{j} F_j \Omega_{m-1-j, \ n-1-j}$$

Hmm. Looks intimidatingly large. Let's break it down.

The left hand side looks like the derivative of a power series, but where only $x$ has been subjected to the derivative operator. We know that as a **partial derivative with respect to $x$**.

$$\text{LHS} = \sum_{m=0}^{\infty} \sum_{n=0}^{\infty}\Omega_{m,n}\frac{x^{n-1}}{(n-1)!}y^m = \frac{\partial}{\partial x} \sum_{m=0}^{\infty} \sum_{n=0}^{\infty}\Omega_{m,n}\frac{x^{n}}{(n)!}y^m = \frac{\partial}{\partial x} \overline{\omega}(x,y)$$

Well, that was quick. Now the entire LHS is simply the partial derivative of $\overline{\omega}(x,y)$ with respect to $x$.

The RHS looks like a huge jumble of symbols, so let's rearrange a bit to combine like objects. Those factorials we just multiplied by don't depend on $j$, so they can move inside the inner sum:

$$- \sum_{m=0}^{\infty} \sum_{n=0}^{\infty}\frac{x^{n-1}}{(n-1)!}y^m\sum_{j=0}^{m-1} \binom{n-1}{j} F_j \Omega_{m-1-j, \ n-1-j} = - \sum_{m=0}^{\infty} \sum_{n=0}^{\infty}y^m\sum_{j=0}^{m-1} \binom{n-1}{j} \frac{x^{n-1}}{(n-1)!} F_j \Omega_{m-1-j, \ n-1-j}$$

We know what $\binom{n-1}{j} = \frac{(n-1)!}{j!(n-1-j)!}$, so let's use that and manipulate powers by adding and subtracting $j$:

$$\binom{n-1}{j} \frac{x^{n-1}}{(n-1)} = \frac{(n-1)!}{j!(n-1-j)!}·\frac{x^{n-1}}{(n-1)!} = \frac{x^j}{j!}·\frac{x^{n-1-j}}{(n-1-j)!}$$

Suddenly, we have objects that we can attach to $F_j$ and $\Omega_{m-1-j, \ n-1-j}$:

$$ RHS = - \sum_{m=0}^{\infty} \sum_{n=0}^{\infty}y^m\sum_{j=0}^{m-1} \left[\left(F_j\frac{x^j}{j!}\right) \left(\Omega_{m-1-j,n-1-j}\frac{x^{n-1-j}}{(n-1-j)!}\right)\right]$$

We're almost there. All we have left to do is move that $y^m$ inside the inner sum. But how?

If we manipulate powers again, we see that:

$$y^m = y^1 \cdot y^{m-1} = y \cdot y^j \cdot y^{m-1-j}$$

Now we can move $y$ inside the sum and match up powers with indices:

$$ RHS = - \sum_{m=0}^{\infty} \sum_{n=0}^{\infty}\sum_{j=0}^{m-1} \left[\left(yF_j\frac{x^j}{j!}y^j\right) \left(\Omega_{m-1-j,n-1-j}\frac{x^{n-1-j}}{(n-1-j)!}y^{m-1-j}\right)\right]$$

This manipulation of $y^m$ clearly exposes the RHS as a convolution of $y\overline{f}(x,y)$ and $\overline{\omega}(x,y)$.

Putting LHS and RHS together, we get:

$$\frac{\partial}{\partial x} \overline{\omega}(x,y) = -y\overline{f}(x,y)\overline{\omega}(x,y) + \underbrace{e^x}_{?!?}$$

Wait. $e^x$? Where'd that come from?

It comes from the boundary condition.

Our recursion works perfectly for $m \ge 1$, matching the derivative (LHS) to the previous term (RHS). However, for the row $m=0$, the recursion tries to look back at $m=-1$, which is empty (0).

In reality, the $m=0$ row exists as an identity row where every $\Omega_{0,n} = 1$, and the derivative of this identity row is $\frac{\partial}{\partial x} \sum \frac{x^n}{n!} = e^x$.

Since the RHS (recursion) produces 0 for this row, but the LHS (reality) contains $e^x$, we must manually add $e^x$ to the equation to balance the scales.

So,

$$\frac{\partial}{\partial x} \overline{\omega}(x,y) = \underbrace{e^x}_{\text{base case}} - y\overline{f}(x,y)\overline{\omega}(x,y)$$

### And Now For Something Even More Completely Differential

Now we have our linear first-order _partial_ differential equation that can be solved using an integrating factor.

$$\frac{\partial \overline{\omega}}{\partial x} + y \overline{f}(xy) \overline{\omega} = e^x$$

Here, the integrating factor is

$$\mathcal{H}(z) = \int_0^z \overline{f}(t) dt$$

Whoa. Where'd that extra $y$ at the beginning go?

Let's take it a bit slower:

$$\mathcal{H}(x,y) = \int y \overline{f}(xy) dx$$

That's a better start. If we define the inner variable as $z = xy$ and take the derivative with respect to $x$ of both sides,

$$dz = y \cdot dx \quad \Rightarrow \quad dx = \frac{dz}{y}$$

then

$$\mathcal{H}(z) = \int y\overline{f}(z)\frac{dz}{y} = \int \overline{f}(z)$$

Now we take it over the (real) finish line.

Multiply through by the integrating factor we just established:

$$\frac{\partial}{\partial x} \left( \overline{\omega} \cdot e^{\mathcal{H}(xy)} \right) = e^x \cdot e^{\mathcal{H}(xy)}$$

Integrate both sides from $0$ to $x$:

$$\int_0^x \frac{\partial}{\partial t} \left( \overline{\omega}(ty) \cdot e^{\mathcal{H}(ty)} \right) = \left. \left( \overline{\omega}(ty) \cdot e^{\mathcal{H}(ty)} \right) \right|\_{0}^{x} = \overline{\omega}(x, y) e^{\mathcal{H}(xy)} - \underbrace{\overline{\omega}(0,y)}\_{1} \underbrace{e^{\mathcal{H}(0)}}_{1} = \int_0^x e^t e^{\mathcal{H}(ty)} dt$$

So, the **Final Bivariate Closed Form** becomes

$$\overline{\omega}(x, y) = e^{-\mathcal{H}(xy)} \left( 1 + \int_0^x e^{t + \mathcal{H}(ty)} dt \right)$$

The $\Omega$ grid is now successfully **closed**.

$\mathcal{H}(xy)$ represents the "accumulated drag" of the system, or, in other words, the "cost" of taking derivatives of a logarithmic function with a variable base, $\text{ln}f$.

We now have proven that the interaction between the identity ($e^x$) and the base function ($\overline{f}$) generates every single $\Omega_{m,n}$ coefficient and that the " $\Omega$ kernel" is mathematically consistent and stable for all derivatives to infinity.

## Epilogue

It's been quite a journey from that practice problem I made up about five months ago. It just goes to show that setting math problems for yourself is generally a _flat-out crazy_ thing to do. Much luck to anyone who tries.

Many thanks to Copilot and Gemini for being my tutors/research grunts/productivity boosters.

Thanks also to my understanding family who were clearly weirded out by my fixation on messing around in Desmos while scribbling lengthy differential algebra equations into notebooks late nights while on a beach vacation around New Year's.

In particular, thanks to my loving wife, Bonnie, whose patience with my months-long obsession appears to have known no bounds.


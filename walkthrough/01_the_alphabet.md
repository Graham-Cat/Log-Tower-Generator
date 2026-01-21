# Part 1: The Practice Problem & The Alphabet

> *"I did a silly thing; I made a practice problem for myself... looking at functions more like Lego blocks that snap together."*

## On a Whim
In August 2025, I was reviewing calculus with a specific goal: I wanted to treat functions ($f$, $g$) as individual objects rather than just processes applied to $x$ to see how they cobbled together.

I needed practice with derivatives, logarithm rules, and the chain rule, so I asked:

**"What is the first derivative of $\log_f(g)$?"**

Then, realizing I also needed experience with exponents in logarithms, I set $g$ to the power of $h$:

$$A(x) = \log_{f(x)}(g(x)^{h(x)})$$

and set about finding the first and second derivatives.

I figured, "How hard could it be?"

Lol. Silly summer 2025 me.

## Step 1: The First Derivative ($A_1$)
To make $A$ differentiable, I first converted it to natural logs using the change-of-base formula, then separated the exponent, turning the tower of powers into a product of quotients:

$$ A = h \frac{\ln g}{\ln f} $$

The goal was to find $A'$ (or $A_1$ in Bell notation). I applied the standard Product Rule and Quotient Rule.

1.  **Differentiating the Quotient** $\left( \frac{\ln g}{\ln f} \right)$:

$$\frac{d}{dx}\left( \frac{\ln g}{\ln f} \right) = \frac{\frac{g'}{g}\ln f - \ln g \frac{f'}{f}}{(\ln f)^2}$$

2.  **Splitting the Terms:**
I noticed the denominator $(\ln f)^2$ could be split to simplify the expression.
    
$$= \frac{g'}{g \ln f} - \frac{\ln g}{\ln f} \left( \frac{f'}{f \ln f} \right)$$

3.  **The "Modules" ($F$ and $G$):**
At this early stage (Day 1) wasn't looking for a new theorem, but two distinct "clumps" of terms stood out. They were complex, but acted like single units, so I isolated them:
    
* **The Base Module:** $F = \frac{f'}{f \ln f}$
* **The Input Module:** $G = \frac{g'}{g \ln f}$

Substituting these back into the quotient derivative, I found a clean identity for the derivative of the log-ratio:
    
$$\frac{d}{dx}\left( \frac{\ln g}{\ln f} \right) = G - \left( \frac{\ln g}{\ln f} \right)F$$

If we define the log-ratio as $R = \frac{\ln g}{\ln f}$, then the identity becomes:[^1]

$$ R' = G - RF $$

[^1]: Students of advanced calculus will recognize this identity as a first-order differential equation of the form y' + P(x)y = Q(x) where R = y, F = P(x), and G = Q(x). Its structure becomes important while developing the closed form of the recursion.

### The First Checkpoint: Emerging Structure
When I substituted back into the full product rule for $A$, two ways of looking at the derivative seemed to highlight different aspects of the function's architecture:

$$A_1 = \underbrace{R'h + Rh'}_{\text{Structural Form}} = \underbrace{R(h' - hF) + hG}_{\text{Canonical Form}}$$

When using the identity $R'=G-RF$ and the initial equation $A = Rh$, the structural form[^2] expands to 

$$A_1 = \underbrace{hG - AF + \frac{A}{h}h'}_{\text{Structural Form}} = \underbrace{R(h' - hF) + hG}_{\text{Canonical Form}}$$

[^2]: Note that this form rearranges to A' + (F - h'/h)A = hG which is also a first order differential equation of the form y' + P(x)y = Q(x), this time with h as a passenger.

* **The Structural Form ($R'h + Rh'$):** This form treats $A$ as a simple product of $h$ and $R$, foreshadowing the "holographic" nature of the higher derivatives (where $h$ is a passenger).
* **The Canonical Form ($R(\dots) + G\dots$):** This form groups the terms by $R$ and $G$. Even here, at $n=1$, we can see the prototype of the final generator:
    $$A_1 = R_0(h_1 - \text{F-sector}) + \text{G-sector}$$

---

## Step 2: The Second Derivative ($A_2$)
Having found a clean form for $A_1$, I wanted to see if the structure held up for the second derivative. The symmetry seemed best highlighted using the **Canonical Form** from above

$$A_1 = R(h' - hF) + hG$$

So, I differentiated this expression directly, applying the product rule to three distinct terms ($Rh'$, $hG$, and $-RhF$).

$$A_2 = \frac{d}{dx}\left(Rh' \right) + \frac{d}{dx}(hG) - \frac{d}{dx}(RhF)$$

I had a roadmap for the first part. Since I had already performed the derivative of $Rh$, then that of $Rh'$ had to be similar but with a climbing derivative order on h.

$$ \frac{d}{dx}\left(Rh' \right) = R(h'' - h'F) + h'G $$

Now came the tricky part. It was clear that

$$ \frac{d}{dx}(hG) = h'G + hG' $$

but what was $G'$? It was also clear that

$$ \frac{d}{dx}(RhF) = \left(\frac{d}{dx}(Rh)\right)F+RhF' $$

and I already had

$$ \frac{d}{dx}(Rh) = A' = R(h' - hF) + hG $$

but what was $F'$?

### The Magic of Modules

Recall that $F$ (the first-order module) is defined as:

$$F = \frac{f'}{f \ln f}$$

So, its derivative is

$$F' = \frac{(f'') (f \ln f) - (f') \frac{d}{dx}(f \ln f)}{(f \ln f)^2}$$

Expanding the derivative in the numerator and splitting the fraction revealed the second derivative naturally formed a **higher-order module**:

$$F' = \underbrace{\frac{f''}{f \ln f}}_{F^{(2)}} - \underbrace{\frac{f'}{f \ln f}}_{F} \left( \frac{f'}{f} + \frac{f'}{f \ln f} \right)$$

Doing so allowed me to define a new superset of modules using superscript notation to denote the **module order** (based on the derivative order of the underlying function):

$$F^{(n)} = \frac{f^{(n)}}{f \ln f}$$

Substituting back, the derivative collapsed into a clean, recursive identity:

$$F' = F^{(2)} - F\left(\frac{f'}{f} + F\right)$$

I applied the same logic to the input module $G$, yielding

$$G' = G^{(2)} - G\left(\frac{g'}{g} + F\right)$$

This was the "magic" moment. I realized that taking the derivative of a module didn't change its fundamental structure; it just incremented its order and subtracted a "decay" term. To verify, I tested the derivatives of the second-order modules $F^{(2)}$ and $G^{(2)}$:

$$(F^{(2)})' = \frac{d}{dx}\left( \frac{f''}{f \ln f} \right) = F^{(3)} - F^{(2)}\left(\frac{f'}{f} + F\right)$$$$(G^{(2)})' = \frac{d}{dx}\left( \frac{g''}{g \ln f} \right) = G^{(3)} - G^{(2)}\left(\frac{g'}{g} + F\right)$$

leading to the general formulas

$$(F^{(n)})' = \frac{d}{dx}\left( \frac{f^{(n)}}{f \ln f} \right) = F^{(n+1)} - F^{(n)}\left(\frac{f'}{f} + F\right)$$$$(G^{(n)})' = \frac{d}{dx}\left( \frac{g^{(n)}}{g \ln f} \right) = G^{(n+1)} - G^{(n)}\left(\frac{g'}{g} + F\right)$$

### $A_2$: Initial Form Confirms the Symmetry

After substituting these partial modular formulations back into $F'$ and $G'$ and rearranging into canonical form, $A_2$ became

$$A_2 = R\left(h''-\left(F^{(2)}h + F\left(2h'-h\left(\frac{f'}{f}+2F\right)\right)\right)\right) +\left(G^{(2)}h + G\left(2h'-h\left(\frac{g'}{g}+2F\right)\right)\right)$$

Satisfied that this symmetry did indeed exist between the F-sector and the G-sector for at least one higher order derivative, I left it at that and went on to learn more advanced calculus.

I noticed that mapping all G's to F's and g's to f's in the G-sector would create the F-sector and mused about performing the third derivative.

### $A_3$: The G-force

Over the next few months, my mind would sometimes return to $A_3$. I began to see the process in terms of developing the G-sector and mapping $G \mapsto F$ to create the F-sector. I also realized that development of $A_\text{3G}$ would require more than simply taking the derivative of $A_\text{2G}$ as some terms would come from $A_\text{2F}$.

But which ones?

One would come from $\frac{d}{dx} Rh''$ in the form of $Gh''$ just like $Gh'$ came from $\frac{d}{dx} Rh'$ in $A_1$. This pattern showed a "leakage" of terms into the G-sector from the next lower order F-sector where each of the four $R⋅(F-sector)$ terms from $A_2F$ would simply map $R\mapsto G$ for $A_{3G}$, or:

$$\left(-RF^{(2)}h -2RFh'+RhF\frac{f'}{f}+2RhF^2\right) \mapsto \left(-GF^{(2)}h -2GFh' + GhF\frac{f'}{f}+2GhF^2 \right)$$

So I tediously accumulated all terms by taking the derivative of $A_{2G}$, adding the above cross-sector induced (or **forced**) terms to the result, and wound up with this monster of a composite polynomial representation:

$$A_{3G} = G^{(3)}h + G^{(2)}(3h'-h \left(\left(\frac{g'}{g}+F \right) + \left(\frac{g'}{g}+2F \right)\right) + G(3h''-3h'\left(\frac{g'}{g}+2F \right) + hK) $$

where

$$ K = \left(\frac{g'}{g}+F \right)\left(\frac{g'}{g}+2F \right) + F^2 - \left(\left(\frac{g'}{g}+2F \right) + F'\right) $$

Note that, out of frustration, I collapsed $F^{(2)}-F(\frac{f'}{f} + F)$ into $F'$ there at the end.

And I thought, "Am I allowed to do that"? (**Spoiler alert:** Yes, I was. Doing so was, in fact, a critical step toward future simplification.)

I didn't even know if I had gotten it correct, so I tested it on random differentiable functions in Desmos, and somehow, miraculously, I entered all the terms correctly the first time, successfully mapped $G \mapsto F$ to create the F-sector of $A_3$.

Suddenly I was matching Desmos' brute force differentiation curves, but developing them entirely while derivative estimator functionality couldn't render them more than a few units away from the origin.

Head to the Desmos file I created and turn $D(x)$ on and off by clicking the colorful circle to its left. Watch how the graph changes. Even enter some random differentiable test functions at the top.

https://www.desmos.com/calculator/a3ugeh8nwa

This algebraic stability through factoring encouraged me, but the thought of developing $A_4$ was unbearable, so I didn't attempt it in this fashion.

### The Auxiliaries and the Closed Alphabet

While making my candidate $A_3$, I did notice that representing $\frac{g'}{g}$ as $v$ and $\frac{f'}{f}$ as $u$ made things a little easier.

I also observed that taking their derivatives led to a peculiar (and subsequently very useful) result:

$$ v'= \frac{d}{dx} \left(\frac{g'}{g}\right) = \frac{g''}{g}-\left(\frac{g'}{g}\right)^2 = v^{(2)}-v^2 $$

and

$$ u'= \frac{d}{dx} \left(\frac{f'}{f}\right) = \frac{f''}{f}-\left(\frac{f'}{f}\right)^2 = u^{(2)}-u^2$$

So, I started treating $u$ and $v$ as modules, letting $u^{(n)}=\frac{f^{(n)}}{f}$ and $v^{(n)}=\frac{g^{(n)}}{g}$, yielding:

$$ \frac{d}{dx} v^{(n)}= \frac{d}{dx} \left(\frac{g^{(n)}}{g}\right) = \frac{g^{(n+1)}}{g}-\left(\frac{g^{(n)}}{g}\right)g = v^{(n+1)}-v^{(n)}v $$

and

$$ \frac{d}{dx} u^{(n)}= \frac{d}{dx} \left(\frac{f^{(n)}}{f}\right) = \frac{f^{(n+1)}}{f}-\left(\frac{f^{(n)}}{f}\right)f = u^{(n+1)}-u^{(n)}u $$

This result showed that, no matter how many times A was differentiated, one would only see this family of ${R,F,G,u,v}$.

For those uninitiated into differential algebra, this phenomenon is what is known as a **closed alphabet** making them a family of objects that are **closed under differentiation** with regard to $A_n$.

Once this realization hit, I knew I was, in fact, "allowed" to present derivatives of $F$ and $G$ in any $A_n$ by simply marking them with their derivative order rather than expanding them algebraically, making $F$ and $G$ **first-class objects**.

The closed alphabet was complete:

$$h$$ (The exponent)

$$F, G$$ (The Log-Tower Modules)

$$u, v$$ (The Logarithmic Derivatives)

Suddenly, $A_4$ was back on the menu.

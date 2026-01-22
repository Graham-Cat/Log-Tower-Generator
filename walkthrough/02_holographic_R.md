# Part 2: The Holography of R

Sequential derivatives of $A_n$ display holographic behavior; coefficients of $h_n$ freeze within the sectors and become the coefficients of $h_{n+1}$ in the next derivative. Seeing and understanding this required, at least for me, calculating higher derivatives.

## Compacted Forms

Understanding the derivative tower also begged for apples-to-apples comparisons. Since I was going to be calculating $A_4$ without expanding $F$ and $G$, the next step was to revise $A_2$ and $A_3$ into the same format.

All the hash marks were starting to make my eyes cross, so Bell notation subscripts came to the rescue.

> [!NOTE]
> Bell subscripts ($h_1, h_2, \dots$) will denote derivative order for the rest of the walkthrough.

The next few bits are, of course, the dry part, so...

> [!WARNING]
> Symbol-heavy math wall ahead!

Bear with me. It gets better.

### Compacted $A_2$ Derivation

Deriving $A_2$ algebraically was now simpler since the number and complexity of terms shrank.

We start with $A_1$:

$$A_1 = R(h_1 - hF) + hG$$

To find $A_2$, we differentiate this entire expression with respect to $x$:

$$A_2 = \frac{d}{dx} [ R(h_1 - hF) ] + \frac{d}{dx} [ hG ]$$

In differentiating the first term, $R(h_1 - hF)$, we apply the product rule $(uv)' = u_1v + uv_1$. Here, $u = R$ and $v = (h_1 - hF)$. Recall that $R_1 = G - RF$.

> *Note: This $u$ and $v$ are **not** the closed family members. They are just illustrating use of the product rule.*

$$R_1(h_1 - hF) = (G - RF)(h_1 - hF)$$

$$= Gh_1 - GhF - RFh_1 + RF^2 h$$

Now differentiate the inner term $(h_1 - hF)$:

$$\frac{d}{dx}(h_1 - hF) = h_2 - (h_1F + hF_1)$$

Multiply by $R$:

$$= R(h_2 - h_1F - hF_1)$$

Group the terms by $R$ and $G$:

$$= \underbrace{R(h_2 - h_1F - hF_1 - Fh_1 + hF^2)}_{\text{R-terms}} + \underbrace{(Gh_1 - GhF)}_{\text{G-terms}}$$

$$= R(h_2 - 2h_1F - h(F_1 - F^2)) + h_1(G) - h(GF)$$

We apply the product rule to $hG$:

$$\frac{d}{dx}(hG) = h_1G + hG_1$$

Now sum the results:

$$A_2 = [ R(h_2 - 2h_1F - h(F_1 - F^2)) + \mathbf{h_1G} - hGF ] + [ \mathbf{h_1G} + hG_1 ]$$

Combine the like terms (specifically the $h_1G$ terms):

$$A_2 = R(h_2 - 2h_1F - h(F_1 - F^2)) + (2h_1G + hG_1 - hGF)$$

Then rearrange into canonical form:

$$A_2 = R(h_2 - \underbrace{(2h_1F + h(F_1 - FF))}_{\text{F-sector}}) + \underbrace{(2h_1G + h(G_1 - GF))}_{\text{G-sector}}$$

Note how $A_2$ has a much tamer look now that derivatives of $F$ and $G$ remain compacted. Also note that the F-sector remains a $G \mapsto F$ mapping of the G-sector.

### Compacted $A_3$ Candidate

Compacting derivatives of $F$ and $G$ did *not* simplify the process enough to perform a full algebraic derivative for $A_3$, though. The large number of terms to parse by hand was overwhelming, so like before, I went with the G-sector candidate mapping process.

I refer to $A_3$ in this method as a "candidate" because, at the time I performed the process, there was no formal proof that it was valid for all derivatives. I could only check against Python's third derivative afterward. (**Spoiler alert:** it passed first try, believe it or not.)

As a refresher, the candidate-forming process involves:
1. Taking the straight derivative of the $A_2$ G-sector.
2. Expanding all $R$ terms from $A_2$.
3. Performing an $R \mapsto G$ mapping on them to derive the cross-sector induced terms.
4. Combining both sets of resulting terms and rearranging into canonical form.
5. Performing a $G \mapsto F$ mapping of the new $A_{3G}$ candidate to create a candidate $A_{3F}$.
6. Inserting the sectors into their proper canonical places in the $A_n = R(h_n - \text{F-sector}) + (\text{G-sector})$ format.

I know it seems like a lot of steps, but it's still *vastly* superior to performing the full derivative.

Instead of putting it all here, I'll just show you the end result. [^3]

[^3]: The derivation of A3 via candidate-forming method is detailed in *** insert the appropriate appendix here ***

$$A_3 = R(h_3 - (3h_2F + 3h_1(F_1 - FF) + h(F_2 - F_1F + F(-2F_1 + F^2))))$$
$$+ (3h_2G + 3h_1(G_1 - GF) + h(G_2 - G_1F + G(-2F_1 + F^2)))$$

Just for fun, I'll paste the previous version of **just the G-sector of A3** next to this one so you can see the improvement.

*Old Version of* $A_{3G}$ *:*

$$A_{3G} = G^{(3)}h + G^{(2)}(3h'-h \left(\left(\frac{g'}{g}+F \right) + \left(\frac{g'}{g}+2F \right)\right) + G(3h''-3h'\left(\frac{g'}{g}+2F \right) + hK) $$

where

$$ K = \left(\frac{g'}{g}+F \right)\left(\frac{g'}{g}+2F \right) + F^2 - \left(\left(\frac{g'}{g}+2F \right) + F'\right) $$

This is why mathematicians look for **closed alphabets**. They clean up messes like this.

### Compacted $A_4$ and $A_5$ Candidates

I went through the same process for $A_4$ and $A_5$. Those math walls are not included in this repo because they would be unnecessary clutter. Seeing it done for $A_3$ shows that it works.

Here they are:

$$A_4 = R\Big(h_4 - \big(4h_3 F + 6h_2(F_1 - FF) + 4h_1(F_2 - F_1 F + F(-2F_1 + F^2)) + h(F_3 - F_2 F + F_1(-3F_1 + F^2) + F(-3F_2 + 5F_1 F - F^3))\big)\Big)$$
$$+ \Big(4h_3 G + 6h_2(G_1 - GF) + 4h_1(G_2 - G_1 F + G(-2F_1 + F^2)) + h(G_3 - G_2 F + G_1(-3F_1 + F^2) + G(-3F_2 + 5F_1 F - F^3))\Big)$$

$$A_5 = R\Big(h_5 - \big(5h_4 F + 10h_3(F_1 - F^2) + 10h_2(F_2 - F_1 F + F(-2F_1 + F^2)) + 5h_1(F_3 - F_2 F + F_1(-3F_1 + F^2) + F(-3F_2 + 5F_1 F - F^3)) $$
$$+ h(F_4 - F_3 F + F_2(-4F_1 + F^2) + F_1(-6F_2 + 7F F_1 - F^3) + F(-4F_3 + 9F F_2 + F_1(-8F_1 + 9F^2) - F^4))\big)\Big) $$
$$+ \Big(5h_4 G + 10h_3(G_1 - GF) + 10h_2(G_2 - G_1 F + G(-2F_1 + F^2)) + 5h_1(G_3 - G_2 F + G_1(-3F_1 + F^2) + G(-3F_2 + 5F_1 F - F^3))$$
$$+ h(G_4 - G_3 F + G_2(-4F_1 + F^2) + G_1(-6F_2 + 7F F_1 - F^3) + G(-4F_3 + 9F F_2 + F_1(-8F_1 + 9F^2) - F^4))\Big)$$

Kudos to Copilot who, with appropriately specific commands, was able to parse the terms like datasets.

## Holography of R Rears its Head

A student of combinatorics should see the binomially-driven accumulation patterns in this sequential list of G sectors from $A_1$ through $A_5$.

* $A_{1G} = hG$
* $A_{2G} = 2h_1G + h(G_1 - GF)$
* $A_{3G} = 3h_2G + 3h_1(G_1 - GF) + h(G_2 - G_1F + G(-2F_1 + F^2)$
* $A_{4G} = 4h_3G + 6h_2(G_1 - GF) + 4h_1(G_2 - G_1 F + G(-2F_1 + F^2)) + h(G_3 - G_2 F + G_1(-3F_1 + F^2) + G(-3F_2 + 5F_1 F - F^3))$
* $A_{5G} = 5h_4G + 10h_3(G_1 - GF) + 10h_2(G_2 - G_1 F + G(-2F_1 + F^2)) + 5h_1(G_3 - G_2 F + G_1(-3F_1 + F^2) + G(-3F_2 + 5F_1 F - F^3)) + h(G_4 - G_3 F + G_2(-4F_1 + F^2) + G_1(-6F_2 + 7F F_1 - F^3) + G(-4F_3 + 9F F_2 + F_1(-8F_1 + 9F^2) - F^4))$

### Pattern Mining for Structure

1.  **Pascal's Triangle:** The clearest pattern is in the binomial multiplier attached to the $h_n$ terms in the form of a Pascal's triangle with the leading 1 removed on each row [i.e., (1), (2,1), (3,3,1), (4,6,4,1)]. 
2.  **The Holographic Shift:** We also see that the coefficient of $h_n$ becomes the binomially-weighted coefficient for $h_{n+1}$ in the next higher derivative and remains **structurally frozen** for all higher derivatives. This displays a "holograph" of itself into all higher order derivatives.
3.  **The Skeleton:** Within the $h$-coefficient itself (i.e., $h_0$) there is a $G$-coefficient (i.e., $G_0$) at the tail that populates binomially with a less obvious structure. Looking closely, an algebraic skeleton of ($F_nF^0$, $F_{n-1}F^1$, ..., $F_0F^n$) emerges.
4.  **Weighted Holography:** Even within the $G_n$-coefficients of the $h$-coefficient we see weighted holographic behavior like $G(-2F_1 + F^2)$ in $A_{3G}$, $G_1(-3F_1 + F^2)$ in $A_{4G}$, and $G_2(-4F_1 + F^2)$ in $A_{5G}$.

So, what to make of all this data? And why are we talking about $G$-coefficients when the section title only involves $R$?

Recall the identity:

$$R_1 = G - RF$$

Note how taking a derivative of $R$ forces a $G$ term into the G-sector of the next higher derivative, meaning all structure projected into the G-sector *at root* originates from $\frac{d}{dx}R$.

Let's take a tour of the basement of the Log-Tower to get a deeper understanding.

## Foundation of the Log-Tower

### Interplay between $R_{n-k}$ and $h_k$

The algebraic foundation of this derivative tower comes from the interplay between the first two members of the closed alphabet to arrive: $R$ and $h$. 

Recall $A=Rh$. Therefore, repeated application of the product rule produces:

$$A_1 = R_1h + Rh_1$$
$$A_2 = (R_2h + R_1h_1) + (R_1h_1 + Rh_2) = R_2h + 2R_1h_1 + Rh_2$$
$$A_3 = (R_3h + R_2h_1) + 2(R_2h_1 + R_1h_2) + (R_1h_2 + Rh_3) = R_3h + 3R_2h_1 + 3R_1h_2 + Rh_3$$

This pattern is expressed in summation notation as:

$$A_n = \sum_{k=0}^{n} \binom{n}{k} R_{n-k} h_k$$

But it only gives us part of the story. This structure explains the binomial weights on the $h_n$-coefficients, but it doesn't clearly explain the structure of the tacked-on $G$-coefficient tail.

For that, we need to go down to the _subbasement_ of the Log-Tower.

Watch your step and look out for cobwebs.


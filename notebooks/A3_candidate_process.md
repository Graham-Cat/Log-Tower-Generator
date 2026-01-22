Appendix: Construction of the $A_3$ Derivative Candidate

This appendix details the step-by-step construction of the third derivative candidate using the sector-mapping method described in Part 2.

Target Form:

$$A_3 = R(h_3 - (3h_2F + 3h_1(F_1 - F^2) + h(F_2 - F_1F + F(-2F_1 + F^2))))$$

$$+ (3h_2G + 3h_1(G_1 - GF) + h(G_2 - G_1F + G(-2F_1 + F^2)))$$

Step 1: Derivative of the $A_2$ G-Sector

We start with the G-sector of $A_2$:

$$A_{2G} = 2h_1G + h(G_1 - GF)$$

Differentiate with respect to $x$ (applying the product rule):

$$\frac{d}{dx}(A_{2G}) = \frac{d}{dx}(2h_1G) + \frac{d}{dx}(hG_1) - \frac{d}{dx}(hGF)$$

$$\frac{d}{dx}(2h_1G) = 2h_2G + 2h_1G_1$$

$$\frac{d}{dx}(hG_1) = h_1G_1 + hG_2$$

$$-\frac{d}{dx}(hGF) = -(h_1GF + hG_1F + hGF_1)$$

Result of Step 1 (Raw Derivative):

$$A_{3G(\text{raw})} = 2h_2G + 3h_1G_1 + hG_2 - h_1GF - hG_1F - hGF_1$$

Step 2: Expand $R$ Terms from $A_2$

We take the F-sector of $A_2$ (which is attached to $R$) and distribute $R$ to prepare for mapping.

$$A_{2R} = R(h_2 - (2h_1F + h(F_1 - F^2)))$$

$$A_{2R} = Rh_2 - 2Rh_1F - RhF_1 + RhF^2$$

Step 3: Perform $R \mapsto G$ Mapping (Cross-Sector Induction)

We differentiate the $R$ coefficient ($R' = G - RF$). The $G$ component of this derivative "leaks" into the G-sector. To find these induced terms, we replace every instance of $R$ in the expanded $A_{2R}$ with $G$.

$$Rh_2 \mapsto Gh_2$$

$$-2Rh_1F \mapsto -2Gh_1F$$

$$-RhF_1 \mapsto -GhF_1$$

$$+RhF^2 \mapsto +GhF^2$$

Result of Step 3 (Induced Terms):

$$G_{\text{induced}} = Gh_2 - 2h_1GF - hGF_1 + hGF^2$$

Step 4: Combine and Rearrange ($A_{3G}$)

Sum the results from Step 1 and Step 3:

$$A_{3G} = (2h_2G + 3h_1G_1 + hG_2 - h_1GF - hG_1F - hGF_1) + (Gh_2 - 2h_1GF - hGF_1 + hGF^2)$$

Group by $h$ terms:

$h_2$ terms: $2h_2G + Gh_2 = 3h_2G$

$h_1$ terms: $3h_1G_1 - h_1GF - 2h_1GF = 3h_1G_1 - 3h_1GF = 3h_1(G_1 - GF)$

$h_0$ terms: $hG_2 - hG_1F - hGF_1 - hGF_1 + hGF^2 = h(G_2 - G_1F - 2GF_1 + GF^2)$

Factor $G$ out of the inner $h_0$ group where appropriate ($F^2 = FF$):

$$h(G_2 - G_1F + G(-2F_1 + F^2))$$

Final Candidate for $A_{3G}$:

$$A_{3G} = 3h_2G + 3h_1(G_1 - GF) + h(G_2 - G_1F + G(-2F_1 + F^2))$$

Step 5: Perform $G \mapsto F$ Mapping ($A_{3F}$)

To create the F-sector, we map every $G$ in $A_{3G}$ to $F$.

$$3h_2G \mapsto 3h_2F$$

$$3h_1(G_1 - GF) \mapsto 3h_1(F_1 - FF) = 3h_1(F_1 - F^2)$$

$$h(G_2 - G_1F + G(-2F_1 + F^2)) \mapsto h(F_2 - F_1F + F(-2F_1 + F^2))$$

Final Candidate for $A_{3F}$:

$$A_{3F} = 3h_2F + 3h_1(F_1 - F^2) + h(F_2 - F_1F + F(-2F_1 + F^2))$$

Step 6: Insert into Canonical Format

Recall the canonical format $A_3 = R(h_3 - A_{3F}) + A_{3G}$.

$$A_3 = R(h_3 - (3h_2F + 3h_1(F_1 - F^2) + h(F_2 - F_1F + F(-2F_1 + F^2))))$$

$$+ (3h_2G + 3h_1(G_1 - GF) + h(G_2 - G_1F + G(-2F_1 + F^2)))$$

## $R_3$ h-coefficient confirmation

We start with the Leibniz expansion for $R_3$:

$$R_3=G_2-F(R_2)-2F_1(R_1)-RF_2$$

and then copy/paste $R_1$ and $R_2$ in terms of $R$

$$R_3 = G_2 - F(G_1 - F(G - RF) - RF_1) - 2F_1(G - RF) - RF_2$$

We expand the nested terms:

Inner Term:

$$F(G - RF) = FG - F^2R$$

Middle Group:

$$G_1 - (FG - F^2R) - RF_1 = G_1 - FG + F^2R - RF_1$$

Multiply by leading F:

$$-F(G_1 - FG + F^2R - RF_1) = -FG_1 + F^2G - F^3R + FF_1R$$

Second Group:

$$-2F_1(G - RF) = -2F_1G + 2F_1FR$$

Combine all terms:

$$R_3 = G_2 + (-FG_1 + F^2G - F^3R + FF_1R) + (-2F_1G + 2F_1FR) - RF_2$$

Group by $R$ (The F-Sector) and Non- $R$ (The G-Sector):

G-Sector: $G_2 - G_1F - G(2F_1 - F^2)$

R-Sector: $-R(F^3 - FF_1 - 2FF_1 + F_2) = -R(F_2 - F_1F - F(2F_1 - F^2))$

Thus, the clean form of $R_3$ is:

$$R_3 = [G_2 - G_1F - G(2F_1 - F^2)] - R[F_2 - F_1F - F(2F_1 - F^2)]$$

which matches the h-coefficients in $A_3$

$$A_3 = R(h_3 - (3h_2F + 3h_1(F_1 - FF) + h\underbrace{(F_2 - F_1F - F(2F_1 - F^2))}\_{\text{h-coeff F-sector}}))$$
$$+ (3h_2G + 3h_1(G_1 - GF) + h\underbrace{(G_2 - G_1F - G(2F_1 - F^2))}_{\text{h-coeff G-sector}})$$


## $R_4$ h-coefficient confirmation


We start with the Leibniz expansion for $R_4$

$$R_4=G_3-(R_3)F-3(R_2)F_1-3(R_1)F_2-RF_3$$

then copy/paste in $R_1$ through $R_3$ in terms of R

$$R_4 = G_3-F(G_2-F(G_1-F(G-RF)-RF_1)-2F_1(G-RF)-RF_2)-3F_1(G_1-F(G-RF)-RF_1)-3F_2(G-RF)-RF_3$$

expand from the innermost parentheses outward

Step A: The Innermost Core

$$G_1 - F(G - RF) - RF_1 \quad \rightarrow \quad G_1 - FG + F^2R - RF_1$$

Grouped: $[G_1 - FG] - R[F_1 - F^2]$

Step B: The "3F" Terms (Right Side)

$$ -3F_1(\text{Step A}) = -3F_1G_1 + 3F_1FG - R(3F_1F^2 - 3F_1^2)$$

$$ -3F_2(G - RF) = -3F_2G + 3F_2FR$$

Step C: The Large Parenthesis (Middle)

Inside the large $F(\dots)$ wrapper:

$G_2$

$-F(\text{Step A}) = -FG_1 + F^2G - F^3R + FF_1R$

$-2F_1(G - RF) = -2F_1G + 2F_1FR$

$-RF_2$

Sum of Step C (Inside):

$$G_2 - FG_1 + G(F^2 - 2F_1) - R(F_2 + F^3 - 3FF_1)$$

Step D: Apply the Leading F

Multiply Step C by $-F$:

$$-F(\text{Step C}) = -FG_2 + F^2G_1 - G(F^3 - 2F^2F_1) + R(FF_2 + F^4 - 3F^2F_1)$$

Grouping the Terms:

Now we sum all components ($G_3 + \text{Step D} + \text{Step B} - RF_3$) and group them by whether they contain $R$.

The Non-R Terms (G-Sector)

- $+G_3$
- $-FG_2$
- $+F^2G_1 - 3F_1G_1 \rightarrow -G_1(3F_1 - F^2)$
- $-F^3G + 2F^2F_1G + 3F_1FG - 3F_2G \rightarrow -G(3F_2 - 5FF_1 + F^3)$

The R Terms (F-Sector)

- $-RF_3$
- $+R(FF_2 + F^4 - 3F^2F_1)$ (from Step D)
- $-R(3F_1F^2 - 3F_1^2)$ (from Step B, accounting for the minus sign distribution)
- $+3F_2FR$ (from Step B)

Summing the coefficients of R:

$$-R \bigg[ F_3 - (FF_2 + 3FF_2) - (-3F^2F_1 - 3F^2F_1) - (3F_1^2) - (F^4) \bigg]$$

$$-R \bigg[ F_3 - 4FF_2 + 6F^2F_1 - 3F_1^2 - F^4 \bigg]$$

### Final Grouped Result

$$R_4 = \underbrace{\bigg[ G_3 - G_2F - G_1(3F_1 - F^2) - G(3F_2 - 5FF_1 + F^3) \bigg]}_{\text{G-Sector}} - R \underbrace{\bigg[ F_3 - F_2F - F_1(3F_1 - F^2) - F(3F_2 - 5FF_1 + F^3) \bigg]}_{\text{F-Sector}}$$

which matches the h-coefficients for $A_4$

$$A_4 = R\Big(h_4 - \big(4h_3 F + 6h_2(F_1 - FF) + 4h_1(F_2 - F_1 F - F(2F_1 - F^2)) + h\underbrace{(F_3 - F_2 F - F_1(3F_1 - F^2) - F(3F_2 - 5F_1 F + F^3))}\_{\text{h-coefficient F-sector}}\big)\Big)$$
$$+ \Big(4h_3 G + 6h_2(G_1 - GF) + 4h_1(G_2 - G_1 F - G(2F_1 - F^2)) + h\underbrace{(G_3 - G_2 F - G_1(3F_1 - F^2) - G(3F_2 - 5F_1 F + F^3))}_{\text{h-coefficient G-sector}}\Big)$$

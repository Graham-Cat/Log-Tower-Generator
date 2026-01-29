# Part 3: Replace and Find

A powerful modular differential algebra analysis tool provided the primary functionality that led to the recursive formula for $\Gamma_n$. 

And that tool was? I have two words for you. [^1]

Microsoft. Word.

[^1]: Note that one of the two words is literally "Word."

Specifically, the find-and-replace and copy/paste mechanisms in MS Word facilitated pattern finding that would have been very difficult (if not practically impossible) for me to perform on paper.

## Replace

Once I had established that $A = Rh$ expanded via the Leibniz rule and that each $R_\text{n-k}$ determined the entire contents of a matching $h_k$ coefficient, the analysis turned on understanding the algebra behind $R_n$.

### R_n Structure

Recall the identity, $R_1 = G - RF$. To get $R_2$, we take the derivative of $G - RF$:

$$ R_2 = \frac{d}{dx}R_1 = \frac{d}{dx}G - \frac{d}{dx}(RF) = G_1 - R_1F-RF_1 $$

So $R_3$ would be:

$$ R_3 = \frac{d}{dx}R_2 = \frac{d}{dx}G_1 - \frac{d}{dx}(R_1F) - \frac{d}{dx}(RF_1) = G_2 - R_2F - R_1F_1 - R_1F_1 - RF_2 = G_2 - R_2F - 2R_1F_1 - RF_2 $$

Hopefully this pattern looks familiar to you since we just saw it at the end of Part 2. If not, I'll list the first five $R_n$ to make things obvious.

$$ R_1=G-RF $$

$$ R_2=G_1-R_1F-RF_1 $$

$$ R_3=G_2-R_2F-2R_1F_1-RF_2 $$

$$ R_4=G_3-R_3F-3R_2F_1-3R_1F_2-RF_3 $$

$$ R_5=G_4-R_4F-4R_3F_1-6R_2F_2-4R_1F_3-RF_4 $$

Or, more succinctly:

$$ R_n = G_\text{n-1}- \sum_{k=0}^{n-1} \binom{n-1}{k} R_{n-k-1} F_k$$

This recursive definition still included every lower-order derivative of $R_n$, though.

I was trying to put everything in terms of $R$ to understand the algebraic roots of F/G symmetry, so I looked at the formula for $R_2$ and pasted $G-RF$ where $R_1$ was:

$$ R_2=G_1-(R_1)F-RF_1 \implies G_1-(G-RF)F-RF_1 = R_2 $$

Now I had $R_2$ in terms of $R$, which simplified to something that looked very familiar:

$$ R_2 = -R(F_1-FF)+(G_1-GF) $$

Remember $A_2$?

$$A_2 = R(h_2 - (2h_1F + h\underbrace{(F_1 - FF)}_{\text{h-coeff}})) + (2h_1G + h\underbrace{(G_1 - GF)}_{\text{h-coeff}}) $$

Unsurprisingly, $R_3$ and $R_4$ yielded the same result. Each displayed the h-coefficients of $A_3$ and $A_4$ when grouped on R.

But I still couldn't see how to formalize. The pattern got muddled in the simplification process.

So, I un-simplified.

### Deleting R

I wanted to cast as wide a net as possible, so I used the copy/paste mechanism to put $R_7$ in terms of $R$. Since I wasn't doing any simplification, the copy/paste process was easy. It yielded this:

$$ R7=G6-(R6)F-6(R5)F1-15(R4)F2-20(R3)F3-15(R2)F4-6(R1)F5-RF6 $$ 

$$ =G6-(G5-(G4-(G3-(G2-(G1-(G-RF)F-RF1)F-2(G-RF)F1-RF2)F-3(G1-(G-RF)F-RF1)F1-3(G-RF)F2-RF3)F-4(G2-(G1-(G-RF)F-RF1)F-2(G-RF)F1-RF2)F1-6(G1-(G-RF)F-RF1)F2-4(G-RF)F3-RF4)F-5(G3-(G2-(G1-(G-RF)F-RF1)F-2(G-RF)F1-RF2)F-3(G1-(G-RF)F-RF1)F1-3(G-RF)F2-RF3)F1-10(G2-(G1-(G-RF)F-RF1)F-2(G-RF)F1-RF2)F2-10(G1-(G-RF)F-RF1)F3-5(G-RF)F4-RF5)F-6(G4-(G3-(G2-(G1-(G-RF)F-RF1)F-2(G-RF)F1-RF2)F-3(G1-(G-RF)F-RF1)F1-3(G-RF)F2-RF3)F-4(G2-(G1-(G-RF)F-RF1)F-2(G-RF)F1-RF2)F1-6(G1-(G-RF)F-RF1)F2-4(G-RF)F3-RF4)F1-15(G3-(G2-(G1-(G-RF)F-RF1)F-2(G-RF)F1-RF2)F-3(G1-(G-RF)F-RF1)F1-3(G-RF)F2-RF3)F2-20(G2-(G1-(G-RF)F-RF1)F-2(G-RF)F1-RF2)F3-15(G1-(G-RF)F-RF1)F4-6(G-RF)F5-RF6 $$

I know it doesn't look useful at the moment, but once I realized that symmetry meant I could delete half the terms without losing any of the algebra, I focused on examining $G_n$ only. I found all $-RF_n$ terms and replaced them with blanks.

## Find

It was still a blurry block of parentheses, letters, numbers, and minus signs, though, until one final magical MS Word function came to my rescue.

### Tabs

AIs like Copilot automatically tab parentheses while writing math code for users. While watching it try to write something in Python code for me, I saw the tabs and figured I should give it a try.

The rules for tabbing were simple. If a parenthesis opened,

1. put the cursor just to the right of the term,
2. hit enter to move the balance of the expression down to the next line, and
3. hit tab until the next term is one tab beyond the one on the previous line.

If a parenthesis closed,

1. put the cursor just to the right of the closed parenthesis,
2. hit enter to move the balance of the expression down to the next line, and
3. hit tab until the next term is one tab **behind** the one on the previous line.

All of a sudden, the waterfall structure popped into crisp focus.

### The Recursive "Spine" of $R_{7G}$

```text
  (G6
  
    -F( G5
    
        -F( G4  <----------------------------------------------------------┐
        
            -F( G3 <-------------------------------------------┐           |
            
                -F( G2  <---------------------┐                |           |
                
                    -F( G1                    | G2 Group       |           |
                    
                        -FG)  <- G0 Group     |                |           |
                        
                    -2G F1) <-----------------┘                | G3 Group  |
                    
                -3F1( G1  <---┐ G1 Group                       |           |
                
                    -FG)  <---┘                                |           |
                    
                -3G F2) <--------------------------------------┘           |
                
            -4F1( G2 <-------┐                                             | G4 Group
            
                -F( G1       |G2 Group                                     |
                
                    -FG)     |                                             |
                    
                -2G F1) <----┘                                             |
                
            -6F2( G1                                                       |
            
                -FG)                                                       |
                
            -4G F3)  <-----------------------------------------------------┘
            
        -5F1( G3  <------------┐
        
            -F( G2             |
            
                -F( G1         |
                
                    -FG)       |
                    
                -2G F1)        | G3 Group
                
            -3F1( G1           |
            
                -FG)           | 
                
            -3G F2) <----------┘
            
        -10F2( G2
        
            -F( G1
            
                -FG)
                
            -2G F1)
            
        -10F3( G1
        
            -FG)
            
        -5G F4)
        
    -6F1( G4  <-----------------┐
    
        -F( G3                  |
        
            -F( G2              |

                -F( G1          |
                
                    -FG)        |
                    
                -2G F1)         |
                
            -3F1( G1            |
            
                -FG)            |
                
            -3G F2)             |  G4 Group
            
        -4F1( G2                |
        
            -F( G1              |
            
                -FG)            |
                
            -2G F1)             |
            
        -6F2( G1                |
        
            -FG)                |
            
        -4G F3)  <--------------┘
        
    -15F2( G3
    
        -F( G2
        
            -F( G1
            
                -FG)
                
            -2G F1)
            
        -3F1( G1
        
            -FG)
            
        -3G F2)
        
    -20F3( G2
    
        -F( G1
        
            -FG)
            
        -2G F1)
        
    -15F4( G1
    
        -FG)
        
    -6G F5)

```


If one looks at these tabs in terms of $G_n$ "groups" (i.e., terms enclosed in parentheses starting with a $G_n$ term), it's obvious that all groups with the same derivative order are identical except for their Pascal weighting and the derivative order of $F_n$ by which they are multiplied.

Now defining these groups is easy. Since we're in the home stretch, it's time to name names.

Each one of these $G_n$ groups is the definition of $\Gamma_n$:

$$ \Gamma_0 = G $$

$$ \Gamma_1 = G_1 - \Gamma_0F $$

$$ \Gamma_2 = G_2 - \Gamma_1F - 2\Gamma_0F_1 $$

$$ \Gamma_3 = G_3 - \Gamma_2F - 3\Gamma_1F_1 - 3\Gamma_0F_2 $$

$$ \Gamma_4 = G_4 - \Gamma_3F - 4\Gamma_2F_1 - 6\Gamma_1F_2 - 4\Gamma_0F_3 $$

which leads to the formula:

$$\Gamma_n = G_n - \sum_{k=0}^{n-1} \binom{n}{k} F_k \Gamma_{n-k-1}$$

This recursive engine is the beating heart of the Log-Tower generator.

Since $\Gamma_0$ is the binomially-weighted $h_\text{n-1}$ -coefficient of $A_\text{nG}$ and $\Gamma_1$ is that of the $h_\text{n-2}$ -coefficient, and so on, 

$$ A_\text{nG} = \sum_{k=0}^{n-1} \binom{n}{k} h_k \Gamma_{n-k-1}$$

Since $\Phi_n$ is the $G \mapsto F$ mapping of $\Gamma_n$, 

$$ A_\text{nF} = \sum_{k=0}^{n-1} \binom{n}{k} h_k \Phi_{n-k-1}$$

which leads to the canonical format of: 

$$P(A_n) = R_0\big[h_n - \sum_{k=0}^{n-1} \binom{n}{k} h_k \Phi_{n-k-1}\big] + \sum_{k=0}^{n-1} \binom{n}{k} h_k \Gamma_{n-k-1}$$

While this mathematical conclusion feels like a satisfying ending, we're not quite to the finish line yet since recursive engines like this one are technically _not_ closed form solutions[^2].

[^2]: A definition of "closed form solution" is available here at Wolfram: https://mathworld.wolfram.com/Closed-FormSolution.html . The definition is fuzzier than one might think, but in this case, clear and accepted closed forms are straightforward to produce.

Honestly, though, it's the end of the exciting reading since everything in the next part is well-known math. Closing a recursion like $\Gamma_n$ is a classical problem solved through use of exponential generating functions (EGFs). Developing the closed double sum is also well-trodden soil.

However, its connection to this closed alphabet { $R, h, F, G, u, v$} and its use as an explicit n-th derivative generator for $P(A_n) = \frac{d^n}{dx^n} \left(h\frac{ln(g)}{ln(f)}\right)$ is, as far as I can tell, novel.



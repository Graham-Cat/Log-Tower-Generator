# Part 8: ...and the Omega

You may have noticed that most talk of $\Omega_\beta^\alpha$ was conspicuously absent in the last part. The information below was initially slated for inclusion in Part 7 as you likely see from the title here being a continuation of the last. The prior part got too long, in particular because of the inclusion of our coverage of Volterra integrals at the end, so our concluding work on the formalization of $\Omega_\beta^\alpha$ will be included here instead.

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

$$↓↓↓↓$$

$$\Omega^\alpha_\beta = - \sum_{0 \leq \gamma \leq \beta - e_w} \binom{\alpha-e_w}{\gamma} F^{(w)}\_\gamma \Omega^{\alpha - e_w - \gamma}_{\beta - e_w - \gamma}$$

import symengine as se
import math
import itertools

class LogTowerGenerator:
    """
    Chronological Step-Operator Engine (v2.0.0)
    Generates high-order mixed-partial derivatives for Log-Tower functions.
    """
    def __init__(self, variables, f, g):
        self.vars = variables  # Tuple of spatial variables, e.g., (x, y, z)
        self.f = f
        self.g = g
        self.R = se.log(g) / se.log(f)
        
        # Persistent Tensors (Anchor/Web Cache)
        self.cache_phi = {}
        self.cache_gamma = {}

    def _get_routing(self, gamma):
        """Finds the root spatial axis (w) and the previous state (prev_gamma)."""
        # Enforces strict right-to-left spatial sequence
        for i in reversed(range(len(gamma))):
            if gamma[i] > 0:
                prev_gamma = list(gamma)
                prev_gamma[i] -= 1
                return self.vars[i], tuple(prev_gamma)
        return None, None

    def _get_phi(self, gamma):
        """Internal F-Sector recursive shift operator."""
        if gamma in self.cache_phi:
            return self.cache_phi[gamma]
            
        if sum(gamma) == 0:
            return -1  # Base Case: Phi_empty = -1
            
        w, prev_gamma = self._get_routing(gamma)
        phi_prev = self._get_phi(prev_gamma)
        
        F_w = se.diff(self.f, w) / (self.f * se.log(self.f))
        phi_curr = se.diff(phi_prev, w) - phi_prev * F_w
        
        self.cache_phi[gamma] = phi_curr
        return phi_curr

    def _get_gamma(self, gamma):
        """Internal G-Sector recursive shift operator."""
        if gamma in self.cache_gamma:
            return self.cache_gamma[gamma]
            
        if sum(gamma) == 0:
            return 0  # Base Case: Gamma_empty = 0
            
        w, prev_gamma = self._get_routing(gamma)
        
        gamma_prev = self._get_gamma(prev_gamma)
        phi_prev = self._get_phi(prev_gamma)  # Pulls from persistent F-Sector cache
        
        G_w = se.diff(self.g, w) / (self.g * se.log(self.f))
        gamma_curr = se.diff(gamma_prev, w) - phi_prev * G_w
        
        self.cache_gamma[gamma] = gamma_curr
        return gamma_curr

    def get_R_alpha(self, alpha):
        """
        The Spine Projection Corollary.
        Evaluates the mixed-partial derivative of the logarithmic scaffold: ln(g) / ln(f).
        """
        phi_val = self._get_phi(alpha)
        gamma_val = self._get_gamma(alpha)
        
        return gamma_val - self.R * phi_val

    def get_A_alpha(self, alpha, h):
        """
        The Master Generator.
        Evaluates the mixed-partial derivative of the full Log-Tower: h * (ln(g) / ln(f)).
        """
        P_A_alpha = 0
        
        # Dynamically build the n-dimensional bounds for beta <= alpha
        beta_ranges = [range(a + 1) for a in alpha]
        
        for beta in itertools.product(*beta_ranges):
            # Calculate multidimensional binomial coefficient
            coeff = math.prod(math.comb(a, b) for a, b in zip(alpha, beta))
            
            # Determine the complementary multi-index for the cache lookup
            gamma = tuple(a - b for a, b in zip(alpha, beta))
            
            # Evaluate raw h_beta state
            h_beta = h
            for var, b in zip(self.vars, beta):
                if b > 0:
                    h_beta = se.diff(h_beta, var, b)
                    
            # Pull cached tensor states
            phi_val = self._get_phi(gamma)
            gamma_val = self._get_gamma(gamma)
            
            # Accumulate Master Polynomial
            P_A_alpha += coeff * h_beta * (gamma_val - self.R * phi_val)
            
        return P_A_alpha

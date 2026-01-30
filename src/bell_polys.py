from sympy import binomial, symbols

def get_complete_bell_poly(n, args):
    """
    Computes the n-th Complete Bell Polynomial B_n(x_1, ..., x_n)
    using the recursive formula:
    B_{n} = sum_{k=0}^{n-1} binomial(n-1, k) * B_k * x_{n-k}
    
    Parameters:
    n (int): The degree of the polynomial.
    args (list): A list of arguments [x_1, x_2, ...]. 
                 Must contain at least n elements.
                 
    Returns:
    sympy expression: The symbolic polynomial.
    """
    # Base case: B_0 is always 1
    if n == 0:
        return 1
    
    result = 0
    
    # The recursion index 'k' runs from 0 to n-1
    for k in range(n):
        # We need B_k (the previous Bell poly)
        prev_bell = get_complete_bell_poly(k, args)
        
        # The argument x_{n-k}. 
        # Note: args is 0-indexed, so x_1 is at index 0.
        # If we need x_{n-k}, the index is (n - k) - 1 = n - k - 1
        x_term = args[n - k - 1]
        
        # Combine: binomial(n-1, k) * B_k * x_{n-k}
        term = binomial(n - 1, k) * prev_bell * x_term
        result += term
        
    return result

# --- Quick Test ---
if __name__ == "__main__":
    x = symbols('x1:6') # generates x1...x5
    
    # Verify B_3 = x1^3 + 3x1x2 + x3
    print("B_3:", get_complete_bell_poly(3, x).expand())

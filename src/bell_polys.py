from sympy import binomial, symbols, Function

def get_complete_bell_poly(n, args):
    """
    Computes the n-th Complete Bell Polynomial B_n(x_1, ..., x_n)
    using the recursive formula:
    B_{n+1} = sum_{k=0}^{n} binomial(n, k) * B_{n-k} * x_{k+1}
    
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
    
    # Memoization could be added here for optimization, 
    # but for symbolic clarity, we use the direct sum.
    result = 0
    
    # The recursion index 'k' runs from 0 to n-1 in the standard formula
    # adapted for 0-based indexing of our loop:
    for k in range(n):
        # We need B_k (the previous Bell poly)
        prev_bell = get_complete_bell_poly(k, args)
        
        # The argument x_{n-k} (Note: args is 0-indexed, so x_1 is at index 0)
        # We need the term x_{n-k}
        x_term = args[n - 1 - k]
        
        # Combine: binomial(n-1, k) * B_k * x_{n-k}
        term = binomial(n - 1, k) * prev_bell * x_term
        result += term
        
    return result

# --- Quick Test ---
if __name__ == "__main__":
    # Test with symbolic variables x1, x2, x3...
    x = symbols('x1:5') # generates x1, x2, x3, x4
    
    print("B_0:", get_complete_bell_poly(0, x))
    print("B_1:", get_complete_bell_poly(1, x)) # Should be x1
    print("B_2:", get_complete_bell_poly(2, x)) # Should be x1^2 + x2
    print("B_3:", get_complete_bell_poly(3, x)) # Should be x1^3 + 3x1x2 + x3

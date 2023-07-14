import numpy as np
from scipy.fftpack import idct

def chebyshev_series_complex(f, a, b, num_terms):
    # Create an array of Chebyshev nodes in the interval [-1, 1]
    nodes = np.cos(np.pi * (2 * np.arange(num_terms) + 1) / (2 * num_terms))

    # Transform the nodes to the desired interval [a, b]
    transformed_nodes = (b - a) / 2 * nodes + (a + b) / 2

    # Compute the function values at the transformed nodes
    function_values = f(transformed_nodes)

    # Compute the Chebyshev coefficients using the discrete cosine transform (DCT)
    chebyshev_coeffs = idct(function_values, type=1) / (num_terms - 1)

    return chebyshev_coeffs

# Example usage:
def complex_function(x):
    return np.exp(1j * x)  # e^(ix)

a = 0.0  # Lower bound of the interval
b = 2 * np.pi  # Upper bound of the interval
num_terms = 10  # Number of terms in the series

coefficients = chebyshev_series_complex(complex_function, a, b, num_terms)
print(coefficients)
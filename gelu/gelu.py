import numpy as np
import math

def gelu(x):
    """
    Compute the Gaussian Error Linear Unit (exact version using erf).
    x: list or np.ndarray
    Return: np.ndarray of same shape (dtype=float)
    """
    # Write code here
    arr = np.asarray(x, dtype=float)
    erf_vec = np.vectorize(math.erf)
    return 0.5*arr*(1+erf_vec(arr/np.sqrt(2)))
    pass

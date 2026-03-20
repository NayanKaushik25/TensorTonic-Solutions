import numpy as np

def expected_value_discrete(x, p):
    """
    Returns: float expected value
    """
    # Write code here
    exp=0
    for i in range(0,len(x)):
        exp+=x[i]*p[i]
    if sum(p)!=1:
        raise ValueError
    return exp
    pass

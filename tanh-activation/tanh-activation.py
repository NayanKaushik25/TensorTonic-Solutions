import numpy as np

def tanh(x):
    """
    Implement Tanh activation function.
    """
    # Write code here
    arr=np.asarray(x,dtype=float)
    li=[]
    for i in arr:
         li.append((np.exp(i) - np.exp(-i))/(np.exp(i)+np.exp(-i)))
    return li
    pass
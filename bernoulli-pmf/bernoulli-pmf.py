import numpy as np

def bernoulli_pmf_and_moments(x, p):
    """
    Compute Bernoulli PMF and distribution moments.
    """
    # Write code here
    pmf=[]
    for i in x:
        if i==0:
            pmf.append(1-p)
        else:
            pmf.append(p)
    mean=p
    var=p*(1-p)
    pmf=np.array(pmf)
    return (pmf,mean,var)
    pass
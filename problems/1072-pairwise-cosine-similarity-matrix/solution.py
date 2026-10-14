import numpy as np

def pairwise_cosine_similarity(X):

    X = np.array(X)
    
    XT = np.transpose(X)
    XSD = np.matmul(X, XT)

    XN = np.linalg.norm(X,axis=1) # (2,)
    XNR = XN.reshape(1,-1)
    XNC = XN.reshape(-1,1)

    o = np.zeros_like(XSD,dtype=float)
    on = np.zeros_like(XSD,dtype=float)

    XSD = np.divide(XSD,XNR, where=(XNR != 0))  
    XSD = np.divide(XSD,XNC, where=(XNC != 0))

    return XSD

    pass
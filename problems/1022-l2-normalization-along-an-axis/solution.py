import numpy as np

def l2_normalize(x: np.ndarray, axis: int = -1, eps: float = 1e-12) -> list:
    """
    L2-normalize x along the given axis.

    Args:
        x: input NumPy array
        axis: axis along which to normalize
        eps: small constant for numerical stability

    Returns:
        Normalized array as a nested Python list.
    """
    l2arr = np.sqrt(np.sum(np.square(x),axis))
    l2arr = np.add(l2arr,eps)
    out = np.full_like(x,-1)
    if axis == 1:
        np.divide(x,l2arr[:,np.newaxis],out=out)
        return out
    
    np.divide(x,l2arr,out=out)
    return out

    pass

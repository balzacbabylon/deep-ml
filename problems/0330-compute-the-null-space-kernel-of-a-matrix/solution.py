import numpy as np

def compute_null_space(A: np.ndarray, tol: float = 1e-10) -> np.ndarray:
    """
    Compute an orthonormal basis for the null space (kernel) of matrix A.
    
    Args:
        A: Input matrix of shape (m, n)
        tol: Tolerance for considering singular values as zero
    
    Returns:
        Matrix of shape (n, k) where k is the dimension of the null space.
        Columns form an orthonormal basis for the null space.
    """
    # Your code here
    #m = np.shape(A)[0]
    n = np.shape(A)[1]


    V = np.zeros((n,n))

    A_T = np.transpose(A)

    G = np.matmul(A_T, A)

    e_vals = np.linalg.eigvalsh(G)
    s_vals = np.sqrt(e_vals)

    V = np.linalg.eigh(G)[1]

    out = []
    
    for i in range(len(s_vals)):
        if e_vals[i] <= tol:
            out.append(V[:,i])

    if out:
        out = np.column_stack(out)
    else:
        out = np.zeros((n,0))

    return out
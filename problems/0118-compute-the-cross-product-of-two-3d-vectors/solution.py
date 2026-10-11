import torch

def cross_product(a, b) -> torch.Tensor:
    """
    Compute the cross product of two 3D vectors a and b.
    Parameters:
        a (array-like or torch.Tensor): A 3-element vector.
        b (array-like or torch.Tensor): A 3-element vector.
    Returns:
        torch.Tensor: The cross product tensor.
    """
    # Your code here

    #a = torch.as_tensor(a)
    #b = torch.as_tensor(b)

    return torch.tensor(
        [
            a[1]*b[2]- a[2]*b[1],
            -1*(a[0]*b[2] - a[2]*b[0]),
            a[0]*b[1] - a[1]*b[0]
            ])

    
    

    
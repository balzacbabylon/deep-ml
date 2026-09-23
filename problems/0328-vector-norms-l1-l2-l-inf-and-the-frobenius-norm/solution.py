import torch

def compute_norm(arr: torch.Tensor, norm_type: str) -> float:
    """
    Compute the specified norm of the input tensor.

    'l1', 'l2' and 'linf' are entrywise norms and accept a 1D or 2D tensor.
    'frobenius' is a matrix norm and must raise a ValueError if arr is not 2D.

    Args:
        arr: Input tensor (1D or 2D)
        norm_type: Type of norm ('l1', 'l2', 'linf', or 'frobenius')

    Returns:
        The computed norm as a float
    """
    # Your code here
    match norm_type:
        case "l1":
            return arr.abs().sum().item()
        case "l2":
           return arr.square().sum().sqrt().item()
        case "linf":
            return arr.abs().max().item()
        case "frobenius":
            if arr.dim() != 2:
                raise ValueError()
            return arr.square().sum().sqrt().item()
        case _:
            raise ValueError()
    
    #pass

import torch

def feature_scaling(data) -> tuple[torch.Tensor, torch.Tensor]:
    """
    Standardize and Min-Max normalize input data using PyTorch.
    Input: Tensor or convertible of shape (m,n).
    Returns (standardized_data, normalized_data), both rounded to 4 decimals.
    """
    x = torch.as_tensor(data, dtype=torch.float)
    
    xmin = torch.amin(x,dim=0,keepdim=True)
    xmax = torch.amax(x,dim=0,keepdim=True)

    datammn = (x - xmin)/(xmax - xmin)

    stnd = torch.std(x,dim=0,correction=0,keepdim=True)
    mean = torch.mean(x,dim=0,keepdim=True)

    datastd = (x - mean)/stnd

    return torch.round(datastd,decimals=4),torch.round(datammn,decimals=4)

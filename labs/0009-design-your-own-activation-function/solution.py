# --- cell 1 ---
import numpy as np
import math

def activation(x):
    '''
    Apply an activation function element-wise.
    
    Args:
        x: numpy array of any shape (raw neuron outputs)
    
    Returns:
        numpy array of same shape (activated outputs)
    
    Requirements:
        - Must be non-linear (not just returning x)
        - Must work on arrays of any shape
        - Must be deterministic
    '''
    # TODO: Implement your activation function
    
    result = np.copy(x)
    
    with np.nditer(result,op_flags=['readwrite']) as it:
        for a in it:
            a[...] = a * 0.5 * ( 1 + math.tanh(math.sqrt(2/math.pi) * (a + 0.044715*pow(a,3) )))
    
    #for a in it:
    #    result[it.index] = a * 0.5 * ( 1 + math.tanh(math.sqrt(2/math.pi) * (a + 0.044715*pow(a,3) )))
    
    #result = None  # Replace with your activation
    
    return result
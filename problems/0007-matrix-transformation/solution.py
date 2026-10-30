import numpy as np

def transform_matrix(A: list[list[int|float]], T: list[list[int|float]], S: list[list[int|float]]) -> list[list[int|float]]:
	
	if  not (np.linalg.det(T) and np.linalg.det(S)):
		return -1
	
	transformed_matrix = np.matmul(np.matmul(np.linalg.inv(T), A),S)
	
	
	return transformed_matrix
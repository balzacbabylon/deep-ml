import numpy as np
def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:

	match mode:
		case 'column':
			return np.mean(matrix,axis=0)
		case 'row':
			return np.mean(matrix,axis=1)
		
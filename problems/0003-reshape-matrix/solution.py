import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
	#Write your code here and return a python list after reshaping by using numpy's tolist() method
	

	orr = len(a)
	orc = len(a[0])
	nc = new_shape[1]
	nr = new_shape[0]

	area = orr * orc
	
	if (( orr * orc ) != (nc * nr)): return []

	fl = [0 for _ in range(area)]

	for i in range(orr):
		for j in range(orc):
			fl[i*orc + j] = a[i][j]

	reshaped_matrix = [[0 for _ in range(nc)] for _ in range(nr)]

	for i in range(nr):
		for j in range(nc):
			reshaped_matrix[i][j] = fl[i*nc + j]



	return reshaped_matrix
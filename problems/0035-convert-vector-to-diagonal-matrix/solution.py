import numpy as np

def make_diagonal(x):
	# Your code here

	diag = [[0 for _ in range(len(x))] for _ in range(len(x))]

	for i in range(len(x)):
		diag[i][i] = x[i]


	return diag

	pass
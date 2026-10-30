
import numpy as np
import math
def matrix_image(A):

	U, S, VT = np.linalg.svd(A)

	tol = 1e-12
	rank = 0
	#print("tol is %f" % (tol))
	for x in S:
		#print("x is %f" % (x))
		if x > tol:
			rank += 1

	#print(rank)
	basis = U[:, :rank]

	#return np.ndarray.tolist(np.ndarray.astype(basis,dtype=A.dtype))
	return A[:,:rank]
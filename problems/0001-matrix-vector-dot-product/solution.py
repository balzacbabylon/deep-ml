def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	# Return a list where each element is the dot product of a row of 'a' with 'b'.
	# If the number of columns in 'a' does not match the length of 'b', return -1.
	pass

	if(len(a[0]) != len(b)):return -1

	result = [0 for _ in range(len(b))]

	for i in range(len(a)):
		for j in range(len(a[0])):
			result[i] += a[i][j]* b[j]

	return result
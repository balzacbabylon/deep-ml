def determinant_4x4(matrix: list[list[int|float]]) -> float:
	
	n = len(matrix)

	if n == 2:

		a = matrix[0][0]
		b = matrix[0][1]
		c = matrix[1][0]
		d = matrix[1][1]

		return a*d - b*c

	else:

		det = 0 

		for i in range(n):
			minor = [[0 for _ in range(n-1)] for _ in range(n-1)]
			l = 0
			for j in range(n):
				if j == 0:
					continue
				p = 0
				for k in range(n):
					if k == i:
						continue
					minor[l][p] = matrix[j][k]
					p+=1
				l+=1

			det += matrix[0][i] * pow(-1,1+i+1) * determinant_4x4(minor)


		return det
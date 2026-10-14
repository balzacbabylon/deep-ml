def matrixmul(a:list[list[int|float]],
              b:list[list[int|float]])-> list[list[int|float]]:
    if len(a[0]) != len(b): return -1
    c = [[0 for _ in range(len(b[0]))] for _ in range(len(a))]
    for k in range(len(b[0])):
        for i in range(len(a)):
            for j in range(len(a[0])):
                c[i][k] += a[i][j]*b[j][k]
    return c
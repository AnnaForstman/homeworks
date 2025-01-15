def get_matrix(m, n, value):
    matrix = []
    matrix_1 = []
    if m <= 0 or n <= 0 or value <= 0:
        print(matrix)
    else:
        for i in range(m):
            for j in range(n):
                matrix_1.append(value)
            matrix.append(matrix_1)
            matrix_1 = []
        return(matrix)

res = get_matrix(2, 2, 10)
print(res)


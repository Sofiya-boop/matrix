def get_matrix (n, m, value):
    matrix = []
    for i in range(n):
        line = []
        matrix.append(line)
        for j in range(m):
            line.append(value)
    return matrix

result1 = get_matrix(0,0,10)
print(result1)
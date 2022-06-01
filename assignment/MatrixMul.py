def matrix_product(A, B):
    c = [[0 for col in range(len(A))] for row in range(len(B[0]))]
    for cRow in range(len(c)):
        for cCol in range(len(c[0])):
            for aRow in range(len(A)):
                for aCol in range((len(A[0]))):
                    c[cRow][cCol] += A[aRow][aCol] * B[aCol][aRow]
                    print([cRow][cCol])
    return c


A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]

print(matrix_product(A, B))

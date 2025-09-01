A = [
    [1, 0, 1, 0],
    [0, 1, 0, 1],
    [1, 1, 0, 0],
    [0, 0, 1, 1]
]

B = [
    [0, 1, 0, 0],
    [1, 0, 1, 0],
    [0, 1, 0, 1],
    [1, 0, 1, 0]
]

if len(A[0]) != len(B):
    print("yes")
else:
    C = [[int(any(A[i][k] and B[k][j] for k in range(len(B)))) for j in range(len(B[0]))] for i in range(len(A))]
    print("نتیجه :")
    for row in C:
        print(row)
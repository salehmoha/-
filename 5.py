M = [
    [0, 1, 0],
    [0, 0, 1],
    [1, 0, 0]
]

n = 2 

def boolean_multiply(A, B):
    return [[int(any(A[i][k] and B[k][j] for k in range(len(A)))) for j in range(len(A))] for i in range(len(A))]

Rn = M
for _ in range(n-1):
    Rn = boolean_multiply(Rn, M)

for row in Rn:
    print(*row)

#Rn
def boolean_multiply(A, B):
    n = len(A)
    return [
        [int(any(A[i][k] and B[k][j] for k in range(n))) for j in range(n)]
        for i in range(n)
    ]

n = int(input("n * n (n): "))

power = int(input("rn: "))

print(f"enter matrix :")
R = []
for i in range(n):
    row = list(map(int, input(f"row {i+1}: ").split()))
    while len(row) != n:
        print("error:")
        row = list(map(int, input(f"row {i+1}: ").split()))
    R.append(row)

result = R
for _ in range(power - 1):
    result = boolean_multiply(result, R)

print(f"\nmatrix R^{power}:")
for row in result:
    print(*row)

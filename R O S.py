#ROS
def read_matrix(name, n):
    print(f"values{name}row:")
    matrix = []
    for i in range(n):
        row = list(map(int, input(f"row {i+1}: ").split()))#دریافت سطر

        while len(row) != n:# بررسی
            print("Error")
            row = list(map(int, input(f"row {i+1}: ").split()))

        matrix.append(row)
    return matrix  

n = int(input("(n × n):"))

R = read_matrix("R", n)
S = read_matrix("S", n)

RoS = [
    [int(any(S[i][k] and R[k][j] for k in range(n))) for j in range(n)]
    for i in range(n)
]

print("\nmatrix R:")
for row in R:
    print(*row)

print("\nmatrix S:")
for row in S:
    print(*row)

print("\nmatrix RoS = R ∘ S:")
for row in RoS:
    print(*row)

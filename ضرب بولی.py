#دریافت مقادیر ماتریس و ضرب بولی 
def read_matrix(name):
    rows = int(input(f"{name} rows:"))#سطر
    cols = int(input(f"{name} cols:"))#ستون
    print(f" matrix value{name}:")#مقادیر هر ماتریس
    matrix = []
    for i in range(rows):
        row = list(map(int, input(f"rows {i+1}: ").split()))
        while len(row) != cols:
            print("Error:")
            row = list(map(int, input(f"row {i+1}: ").split()))
        matrix.append(row)
    return matrix

#خواندن ماتریس‌
A = read_matrix("A")
B = read_matrix("B")

#ضرب بولی
if len(A[0]) != len(B):
    print("Error")
else:
    C = [[int(any(A[i][k] and B[k][j] for k in range(len(B)))) for j in range(len(B[0]))] for i in range(len(A))]
    print("finaly:")
    for row in C:
        print(row)

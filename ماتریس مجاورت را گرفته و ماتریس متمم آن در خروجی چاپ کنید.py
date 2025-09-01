# تعریف ماتریس A (4×4)
A = [
    [1, 0, 1, 0],
    [0, 1, 0, 1],
    [1, 1, 0, 0],
    [0, 0, 1, 1]
]

# تعریف ماتریس B (4×4)
B = [
    [0, 1, 0, 0],
    [1, 0, 1, 0],
    [0, 1, 0, 1],
    [1, 0, 1, 0]
]

# بررسی امکان‌پذیری ضرب بولی
if len(A[0]) != len(B):
    print("❌ ضرب بولی امکان‌پذیر نیست.")
else:
    C = [[int(any(A[i][k] and B[k][j] for k in range(len(B)))) for j in range(len(B[0]))] for i in range(len(A))]
    print("✅ نتیجه ضرب بولی:")
    for row in C:
        print(row)

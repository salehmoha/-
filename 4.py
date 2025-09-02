n = 3  

# ماتریس R
R = [
    [1, 0, 1],
    [0, 1, 0],
    [0, 0, 1]
]

# ماتریس S
S = [
    [0, 1, 0],
    [1, 0, 1],
    [0, 1, 0]
]

# محاسبه‌ی RoS با استفاده از any و and
RoS = [[int(any(S[i][k] and R[k][j] for k in range(n))) for j in range(n)] for i in range(n)]

# چاپ نتیجه
print("ماتریس R:")
for row in R:
    print(*row)

print("\nماتریس S:")
for row in S:
    print(*row)

print("\nماتریس RoS = R ∘ S:")
for row in RoS:
    print(*row)

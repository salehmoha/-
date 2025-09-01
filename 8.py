M = [
    [0, 1, 0],
    [0, 0, 1],
    [1, 0, 0]
]

n = len(M)

# چاپ گراف متنی
print("گراف جهت دار (نمایش یال‌ها):")
for i in range(n):
    for j in range(n):
        if M[i][j] != 0:
            print(f"{i+1} -> {j+1}")


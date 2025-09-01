M = [
    [0, 1, 0],
    [0, 0, 1],
    [1, 0, 0]
]

n = len(M)

# رئوس
vertices = list(range(1, n+1))

# یال‌ها
edges = [(i+1, j+1) for i in range(n) for j in range(n) if M[i][j] == 1]

print("رئوس:", vertices)
print("یال‌ها:", edges)

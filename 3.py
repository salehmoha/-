
n = 4
adj = [
    [0, 1, 0, 0],
    [1, 0, 1, 0],
    [0, 1, 0, 1],
    [0, 0, 1, 0]
]

# متمم
comp = [[1 - adj[i][j] if i != j else 0 for j in range(n)] for i in range(n)]

print(" ماتریس متمم:")
for row in comp:
    print(row)

n = 4
adj = [
    [0, 1 , 0 ,0],
    [1, 0 , 0, 0]
]
comp = [[1-adj[i][j]]]
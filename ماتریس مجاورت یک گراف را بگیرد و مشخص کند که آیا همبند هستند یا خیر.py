M = [
    [0, 1, 0],
    [1, 0, 1],
    [0, 1, 0]
]

n = len(M)
visited = [False]*n
queue = [0]
visited[0] = True

while queue:
    u = queue.pop(0)
    for v in range(n):
        if M[u][v] and not visited[v]:
            visited[v] = True
            queue.append(v)

if all(visited):
    print("YES")
else:
    print(" NO ")

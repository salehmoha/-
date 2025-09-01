M = [
    [0, 1, 1],
    [1, 0, 0],
    [1, 0, 0]
]

n = len(M)

print("درجه هر رأس:")
for i in range(n):
    degree = sum(M[i])  
    print(f"رأس {i+1}: درجه {degree}")

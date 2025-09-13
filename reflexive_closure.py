#بستار تقارنی
def reflexive_closure(matrix):
    n = len(matrix)
    for i in range(n):
        matrix[i][i] = 1  
    return matrix

n = int(input("N * N : "))

print("Value:")
relation = []
for i in range(n):
    row = list(map(int, input(f"row {i+1}: ").split()))
    while len(row) != n:
        print("error:")
        row = list(map(int, input(f"row {i+1}: ").split()))
    relation.append(row)

closure = reflexive_closure(relation)

print("\nreflexive closure  :")
for row in closure:
    print(*row)

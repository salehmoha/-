
relation_matrix = [
    [0, 0, 0],
    [0, 0, 1],
    [0, 0, 0]
]
for i in range(len(relation_matrix)):
    relation_matrix[i][i] = 1
    print("relation matrix")
    for row in relation_matrix:
        print(row)
rows = int(input())
new_matrix = []
for _ in range(rows):
    matrix_numbers = [int(i) for i in input().split(", ")]
    for i in matrix_numbers:
        new_matrix.append(i)
print(new_matrix)





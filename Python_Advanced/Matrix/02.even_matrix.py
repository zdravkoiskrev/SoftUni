rows = int(input())
new_matrix = []
for _ in range(rows):
    matrix_numbers = [int(i) for i in input().split(", ") if int(i) % 2 == 0]
    new_matrix.append(matrix_numbers)
print(new_matrix)





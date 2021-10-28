n = int(input())

new_matrix = []

for _ in range(n):
    new_matrix.append(input().split(" "))
matrix_p_diagonal = [new_matrix[i][i] for i in range(n)]
matrix_diagonal_sum = 0
for i in matrix_p_diagonal:
    matrix_diagonal_sum += int(i)
print(matrix_diagonal_sum)
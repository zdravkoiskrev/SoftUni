n = int(input())

matrix = []

for _ in range(n):
    rows = [int(i) for i in input().split(" ")]
    matrix.append(rows)

primary_diagonal = []
secondary_diagonal = []

for i in range(n):
    primary_diagonal.append(matrix[i][i])
    secondary_diagonal.append(matrix[i][n - 1 - i])

primary_diagonal_sum = sum(primary_diagonal)
secondary_diagonal_sum = sum(secondary_diagonal)

difference = abs(primary_diagonal_sum - secondary_diagonal_sum)

print(difference)
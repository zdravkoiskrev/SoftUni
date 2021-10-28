rows = int(input())

matrix = []

for r in range(rows):
    row = list(input())
    matrix.append(row)


def is_valid(row, col):
    if 0 <= row < rows and 0 <= col < rows:
        return True
    return False


def calculate_attacks(matrix, row, col):
    attacks = 0
    rowl = [-2, -2, 2, 2, -1, -1, 1, 1]
    cols = [-1, 1, -1, 1, -2, 2, 2, -2]
    for index in range(len(rowl)):
        potential_row = row + rowl[index]
        potential_col = col + cols[index]
        if is_valid(potential_row, potential_col):
            potential_position = matrix[potential_row][potential_col]
            if potential_position == "K":
                attacks += 1
    return attacks


counter = 0
while True:
    max_attacks = 0
    attaker_possition = []

    for row_index in range(rows):
        for col_index in range(rows):
            if matrix[row_index][col_index] == "K":
                attacks = calculate_attacks(matrix, row_index, col_index)
                if max_attacks < attacks:
                    max_attacks = attacks
                    attaker_possition = [row_index, col_index]
    if attaker_possition:
        matrix[attaker_possition[0]][attaker_possition[1]] = "0"
        counter += 1
    else:
        break


print(counter)

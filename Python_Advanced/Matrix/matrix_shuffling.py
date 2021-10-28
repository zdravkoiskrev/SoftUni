(rows, columns) = [int(i) for i in input().split()]

matrix = []

for r in range(rows):
    row = [i for i in input().split()]
    matrix.append(row)


def check_if_index_is_valid(index_row, index_columns, rows, columns):
    if 0 <= index_row < rows and 0 <= index_columns < columns:
        return True
    return False


def command_is_valid(command, coords, rows, columns):
    if len(coords) == 4 and command == "swap":
        for index in range(0, len(coords), 2):
            if not check_if_index_is_valid(coords[index], coords[index + 1], rows, columns):
                print("Invalid input!")
                return False
        return True
    print("Invalid input!")
    return False


def print_matrix(matr):
    for row_index in range(0, len(matr)):
        for col_index in range(0, len(matr[row_index])):
            print(f"{matr[row_index][col_index]} ", end="")
        print()


data = input()

while not data == "END":
    splitted_data = data.split()
    try:
        command = splitted_data[0]
        coordinates = [int(i) for i in splitted_data[1:]]
        if command_is_valid(command, coordinates, rows, columns):
            current_row = coordinates[0]
            current_col = coordinates[1]
            row_to_swap = coordinates[2]
            col_to_swap = coordinates[3]
            temp = matrix[current_row][current_col]
            matrix[current_row][current_col] = matrix[row_to_swap][col_to_swap]
            matrix[row_to_swap][col_to_swap] = temp
            print_matrix(matrix)
        data = input()
    except:
        print("Invalid input!")
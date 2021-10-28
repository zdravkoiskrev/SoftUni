n = int(input())

matrix = []

for _ in range(n):
    row = [i for i in input().split(" ")]
    matrix.append(row)

b_loc = []
for i in range(n):
    for el in range(n):
        if matrix[i][el] == "B":
            b_loc.append([i, el])


going_up = []


def egg_counter_up():
    total_eggs = 0
    rows = int(b_loc[0][0])
    cols = int(b_loc[0][1])
    for i in range(1, n + 1):
        if not rows - i < 0:
            if not matrix[rows - i][cols] == "X":
                going_up.append([rows - i, cols])
                total_eggs += int(matrix[rows - i][cols])
            else:
                break
    return total_eggs


going_down = []


def egg_counter_down():
    total_eggs = 0
    rows = int(b_loc[0][0])  # 3
    cols = int(b_loc[0][1])  # 0
    for i in range(1, n + 1):
        if rows + i <= n - 1:
            if not matrix[rows + i][cols] == "X":
                going_down.append([rows + i, cols])
                total_eggs += int(matrix[rows + i][cols])
            else:
                break
        else:
            break
    return total_eggs


to_the_right = []


def egg_counter_right():
    total_eggs = 0
    rows = int(b_loc[0][0])  # 3
    cols = int(b_loc[0][1])  # 0
    for i in range(1, n):
        if cols + i <= n - 1:
            if not matrix[rows][cols + i] == "X":
                to_the_right.append([rows, cols + i])
                total_eggs += int(matrix[rows][cols + i])
            else:
                break
    return total_eggs


to_the_left = []


def egg_counter_left():
    total_eggs = 0
    rows = int(b_loc[0][0])  # 3
    cols = int(b_loc[0][1])  # 0
    for i in range(1, n):
        if not cols - i <= 0:
            if not matrix[rows][cols - i] == "X":
                to_the_left.append([rows, cols - i])
                total_eggs += int(matrix[rows][cols - i])
            else:
                break
    return total_eggs


def which_way():
    right = egg_counter_right()
    ll = egg_counter_left()
    up = egg_counter_up()
    down = egg_counter_down()
    if right > ll and right > up and right > down:
        print("right")
        for i in to_the_right:
            print(i)
        print(right)
    elif ll > right and ll > up and ll > down:
        print("left")
        for i in to_the_left:
            print(i)
        print(ll)
    elif up > down and up > right and up > ll:
        print("up")
        for i in going_up:
            print(i)
        print(up)
    elif down > up and down > right and down > ll:
        print("down")
        for i in going_down:
            print(i)
        print(down)


which_way()
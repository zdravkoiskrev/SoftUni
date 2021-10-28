def even_odd(*args):
    new_list = []
    old_list = []
    list_args = []
    for i in args:
        if i == "even":
            old_list.append(i)
        elif i == "odd":
            old_list.append(i)
    for i in args:
        list_args.append(i)
    list_args.pop(len(list_args) - 1)
    if old_list[0] == "even":
        for i in list_args:
            if i % 2 == 0:
                new_list.append(i)
    elif old_list[0] == "odd":
        for i in list_args:
            if not i % 2 == 0:
                new_list.append(i)
    return new_list



print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))
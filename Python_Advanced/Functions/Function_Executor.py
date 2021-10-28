def func_executor(*args):
    new_list = []
    for el, el_arg in args:
        new_list.append(el(*el_arg))

    return new_list


def sum_numbers(num1, num2):
    return num1 + num2


def multiply_numbers(num1, num2):
    return num1 * num2


print(func_executor((sum_numbers, (1, 2)), (multiply_numbers, (2, 4))))


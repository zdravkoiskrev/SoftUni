first_sequence_input = input().split(" ")
second_sequence_input = input().split(" ")

first_sequence = first_sequence_input
second_sequence = second_sequence_input


def unique_values_f():
    f_s = first_sequence
    f_s_set = set(f_s)
    f_s_list = list(f_s_set)
    return f_s_list


def unique_values_s():
    s_s = second_sequence
    s_s_set = set(s_s)
    s_s_list = list(s_s_set)
    return s_s_list


numb_commands = int(input())
for _ in range(numb_commands):
    command = input().split(" ")
    token1 = command[0]
    token2 = command[1]
    if token1 == "Add":
        if token2 == "First":
            unique_values_f()
            del command[0:2]
            command = [int(i) for i in command]
            first_sequence.extend(command)
            first_sequence = unique_values_f()
        if token2 == "Second":
            unique_values_s()
            del command[0:2]
            command = [int(i) for i in command]
            second_sequence.extend(command)
            second_sequence = unique_values_s()
    if token1 == "Remove":
        if token2 == "First":
            first_sequence = unique_values_f()
            del command[0:2]
            command = [int(i) for i in command]
            for i in command:
                if i in first_sequence:
                    first_sequence.remove(int(i))
                else:
                    continue
        if token2 == "Second":
            second_sequence = unique_values_s()
            del command[0:2]
            command = [int(i) for i in command]
            for i in command:
                if i in second_sequence:
                    second_sequence.remove(int(i))
                else:
                    continue

    if token1 == "Check" and token2 == "Subset":
        first_sequence = [int(p) for p in first_sequence]
        first_sequence.sort()
        second_sequence = [int(s) for s in second_sequence]
        second_sequence.sort()
        first_sequence_set = set(first_sequence)
        second_sequence_set = set(second_sequence)
        print(second_sequence_set.issubset(first_sequence_set))

final_first_se = [str(i) for i in unique_values_f()]
final_second_se = [str(i) for i in unique_values_s()]


print(", ".join(final_first_se))
print(", ".join(final_second_se))


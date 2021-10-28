def odd_even(command, numbers):
    odd_numbers = 0
    even_numbers = 0
    for i in numbers:
        if not i % 2 == 0:
            odd_numbers += i
        else:
            even_numbers += i
    if command == "Odd":
        print(odd_numbers * len(numbers))
    elif command == "Even":
        print(even_numbers * len(numbers))
    return


command = input()
numbers = [int(i) for i in input().split(" ")]

odd_even(command, numbers)

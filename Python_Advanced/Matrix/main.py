def negative_positive(dnumbers):
    positive_numbers_sum = 0
    negative_numbers_sum = 0
    for i in dnumbers:
        if i >= 0:
            positive_numbers_sum += i
        elif i < 0:
            negative_numbers_sum += i
    print(negative_numbers_sum)
    print(positive_numbers_sum)
    if abs(negative_numbers_sum) > positive_numbers_sum:
        print("The negatives are stronger than the positives")
    elif abs(negative_numbers_sum) < positive_numbers_sum:
        print("The positives are stronger than the negatives")
    return


dnumbers = [int(i) for i in input().split(" ")]

negative_positive(dnumbers)
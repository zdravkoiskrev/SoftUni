def shopping_list(arg, **kwargs):
    budget = arg
    if budget < 100:
        no_budget = "You do not have enough budget."
        return no_budget
    basket = 0
    if not basket > 5:
        for i, v in kwargs.items():
            cost_item = float(v[0])
            amount = float(v[1])
            cost = cost_item * amount
            if budget > cost:
                if basket < 5:
                    budget -= cost
                    basket += 1
                    return "You bought {i} for {cost:.2f} leva."






print(shopping_list(104,
                    cola=(1.20, 2),
                    candies=(0.25, 15),
                    bread=(1.80, 1),
                    pie=(10.50, 5),
                    tomatoes=(4.20, 1),
                    milk=(2.50, 2),
                    juice=(2, 3),
                    eggs=(3, 1),
                    ))

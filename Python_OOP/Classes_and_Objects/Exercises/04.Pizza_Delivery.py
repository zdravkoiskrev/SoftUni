class PizzaDelivery:

    counter = 0

    def __init__(self, name, price, ingredients):
        self.name = name
        self.price = price
        self.ingredients = ingredients
        self.ordered = False

    def add_extra(self, ingredient: str, quantity: int, price_per_quantity: float):
        if PizzaDelivery.counter == 0:
            if ingredient in self.ingredients:
                self.ingredients[ingredient] += quantity
                self.price += price_per_quantity * quantity
            else:
                self.ingredients[ingredient] = quantity
                self.price += price_per_quantity * quantity
        else:
            return f"Pizza {self.name} already prepared, and we can't make any changes!"

    def remove_ingredient(self, ingredient: str, quantity: int, price_per_quantity: float):
        if PizzaDelivery.counter == 0:
            if ingredient not in self.ingredients:
                return f"Wrong ingredient selected! We do not use {ingredient} in {self.name}!"
            else:
                if self.ingredients[ingredient] < quantity:
                    return f"Please check again the desired quantity of {ingredient}!"
                else:
                    self.ingredients[ingredient] -= quantity
                    self.price -= price_per_quantity * quantity
        else:
            return f"Pizza {self.name} already prepared, and we can't make any changes!"

    def make_order(self):
        self.ordered = True
        PizzaDelivery.counter += 1
        new_list = []
        for i, v in self.ingredients.items():
            new_item = i, ": ", str(v)
            new_item = "".join(new_item)
            new_list.append(new_item)
        new_list = ", ".join(new_list)
        return f"You've ordered pizza {self.name} prepared with {new_list} and the price will be {self.price}lv."


margarita = PizzaDelivery('Margarita', 11, {'cheese': 2, 'tomatoes': 1})
margarita.add_extra('mozzarella', 1, 0.5)
margarita.add_extra('cheese', 1, 1)
margarita.remove_ingredient('cheese', 1, 1)
print(margarita.remove_ingredient('bacon', 1, 2.5))
print(margarita.remove_ingredient('tomatoes', 2, 0.5))
margarita.remove_ingredient('cheese', 2, 1)
print(margarita.make_order())
print(margarita.add_extra('cheese', 1, 1))

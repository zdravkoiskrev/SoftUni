class Cup:

    def __init__(self, size, quantity):
        self.size = size
        self.quantity = quantity

    def fill(self, ml):
        reminder = self.size - self.quantity
        if ml < reminder:
            self.quantity += ml

    def status(self):
        reminder = self.size - self.quantity
        return reminder


cup = Cup(100, 50)
print(cup.status())
cup.fill(40)
cup.fill(20)
print(cup.status())
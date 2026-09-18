class CatFood:

    def __init__(self, brand, flavor):
        self.brand = brand
        self.flavor = flavor


class Cat:

    def __init__(self, name):
        self.name = name

    def eat(self, food):
        print(f"{self.name} eats {food.brand} {food.flavor} food.")


# One Cat eating Many CatFood items
my_cat = Cat("Whiskers")

food1 = CatFood("Whiskas", "Tuna")
food2 = CatFood("Friskies", "Chicken")

my_cat.eat(food1)
my_cat.eat(food2)

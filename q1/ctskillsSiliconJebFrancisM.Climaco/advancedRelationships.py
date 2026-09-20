# Parent Class
class Pet:

    def __init__(self, name: str, age: int, breed: str):
        self.name = name
        self.age = age
        self.breed = breed

    def get_info(self) -> str:
        return f"{self.name} is a {self.age} year old {self.breed}."


# Child Class using Inheritance
class Cat(Pet):

    def __init__(
        self, name: str, age: int, breed: str, hunger_level: int = 2
    ):
        super().__init__(name, age, breed)
        self.hunger_level = hunger_level

    def eat(self, food) -> None:
        if self.hunger_level > 0:
            self.hunger_level -= 1
            print(
                f"{self.name} ate {food.brand} {food.flavor} food! Hunger level is now {self.hunger_level}."
            )
        else:
            print(f"{self.name} is full!")

    def meow(self) -> None:
        print(f"{self.name} says: Meow!")


# Contained Object Class
class CatFood:

    def __init__(self, brand: str, flavor: str):
        self.brand = brand
        self.flavor = flavor


# Aggregation: CatOwner receives an existing Cat object
class CatOwner:

    def __init__(self, owner_name: str, cat: Cat = None):
        self.owner_name = owner_name
        self.cat = cat

    def feed_cat(self, food: CatFood) -> None:
        if self.cat:
            print(f"{self.owner_name} is feeding {self.cat.name}.")
            self.cat.eat(food)
        else:
            print(f"{self.owner_name} does not have a cat!")


# Execution / Testing
if __name__ == "__main__":
    # Test 1 — Inheritance
    cat1 = Cat(name="Whiskers", age=3, breed="Siamese", hunger_level=2)
    print("--- Test 1: Inheritance ---")
    print(cat1.get_info())
    cat1.meow()

    # Test 2 — Aggregation
    owner = CatOwner(owner_name="Alice", cat=cat1)
    print("\n--- Test 2: Aggregation ---")
    print(f"Owner {owner.owner_name} has pet: {owner.cat.name}")

    # Test 3 — Dependency
    food1 = CatFood(brand="Whiskas", flavor="Tuna")
    print("\n--- Test 3: Dependency ---")
    owner.feed_cat(food1)

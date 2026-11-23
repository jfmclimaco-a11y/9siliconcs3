class Animal:
    # Parent class
    def __init__(self, name):
        # sets the animal's name
        self.name = name
        # zaves the name

    def eat(self):
        # default eat method
        print(self.name, "is eating.")
        # prints eating message

    def make_sound(self):
        # default sound method
        print(self.name, "makes a sound.")
        # prints sound message


class Lion(Animal):
    # Lion child class
    def make_sound(self):
        # overrides sound for lion
        print(self.name, "roars loudly!")
        # prints lion sound

    def eat(self):
        # overrides eat for lion
        print(self.name, "eats fresh meat.")
        # prints lion food


class Elephant(Animal):
    # Elephant child class
    def make_sound(self):
        # overrides sound for elephant
        print(self.name, "trumpets!")
        # prints elephant sound

    def eat(self):
        # overrides eat for elephant
        print(self.name, "eats grass and fruits.")
        # prints elephant food


class Monkey(Animal):
    # Monkey child class
    def make_sound(self):
        # overrides sound for monkey
        print(self.name, "chatters!")
        # prints monkey sound

    def eat(self):
        # overrides eat for monkey
        print(self.name, "eats bananas.")
        # prints monkey food


lion = Lion("Simba")
# creates lion variable
elephant = Elephant("Dumbo")
# creates elephant variable
monkey = Monkey("George")
# creates monkey variable

animals = [lion, elephant, monkey]
# puts all objects in a list
for animal in animals:
    # loops through each animal
    animal.make_sound()
    # calls make_sound method
    animal.eat()
    # calls eat method
    print("------")
    # prints divider line

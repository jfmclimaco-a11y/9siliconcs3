class Cat:
    def __init__(self, Name, FurColor, EyeColor, Breed, Height, Length):
        self.Name = Name
        self.FurColor = FurColor
        self.EyeColor = EyeColor
        self.Breed = Breed
        self.Height = Height
        self.Length = Length
    
    def getName(self, Input_Name):
        self.Name = Input_Name

    def getFurColor(self, Input_FurColor):
        self.FurColor = Input_FurColor

    def getEyeColor(self, Input_EyeColor):
        self.EyeColor = Input_EyeColor

    def getBreed(self, Input_Breed):
        self.Breed = Input_Breed

    def getFurColor(self, Input_FurColor):
        self.FurColor = Input_FurColor
    
    def updateHeight(self, Input_Height):
        self.Height = int(Input_Height)
    
    def updateLength(self, Input_Length):
        self.Length = int(Input_Length)
    
    def displayInfo(self):
        print(f'''Name: {self.Name}
        Eye Color: {self.EyeColor}
        Fur Color: {self.FurColor}
        Breed: {self.Breed}
        Height (in inches): {self.Height}
        Length (in inches): {self.Length}''')
    
object1 = Cat("Charles", "Blue", "Black", "Siamese", 6, 15)
object2 = Cat("Xavier", "Amber", "Ginger", "Maine Coon", 7, 16)

print("---Before---")
object1.displayInfo()
object2.displayInfo()
print(f"Changing Length of cat {object2.Name}..")
object2.updateLength(17)
print("---After---")
object1.displayInfo()
object2.displayInfo()

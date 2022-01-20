# An example class I created for the RealPython Intro to OOP course

class WaterBottle:
    def __init__(self, size, color, level):
        self.size = size
        self.color = color
        self.level = level

    def describe(self):
        return f"This bottle is {self.size}oz, {self.color}, and is currently {self.level}% full"

    def sip(self, sips):
        if self.level < 0:
            print("It's already empty...")
            
        elif self.level < (sips * .5):
            print("You've finished it!")
            
        else:
            self.level -= sips * .5
            print("ahhh")

    def remaining(self):
        return f"There's about {self.level}% left"


hydro = WaterBottle(64, "green", 80)

print(hydro.describe())

hydro.sip(5)

print(hydro.remaining())

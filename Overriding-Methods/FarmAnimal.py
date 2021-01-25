class FarmAnimal:
    def __init__(self, type='Animal', legNumber=0):
        self.type = type
        self.legNumber = legNumber

    def setLeg(self, legNumber):
        self.legNumber = legNumber

    def getLeg(self):
        return self.legNumber

    def describe(self):
        print("%s has %d legs, it lives on the farm." % (self.type, self.legNumber))


class Duck(FarmAnimal):
    def makeSound(self):
        print("Quark! Quark! Quark!")


duck = Duck()  # create a Duck instance
print(duck.legNumber)  # 0 (variable defined in parent class)

duck.setLeg(2)  # access parent method
print(duck.legNumber)  # 2

duck2 = Duck('Duck', 2)  # another Duckl instance ( access the constructor in parent class)
duck2.describe()  # Duck has 2 legs, it lives on the farm. (access parent class method)

duck2.makeSound()

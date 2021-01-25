class Animal():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print("I am", self.name, "and I am", self.age, "years old")


class Dog(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)  # This will call the Animal classes constructor method
        self.name = name
        self.age = age

    def speak(self):
        print("I am a Dog")


tim = Dog("Tim", 5)
tim.speak()  # This will print "I am a Dog"

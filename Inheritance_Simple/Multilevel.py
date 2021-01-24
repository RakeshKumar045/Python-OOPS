# GrandFather -> Father -> Son

class GrandFather:
    def __init__(self, name):
        self.name = name

    def display(self):
        print(self.name)


class Father(GrandFather):
    def __init__(self, name, age):
        GrandFather.__init__(self, name)
        self.age = age

    def display(self):
        print(self.name, self.age)


class Son(Father):
    def __init__(self, name, age, address):
        Father.__init__(self, name, age)
        self.address = address

    def display(self):
        print(self.name, self.age, self.address)


s = Son("Rakesh", 27, "Bangalore")
s.display()

f = Father("Jokhan Sah", 65)
f.display()

g = GrandFather("Janki Sah")
g.display()

print("Son Details: ", s.name, s.age, s.address)
print("Father Details: ", f.name, f.age)
print("Grand Father Details: ", g.name)

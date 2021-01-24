class Polygon:
    def __init__(self, no_of_sides):
        self.n = no_of_sides
        self.sides = [0 for i in range(no_of_sides)]

    def inputSides(self):
        self.sides = [float(input("Enter side " + str(i + 1) + " : ")) for i in range(self.n)]

    def dispSides(self):
        for i in range(self.n):
            print("Side", i + 1, "is", self.sides[i])


class Triangle(Polygon):
    def __init__(self):
        Polygon.__init__(self, 3)

    def findArea(self):
        a, b, c = self.sides
        # calculate the semi-perimeter
        s = (a + b + c) / 2
        area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
        print('The area of the triangle is %0.2f' % area)


# def __init__(self, param):
#     return None

t = Triangle()
t.inputSides()

t.dispSides()
t.findArea()

# Two built-in functions isinstance() and issubclass() are used to check inheritances.

# The function isinstance() returns True if the object is an instance of the class or other classes derived from it.
print("\nisinstance")

print(isinstance(t, Triangle))
print(isinstance(t, Polygon))
print(isinstance(t, int))
print(isinstance(t, object))

print("\nissubclass")

# Similarly, issubclass() is used to check for class inheritance.
print(issubclass(Polygon, Triangle))
print(issubclass(Triangle, Polygon))
print(issubclass(bool, int))

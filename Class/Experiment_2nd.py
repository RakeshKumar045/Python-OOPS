class Point:
    def __init__(self, x=10, y=15):
        self.x = x
        self.y = y

    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)


p1 = Point(2, 3)
print(p1)

p2 = Point()
print(p2)

# All are same
print(p1.__str__())
print(str(p1))
print(format(p1))

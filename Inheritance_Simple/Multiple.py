# Multiple Base1 * Base2 = Derived

class Base1:
    def __init__(self):
        self.test1 = "Testing 1"
        print("Base1")


class Base2:
    def __init__(self):
        self.test2 = "Testing 2"
        print("Base2")


class Derived(Base1, Base2):
    def __init__(self):
        # Calling constructors of Base1 and Base2 classes
        Base1.__init__(self)
        Base2.__init__(self)
        print("Derived")

    def display(self):
        print(self.test1, self.test2)


# b1 = Base1()
# b2 = Base2()
d = Derived()
d.display()

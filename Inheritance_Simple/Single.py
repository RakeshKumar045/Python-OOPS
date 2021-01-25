# Single Inheritance : only 1 child

# Base or Super class. Note object in bracket.
# (Generally, object is made ancestor of all classes)
# In Python 3.x "class Person" is
# equivalent to "class Person(object)"

class Person(object):
    # __init__ is known as the constructor
    def __init__(self, name):
        self.name = name

    def displayName(self):
        print("Person Name is ", self.name)


class Employee(Person):
    def __init__(self, name, id):
        # self.name = name
        # invoking the __init__ of the parent class
        # Person.__init__(self, name)

        super().__init__(name)
        self.id = id
        pass

    def displayName(self):
        print("Employee Name is ", self.name)


pesron1 = Person("Rakesh")
pesron1.displayName()

employee1 = Employee("Raka")
employee1.displayName()

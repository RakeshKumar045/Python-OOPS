# Hierarchical inheritance (more than 1 child)


class Parent:
    def f1(self):
        print("Parent")


class Child1(Parent):
    def f2(self):
        print("Child 1")


class Child2(Child1):
    def f3(self):
        print("Child 2")


p = Parent()
p.f1()

print("\nChild 1 Details : ")
child1 = Child1()
child1.f1()  # calling Parent
child1.f2()  # calling own class child 1

print("\nChild 2 Details : ")
child2 = Child2()
child2.f1()  # calling Parent
child2.f2()  # calling  child 1
child2.f3()  # calling own class child 2

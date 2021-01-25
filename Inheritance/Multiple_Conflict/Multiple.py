class A:
    def __init__(self):
        self.name = 'A'
        self.age = 23

    def getName(self):
        return self.name


class B:
    def __init__(self):
        self.name = 'B'
        self.id = '32'

    def getName(self):
        return self.name


class C(A, B):
    def __init__(self):
        A.__init__(self)
        B.__init__(self)

    def getName(self):
        return self.name


C1 = C()
print(C1.getName())


# 2nd Experiment
class D(A, B):
    def __init__(self):
        # change the order
        B.__init__(self)
        A.__init__(self)

    def getName(self):
        return self.name


d = D()
print(d.getName())

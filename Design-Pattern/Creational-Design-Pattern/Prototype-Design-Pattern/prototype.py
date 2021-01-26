# https://sbcode.net/python/prototype/

import copy
from abc import ABCMeta, abstractstaticmethod


class IProtoType(metaclass=ABCMeta):
    """interface with clone method"""

    @abstractstaticmethod
    def clone():
        """The clone, deep or shallow, is up to how you
        want implement the details in your concrete class?"""


class ConcreteClass1(IProtoType):
    """concrete class 1"""

    def __init__(self, i=0, s="", l=[], d={}):
        self.i = i
        self.s = s
        self.l = l
        self.d = d

    def clone(self):
        return type(self)(
            self.i,
            self.s,
            self.l.copy(),
            self.d.copy())

    def __str__(self):
        return f"{id(self)}\ti={self.i}\ts={self.s}\tl={self.l}\td={self.d}"


class ConcreteClass2(IProtoType):
    """concrete class 2"""

    def __init__(self, i=0, s="", l=[], d={}):
        self.i = i
        self.s = s
        self.l = l
        self.d = d

    def clone(self):
        return type(self)(
            self.i,
            self.s,
            copy.deepcopy(self.l),
            copy.deepcopy(self.d))

    def __str__(self):
        return f"i={self.i}\t\ts={self.s}\tl={self.l}\td={self.d}\n{id(self.i)}\t{id(self.s)}\t{id(self.l)}\t{id(self.d)}\t"


if __name__ == "__main__":
    OBJECT1 = ConcreteClass1(
        1,
        "OBJECT1",
        [1, 2, 3],
        {"a": 4, "b": 5, "c": 6}
    )
    print(f"OBJECT1 {OBJECT1}")

    OBJECT2 = OBJECT1.clone()
    OBJECT2.s = "OBJECT2"
    OBJECT2.l[0] = 10
    print(f"OBJECT2 {OBJECT2}")
    print(f"OBJECT1 {OBJECT1}")

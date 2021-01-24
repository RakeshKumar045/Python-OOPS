# Hybrid Inheritance: Inheritance consisting of multiple types of inheritance

class University:
    def f1(self):
        print("University")


class College1(University):
    def f2(self):
        print("College 1")


class College2(University):
    def f3(self):
        print("College 2")


class School(College1, College2, University):
    def f4(self):
        print("School")


# Note :
# error : (  University, College1):
# work : ( College1, University):

# OR
# class School( College1, University):
#     def f4(self):
#         print("School")

u = University()
u.f1()

print("\nCollege 1 details : ")
c1 = College1()
c1.f1()
c1.f2()

print("\nCollege 2 details : ")
c2 = College2()
c2.f1()
c2.f3()

print("\nSchool details : ")
s = School()
s.f1()
s.f2()
s.f3()
s.f4()

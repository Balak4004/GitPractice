'''
class Student:
    name  = "Rahul"
    age = 16
    def attendCalss(self):
        print("attending the classes")
    def solveAssignmnt(self):
        print("attending solving assignment")

st1 = Student()
print(st1.name)
st1.attendCalss()
'''
from symtable import Class

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def attendCalss(self):
        print(self.name+", " +str(self.age)+" : attending the classes")
    def solveAssignmnt(self):
        print(self.name+", "+str(self.age)+" : attending solving assignment")

st1 = Student("Rahul",16)
print(st1.name)
print(st1.age)
st1.attendCalss()
st1.solveAssignmnt()

st1 = Student("Mohan",17)
print(st1.name)
print(st1.age)
st1.attendCalss()
st1.solveAssignmnt()
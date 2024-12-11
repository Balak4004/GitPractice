

class Human:
    eyes = 2
    def speak(self):
        print("human speaks")
    def eat(self):
        print("human eats")

class Student(Human):
    name = "Rahul"
    print("Name of std is : "+name)
    def speak(self):
        print(self.name+" : student speaks")
    def attendClasses(self):
        print(self.name+" : student attending classes")


human = Human()
#human.speak()
#human.eat()
print(human.eyes)
student = Student()
print(student.name)
student.eat()
student.speak()
student.attendClasses()

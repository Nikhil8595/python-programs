class Course(object):
    pass
class Student(object):
    #name = "Nik"
    #tech = "Python"

    def __init__(self,name,number):
        self.course_name = name
#       self.Student_number = self.number

    def set(self):
        self.name = "Nikhil"
        self.tech = "Python"

    def get(self):
        print(self.name,self.tech)
obj1=Student("py",30)
obj1.set()
obj1.get()
print(obj1)
print(obj1.course_name)


# obj1 = Student("Nikhil",2)
# obj2 = Student("java",30)

#print(obj2.name)
class Person(object):

    def __init__(self,name,age, role=""):
        self.name = name
        self.age = age
        self.role = role
    def __str__(self):
        return "My name is %s. I am %d years old. I am %s at ABC Primary School."%(self.name,self.age,self.role)

class Student(Person):
    def __init__(self, name, age):
        super(Student, self).__init__(name, age,'studying')

class Teacher(Person):
    def __init__(self,name, age):
        super(Teacher, self).__init__(name, age,'teaching')



steve = Student('Steve', 10)
bob = Teacher('Bob', 65)

print steve
print bob
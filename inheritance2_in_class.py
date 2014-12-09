class Job(object):
    def __init__(self, title):
        self.title = title


class Employee(object):
    def __init__(self, name, age, title):
        self.name = name
        self.age = age
        self.job = Job(title)

    def __str__(self):
        return "My name is %s, I am %d years old and I am a %s" % (self.name, self.age, self.job.title)

morgan = Employee('Morgan Williams', 24, 'software developer')
print morgan

class Person(object):
    def __init__(self, name, age, birthday, address):
        self.name = name
        self.age = age
        self.birthday = birthday
        self.address = address

    def __str__(self):
        return 'Person name: ' + self.name + \
               '\nPerson age: ' + str(self.age) + \
               '\nPerson birthday: ' + str(self.birthday) + \
               '\nPerson address: '+ str(self.address)
person = Person('Bob', 45,'08/31/56', '123 Fake Way')
print person



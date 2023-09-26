import math


class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def description(self):
        print(f'Hello {self.name}. You are {self.age} years old and you live at {self.address}')


class Circle:
    def __init__(self, radie):
        self.radie = radie

    def omkrets(self):
        return self.radie * 2 * math.pi


c1 = Circle(4)
p1 = Person('Johan', 45, 'Ålgrytebacken 7')
Person.description(p1)
print('Cirkelns omkrets är: ', Circle.omkrets(c1), 'cm')

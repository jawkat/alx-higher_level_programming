######### exemple 1
class Person:
    def __init__(self, name, age):
        self.__name = name
        self.age = age
    def get_name(self):
        return self.__name

Person = Person("Alice", 30)

print(Person.get_name())
print(Person.age)

######### exemple 2

class Mycalss:
    def __init__(self, value):
        self.value = value

    def print_value(self):
        print(self.value)
obj = Mycalss(42)
obj.print_value()

######### exemple 3


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height
    
rec1 = Rectangle(5, 3)
area = rec1.calculate_area()

print("area : {:d}".format(area))

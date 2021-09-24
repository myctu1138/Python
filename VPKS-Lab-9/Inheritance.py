class Person:
    name = ""
    age = 0
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def sayHello(self):
        print("Hello my name is "+self.name)

person1 = Person("John", 36)
person1.sayHello()

class Student(Person):
    graduationyear = 1900
    def __init__(self, name, age, year):
        super().__init__(name, age)
        self.graduationyear = year
    def welcome(self):
        print(self.name, "graduated", self.graduationyear)

x = Student("Ivan Petrov", 24, 2020)
x.welcome()
x.sayHello()
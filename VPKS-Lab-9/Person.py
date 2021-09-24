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
class Animal:
    def __init__(self,age,name):
        self.name=name
        self.age=age
    
    def speak(self):
        raise NotImplementedError("Subclass must implement abstract method")
    
class Dog(Animal):
    def speak(self):
        print(f"{self.name} says woof!")

class Cat(Animal):
    def speak(self):
        print(f"{self.name} says meow!")


a1=Dog("ANDRE",12)
a2=Cat("Nandre",7)

a1.speak()
a2.speak()        
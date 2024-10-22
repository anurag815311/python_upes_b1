class Dog:
    species="coins familiars"
    def __init__(self, name, age):
        self.name=name
        self.age=age
    def bark(self):
        return f"{self.name} says woof!"
    def get_age(self):
        return f"{self.name} is {self.age} years old"
    
dog1=Dog("Buddy",3)
dog2=Dog("Charlie",5)

print(dog2.bark())
print(dog1.get_age())
print(dog1.species)
print(dog1.age)
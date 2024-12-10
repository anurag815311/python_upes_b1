class Car:
    def __init__(self,Model,speed,color):
        self.Model=Model
        self.speed=speed
        self.color=color
    
    def get_speed(self):   #instance method
        print(f"{self.speed} is the top speed of the car")
    
    def get_model(self):
        print(f"{self.Model} is the model of the car")

    def color(self):
        print(f"the colour of the car is {self.color} ")
    
    def __str__(self):
        return f"Car details :{self.Model} {self.color} {self.speed}"
    

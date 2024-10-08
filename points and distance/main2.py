class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def distance(self,otherpoint):
        return ((self.x-otherpoint.x)**2+(self.y-otherpoint.y)**2)**(1/2)
p1=Point(0,1)
p2=Point(2,4)
p3=Point(3,6)
p4=Point(7,7)

#distance between p1 and p2 
print(p1.distance(p2))

import math
p1={"x":0,"y":1}
p2={"x":2,"y":4}
p3={"x":3,"y":6}
p4={"x":7,"y":7}
p5={"x":1,"y":0}
def distance(p1,p2):
    x1=p1["x"]
    x2=p2["x"]
    y1=p1["y"]
    y2=p2["y"]
    d=((x2-x1)^2 + (y2-y2)^2)**(1/2)
    return d;

def polar(p1):
    x=p1["x"]
    y=p1["y"]
    r=math.sqrt(x**2 + y**2)
    theta=math.atan2(y,x)
    phi=math.degrees(theta);
    return(r,phi)
#distance between two points 
print(distance(p3,p4))
#calculate polar coordinate 
print(polar(p1))
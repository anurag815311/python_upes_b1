#FUNCTION AS FIRST CLASS CITIZEN 

def square(x):
    return x * x

def apply_function(func,value):
    return func(value)

result=apply_function(square,4);
print(result)


f=square
print(f(5))
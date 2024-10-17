def introduce(name,age=25):
    print(f"Hello, my name is {name} and I am {age} years old")


def sum_number(number):
    return sum(number)

#result=sum_number([1,23,4])
#print(result)

def sum_of_number(*args):
    sum=0
    for i in args:
        sum+=i
    return sum

#result=sum_of_number(1,2,3,4,5)
#print(result)

def printting(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}:{value}")

printting(name="Alice", age=30)


"""
def print_numbers(*args):
    for i in args:
        print(i)

print_numbers(1,23,4,6)
result=sum_number([1,2,3,4,5])
print(result)
introduce("John",30)
introduce("bob")
"""

from functools import reduce


#without using reduce
def multiply(x,y):
    return x * y

numbers=[1,2,3,4]
product=1
for i in numbers:
    product=multiply(i,product)

print(product)

# with reduce

result=reduce(multiply,numbers)
print(result)

#more on map and lambda

def add_ten(number):
    return number+10
numbers=[1,2,3,4]
result=map(add_ten,numbers)
print(list(result))

#using lambda function
results=list(map(lambda x:x+10,numbers))
print(results)
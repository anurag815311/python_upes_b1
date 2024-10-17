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
def outerfunc():
    count=0
    def innerfunc():
        nonlocal count
        count += 1
        return count
    return innerfunc

def outer_func(x):
    def inner_func(y):
        return x + y
    return inner_func

clouser_func=outer_func(5)
print(clouser_func(10))  
print(clouser_func(15))


#counter1= outerfunc()

#print(counter1())
#print(counter1())

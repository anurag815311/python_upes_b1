#you can use dictionaries to map string keys to functions,enabling 
# enabling you to dynamically select and execute functions based on input.. 
def add(a,b):
    return a+b
def sub(a,b):
    return a-b

operation={
    "add": add,
    "sub": sub
}

#operation="add"
result= operation["add"](2,4)
print(result)
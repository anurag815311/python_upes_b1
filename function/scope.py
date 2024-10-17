x=10#global scope

def outer_function():
    x=20 #enclosing scope
    def inner_function():
        x=30
        print("Inner function:",x) #local scope
    inner_function()
    print("enclosing scope :",x)

outer_function()
print("global scope:",x)



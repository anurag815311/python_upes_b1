def wrapped(func):
    def innerwrapped(*args,**kwargs):
        for i in range(1,50):
            #for j in range(1,i):
                print("*",end="");
        print(" ")
        func(*args,**kwargs)
        for i in range(1,50):
            #for j in range(1,i):
                print("*",end="");
        print(" ")
    return innerwrapped

@wrapped 
def fun(n):
    for i in range(1,n):
        print(i*n);

result=fun(10)

def wrapped(func):
    def innerwrapped(*args,**kwargs):
        for i in range(1,5):
            for j in range(1,i):
                print("*");
        func(*args,**kwargs)
        print(" ",end="");
    return innerwrapped



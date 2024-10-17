#without using decorators

import time

def wrapper(func,*args,**kwargs):
    def wrapped(*args,**kwargs):
        start_time=time.time() * 1000000
        func(*args,**kwargs)
        end_time=time.time()*1000000
        print(f"FOR n : {n} \n Execution time is {end_time-start_time}")
    return wrapped

def testfn(n):
    for i in range(0,n):
        a=i*10

n=1000000
wrapped_fn=wrapper(testfn,n)

wrapped_fn(n)

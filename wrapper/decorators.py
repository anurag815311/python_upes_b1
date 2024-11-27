import time

def wrapper(func):
    def wrapped(*args,**kwargs):
        start_time=time.time()
        func(*args,**kwargs)
        end_time=time.time()
        print(f"Time taken by {func.__name__} is {end_time-start_time}");
    return wrapped

@wrapper
def count(n):
    for i in range(n):
        a=i*10


@wrapper
def random_task():
    for i in range(0,100000):
        pass

n=100000
count(n)

#random_task()
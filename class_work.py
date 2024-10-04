#class:- 04-10-24
import time
n=1000000

def testfn(n):
    for i in range(0,n):
        a=i*10

start_time=time.time() * 100000
#print(start_time)
testfn(n)
end_time=time.time()*100000
#print(end_time)
print(f"for n ={n} \n Execution time is {end_time-start_time}")

#date :- 04-10-24
import time 
ns={12312312,23423423,24234234,2345346456}

def testfn(n):
    for i in range(0,n):
        a=i*10

def wrapper(func,n):
    start_time = time.time() * 1000000

    func(n)

    end_time=time.time()*1000000
    print(f" for n = {n} \n Execution time is {end_time-start_time}")

for n in ns:
    wrapper(testfn,n)


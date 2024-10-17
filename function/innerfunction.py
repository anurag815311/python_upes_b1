def outerfunction(*args):
    def innerfunction():
        return args*2;
    return innerfunction()

def cap(ch):
    def toupper():
        return ch.upper()
    return toupper()

slogan="jai shree ram"
#list1=[1,2,3,[1,2,3],12,23]
#print(outerfunction(list1))  
print(cap(slogan))
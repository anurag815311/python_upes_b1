file=open("example.txt","w")
file.write("hello,My name is Anurag.")


file=open("example.txt","r")
content=file.read()
print(content)

file=open("example.txt","a")
file.write(" I am from India")


file=open("example.txt","r")
content=file.read()
print(content)

file.close()



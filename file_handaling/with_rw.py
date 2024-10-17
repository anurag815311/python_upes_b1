with open("example.txt","r") as file:
    data=file.read()
    print(data)

with open("example.txt","w") as file:
    file.write("\nHello, world!")

with open("example.txt","r") as file:
    data=file.read()
    print(data)
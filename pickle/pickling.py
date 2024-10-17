import pickle


info={"name":"Anu","age":21,"sapid":590018370}

with open("data.pickle","wb") as file:
    pickle.dump(info,file)

print("Data has been serialized and saved to data.pickle")


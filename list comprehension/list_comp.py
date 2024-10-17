square=[i**2 for i in range(0,10) if i %2==0]

#print(square)

even=[i for i in range(0,10) if i %2==0]
#print(even)

def to_upper(words):
    return [word.upper() for word in words]


words=['hello','baby','girl']
upper_words=[]
for w in words:
    upper_words.append(to_upper(w))

#print(upper_words)

uwords=list(map(to_upper,words))
print(uwords)
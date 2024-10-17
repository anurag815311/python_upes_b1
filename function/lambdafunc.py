add=lambda a,b:a+b

#print(add(3,2))
numbers=[1,23,2,3]
squared=map(lambda x:x*x,numbers)
#print(list(squared))

numbers2=[2,3,4,8]
even_list=filter(lambda x:x%2==0,numbers2)
print(list(even_list))
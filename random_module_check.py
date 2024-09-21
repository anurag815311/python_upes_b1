import random
counter=1
correct_num=random.randint(1,100)
user_input=int(input("enter the number between 1 to 100"))
while user_input!=correct_num:
    if user_input<correct_num:
        print("enter a higher number")
        counter=counter+1
        user_input=int(input("enter number between 1 to 100"))
    elif user_input>correct_num:
        print("enter a lower number")
        counter=counter+1
        user_input=int(input("enter number between 1 to 100"))
    else:
        print("you gussed the correct number")
        counter=counter+1
print("the number of attempts:",counter)
        
        
    

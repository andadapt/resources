timestable = input("Enter the timestable you wish to learn (1-12) ")
if len(timestable)==0:
    print("Please enter a number")
elif int(timestable)<1 or int(timestable)>12:
    print("Please enter a number between 1 and 12")
else:      
    for x in range(0,13):
        answer = x * int(timestable)
        print(timestable,"x",x,"=",answer)

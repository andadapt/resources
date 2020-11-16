timestable = input("Enter the timestable you wish to learn (1-12) ")
for x in range(0,13):
    answer = x * int(timestable)
    print(timestable,"x",x,"=",answer)

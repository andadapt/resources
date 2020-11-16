name = input("Enter your name ")
age = input("Enter your age ")
if len(name)==0 or len(age)==0:
    print("Please enter a name and age")
else:
    for x in range(0,int(age)):
        print(x+1,"Your name is",name)

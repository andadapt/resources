number = input("Enter a five digit number: ")
total = 0
for x in range(0,5):
    if x == 0 or x == 2 or x == 4:
        total = total + int(number[x])
    else:
        total = total - int(number[x])
print("The final total is:",total)

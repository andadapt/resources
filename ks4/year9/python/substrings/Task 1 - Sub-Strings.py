word = input("Enter a 5 letter word ")
print("The word backwards is",word[4] + word[3] + word[2] + word[1] + word[0])


dob = input("Enter your date of birth in the format ddmmyyyy ")
specialnumber = int(dob[0])+6 + int(dob[1])*3 + int(dob[2]) -\
                int(dob[3]) + int(dob[4])+2 + int(dob[5])+4 +\
                int(dob[6])*4 - int(dob[7])
print("The special number based on your DOB is",specialnumber)

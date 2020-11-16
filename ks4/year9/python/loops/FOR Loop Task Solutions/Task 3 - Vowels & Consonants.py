word = input("Enter a 5 letter word ")
consonant=""
vowel=""
for x in range(0,5):
    if word[x] == "a" or word[x] == "e" or \
       word[x] == "i" or word[x] == "o" or word[x] == "u":
        vowel = vowel + word[x]
    else:
        consonant = consonant + word[x]
print("Vowels in word:",vowel)
print("Consonants in word:",consonant)

word = input("Enter a word ")
consonant=""
vowel=""
if len(word)==0:
    print("Please enter a word")
else:
    wordlength= len(word)
    for x in range(0,wordlength):
        if word[x] == "a" or word[x] == "e" or \
           word[x] == "i" or word[x] == "o" or word[x] == "u":
            vowel = vowel + word[x]
        else:
            consonant = consonant + word[x]
    print("Vowels in word:",vowel)
    print("Consonants in word:",consonant)


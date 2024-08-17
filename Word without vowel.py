Vowels="AEOUI"
Word=input("Enter Word: ")
Word=Word.upper()
print(Word)
for l in Word:
    if l in Vowels:
        continue
    print(l,end="")
text=input("Enter the word :")
vowel_count=0
for i in range(0,len(text)):
    if(text[i].upper()=='A' or text[i].upper()=='E' or text[i].upper()=="I" or text[i].upper()=="O" or text[i].upper()=="U"):
        vowel_count+=1
    else:
        pass
print("The word {0} has {1} vowels".format(text.capitalize()    ,vowel_count))
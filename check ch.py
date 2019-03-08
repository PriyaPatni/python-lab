ch = input("Enter a character : ")
if(ch >= 'a' and ch <= 'z'):
    print("Lowercase Alphabet")
elif (ch >= 'A' and ch <= 'Z'): 
    print("Uppercase Alphabet") 
elif(ch >= '0' and ch <= '9'):
    print("Number")
else:
    print("Special Character")

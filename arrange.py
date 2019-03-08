a=input("enter: ")
a=''.join(sorted(a))
odd=['1','3','5','7','9']
even=['0','2','4','6','8']
str1=[ ]
str2=[ ]
str3=[ ]
str4=[ ]
for i in a:
   if i in odd:
       str1.append(i)
   elif i in even:
       str2.append(i)
   elif i>='a' and i<='z':
       str3.append(i)
   elif i>='A' and i<='Z':
       str4.append(i)
a=str3+str4+str1+str2
a=''.join(a)
print(a)

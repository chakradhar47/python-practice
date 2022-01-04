s=input("Enter the string with upper and lower case : ")
for ch in s:
    if ch>='a' and ch<='z':
        print(ch,end="")
for ch in s:        
    if ch>='A' and ch<='Z':
        print(ch,end="")

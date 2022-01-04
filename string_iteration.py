str=input("Enter string ") # hi hello nagul
words=str.split(" ") # nagul hello hi
for i in range(len(words)-1,-1,-1):
    print(words[i],end=" ")
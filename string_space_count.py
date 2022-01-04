str=input("Enter string ") # hi@3 hello nagul

print("withspaces: ",len(str))
count=0;
for ch in str:
    if ch!=' ':
        count=count+1
print("without spaces: ",count)
str="Hi hello bitLabs hi hello hi hi hello welcome to bitLabs".lower()

words=str.split(" ")
count=1;
k=0;
l=len(words)

for i in words:
    k=k+1
    for j in range(k,len(words)):
        if i==words[j]:
            count=count+1
            words[j]=" "
    if i!=' ' and count>1:
        d=(count/l)*100
#print(i,": Density: ",d)
        print(i," : ",count)
    count=1
a,b=list(map(str,input().split()))
c=a.lower()
d=b.lower()
str1=[str(x) for x in str(c)]
str2=[str(y) for y in str(d)]
length1=len(str1)
count=0
length2=len(str2)
if(length1==length2):
    for i in range(0,length1):
        if(str1[i]==str2[i]):
            count=count+0
        else:
            count=count+1
if(count==1):
    print("yes")
else:
    print("no")

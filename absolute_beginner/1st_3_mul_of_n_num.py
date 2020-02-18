#To print the 1st 3 multiples of n number

a=int(input())   #enter the input
l=[]
for i in range(1,4):
  l.append(a*i)
print(*l,end='')

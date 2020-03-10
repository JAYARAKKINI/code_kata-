#To find the count of repeatation

N,K=list(map(int,input().split())) #Enter the N and K value
n=[int(x) for x in input().split()][:N]
count=0
for i in n:
  if K==i:
    count=count+1
print(count-1)

#To print the 9 Table till the N value

n=int(input())  #Enter the n number
l=[]            
for i in range(1,n+1):
  l.append(9*i)   #Append the value into l
print(*l,end='')  #print the value

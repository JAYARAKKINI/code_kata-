#To check the value is composite or not

N=int(input())     #Enter the input
l=0
for i in range(1,N):  
  if N%i==0:
    l=i
if l>1:
  print('yes')        #If it is greater than 1 print yes
else:
  print('no')         #If it is smaller than 1 print no

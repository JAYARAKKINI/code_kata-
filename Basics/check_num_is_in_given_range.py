#To Print 'yes' if N is between L and R else print 'no'

N=int(input())
L,R=list(map(int,input().split()))
if(N>=L and N<=R) :
  print('yes')
else:
  print('no')

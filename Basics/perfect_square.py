#Print 'yes' if their product is a perfect square else print 'no'.

N,M=map(int,input().split())
L=N*M
O=N**2
if(L==O):
  print('yes')
else:
  print('no')

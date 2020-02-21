#To check the sides of scalene triangle

a,b,c=map(int,input().split())    #Enter the sides of scalene triangle
if((a!=b) and (b!=c) and (a!=c)):   #Check condition
  print('yes')
else:
  print('no')

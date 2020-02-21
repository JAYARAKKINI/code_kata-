#To print 'yes' if they can form the sides of a triangle otherwise print 'no'.

a,b,c = map(int, input().split())  #Enter the 3 side of the triangle
if (a + b <= c) or (a + c <= b) or (b + c <= a) :  # check condition  
  print('no')
else: 
  print('yes')

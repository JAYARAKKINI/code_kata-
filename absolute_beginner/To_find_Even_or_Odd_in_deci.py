#To print even or odd 

n=float(input())   #Enter the input
r=round(n)         #Round off the decimal values
if(r==0):
  print('Zero')    #if r==0 then print Zero
elif(r%2==0):
  print('Even')    #if r is even print even 
else:
  print('Odd')     #if r is odd print odd

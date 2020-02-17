#To find the square value of Nth term

N=int(input())    #Enter the input values
if(N<0):
  print('Error')  #if n is negative value print error
elif(N==0):
  print('0')      #if n is zero print Zero
else:
  print(N**2)     #print square value of N th term

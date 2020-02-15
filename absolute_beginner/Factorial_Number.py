#To find the factorial of the number

N = int(input())   # Getting an integer to find factorial
factorial = 1
  
for i in range(1,N+1): 
    factorial = factorial * i      #to calculate the factorial of a num
print(factorial)                   #to print the calculated value

# Python3 program to find simple interest 

P,R,T = map(float, input("").split())
# Calculates simple interest  
Simple_Interest = (P * R * T) / 100
  
# Print the resultant value of SI  
print('%.2f'%Simple_Interest) 

#To find the circumference of the circle 

import math              #import the math function
radius = float(input())  #Enter the radius value
if(radius>0):
  circumference = 2 * math.pi * radius      #Calculate circumference
  print("%.2f" % circumference)             #print circumference value
else:
  print('Error')

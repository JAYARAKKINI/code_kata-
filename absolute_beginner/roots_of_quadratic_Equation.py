#To find all of the roots of the quadratic.

import math
A,B,C=map(int, input().split())  #Enter the co-efficient of quadratic equation
root1 = (-B + (math.sqrt((B * B) - (4 * A * C)) ))/ (2 * A)  #First root value
root2 = (-B - (math.sqrt((B * B) - (4 * A * C)) ))/ (2 * A)
#Second root value
print('%.2f'%root1)
print('%.2f'%root2)

#To check palindrome or not

x = input()   #Enter the string
w = "" 
for i in x: 
    w = i + w 
if (x==w):   #Check both x and W are same
    print("1")   #If true print 1
else:
    print('0')  #Else print 0

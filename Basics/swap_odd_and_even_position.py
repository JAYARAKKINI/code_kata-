#To print even in odd position and odd in even position

string=str(input())  #Enter the string
swap=''.join([ string[x:x+2][::-1] for x in range(0, len(string) ,2) ])
print(swap)

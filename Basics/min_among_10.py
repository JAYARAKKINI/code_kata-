#To find minimum among 10 numbers

n=10  #get the input
x = list(map(int, input().split()))[:n]   #get the 10 array element
print(min(x))   #print minimum number

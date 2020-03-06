#Find the smallest number and largest number and print both the indices

N=input()
n=int(N)
n1=[int(x) for x in input().split()][:n]
a=min(n1)
b=max(n1)
print((n1.index(a))+1,(n1.index(b))+1)

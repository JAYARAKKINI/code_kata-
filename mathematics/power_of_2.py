a, i = set(), 1
while i <= 10000:
    a.add(i)
    i <<= 1

N = int(input())
if N in a:
    print("yes")
else:
    print("no")

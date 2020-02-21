#print 'yes' if it has a vowel in it else print 'no'

s=input()   #Enter the input
count=0
for i in range(len(s)):    #Check vowels in string
  if(s[i]=='a' or s[i]=='e' or s[i]=='i' or s[i]=='o' or s[i]=='u' or s[i]=='A' or s[i]=='E' or s[i]=='I' or s[i]=='O' or s[i]=='U'):
    count=count+1
if(count>0):   #If vowel is present print yes
  print("yes")
else:  #Else print no
  print("no")

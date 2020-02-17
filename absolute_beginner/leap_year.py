#To find leap year or not

year = int(input())   #Enter the year
if (year % 4) == 0:
   if (year % 100) == 0:
       if (year % 400) == 0:
          print("Y")
       else:
          print("N")
   else:
      print("Y")
else:
  print("N")  

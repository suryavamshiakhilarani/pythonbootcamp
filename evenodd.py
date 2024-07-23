a=int(input())
if(a%2==0 and a>=0):
   print("the number is even and positive")
elif(a%2!=0 and a<0):
   print("the number is odd and negative")
elif(a%2!=0 and a>=0):
   print("the number is odd and positive")
else:
   print("even negative number")


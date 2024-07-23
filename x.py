ca=15
cb=4
co=5
apple=int(input())
banana=int(input())
orange=int(input())
amount_given=int(input())
sum1=(apple*ca)+(banana*cb)+(orange*co)
if(sum1<=amount_given):
   print("not cheated")
else:
   print("cheated")
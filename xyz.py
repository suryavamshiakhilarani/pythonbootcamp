''' mister Z is selected for Olympics  participating in swimming one is selected as winner. z got selected x and y are friends  z. x is participating in badminton  and y in table tennis. 
height=140cm
weight is factors of 2
body fat is < 12% this for badminton
according to the selection committee  req for table tennis are
height mini=118-148
weight is the factors of no. of  medals won by z
body fat=14% acc to previous history z participated in 14 games out of it he is having success rate of 65% write a program to check whether x , y, z from India  in a same plane or not'''
x_h=int(input())
x_w=int(input())
x_f=float(input())
y_h=int(input())
y_w=int(input())
y_f=float(input())
x=0
y=0
if(x_h==140 and x_w%2==0 and x_f<0.12):
   x +=1
   #print("x is selected for badminton")
   if((118==y_w or y_w<=148) and y_w%9==0 and y_w%3==0 and y_f==0.14 ):
        y +=1
        #print("y is selected table tennis")
        print("travel in same plane")
else:
   print("they wont")

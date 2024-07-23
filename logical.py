# logical operators
'''
and , or

age=int(input())
if(age>=18 and age<24):
    print("only two wheeler")   
elif(age>=24 and age<45):
    print("both two wheeler and four wheeler")
else:
    print("all") '''
''' x goes to market buys 10 apples -$15 24 bananas-$4 and 8 oranges-$5 mother of x gave $700  '''
apple=int(input())
banana=int(input())
oranges=int(input())
a=apple*15
b=banana*4
o=orange*5
cost=a+b+o
if(cost<700):
    print("seller didnot cheat")
else:
    print("cheated")
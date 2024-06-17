import datetime
a=int(input("enter year : "))
b=int(input("enter month : "))
c=int(input("enter date : "))
x=datetime.datetime(a,b,c)
y=x.strftime("%A")
print(y)

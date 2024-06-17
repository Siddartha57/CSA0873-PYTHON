def simple(p,t,r):
    x=p
    y=t
    z=r
    s=(p*t*r)/100
    print(s)
a=int(input("Enter amount : "))
b=int(input("Enter time : "))
c=input("Senior citizen(y/n) : ")
d=0
if(c=='n'):
      d=15
else:
    d=12
simple(a,b,d)

n=int(input("Enter number : "))
x=n
rem=0
rev=0
while n!=0:
    rem=n%10
    rev=rev+rem**3
    n//=10
if(x==rev):
    print("Armstrong")
else:
    print("Not armstrong")

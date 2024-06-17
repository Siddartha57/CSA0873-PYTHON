n=int(input("Enter number : "))
rem=0
rem1=0
sum1=0
sum2=0
while n!=0:
    rem=n%10
    sum1=sum1+rem
    n//=10
while sum1!=0:
    if(sum1>=10):
        rem1=sum1%10
        sum2=sum2+rem
    else:
        sum2=sum1
    sum1//=10
print(sum2)

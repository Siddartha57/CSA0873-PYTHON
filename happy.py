def happy(n):
    rem=0
    sum1=0
    x=n
    while x>0:
        rem=x%10
        sum1=sum1+rem**2
        x//=10
        return sum1
num=int(input("Enter number : "))
y=num
while y!=1 and y!=4:
    y=(happy(y))
if(y==1):
    print("happy")
elif(y==4):
    print("un happy")
    
        

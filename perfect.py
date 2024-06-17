n=int(input("enter number : "))
x=n
sum=0
for i in range(1,n):
    if(n%i==0):
        sum=sum+i
if(x==sum):
    print("perfect")
else:
    print("not a perfect")

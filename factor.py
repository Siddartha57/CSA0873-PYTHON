x=int(input("Enter the number : "))
n=int(input("Enter position of factor : "))
fact=0
arr=[]
for i in range(1,x+1):
    if(x%i==0):
        fact=fact+1
        arr.append(i)
y=len(arr)
for i in range(0,y):
    if(n==i):
        print("",n,"th factor of ",x,"is",arr[i-1])
print("no of factors for",x,"is",fact)


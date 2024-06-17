arr1=[]
arr2=[]
n=int(input("Enter no of elements : "))
for i in range(0,n):
    ele=int(input())
    arr1.append(ele)
for i in range(0,n):
    if(arr1[i]%3==0):
        x="Fizz"
        arr2.append(x)
    elif(arr1[i]%5==0):
        x="Buzz"
        arr2.append(x)
    else:
        arr2.append(arr1[i])
print(arr2)

arr1=[]
arr2=[]
n=int(input("Enter no of elements : "))
for i in range(0,n):
    ele=int(input())
    arr1.append(ele)
x=int(input("Enter the target : "))
for i in range(0,n):
    if(arr1[i]==x):
        arr2.append(i)
print(arr2)


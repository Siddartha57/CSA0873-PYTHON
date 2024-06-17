arr1=[]
arr2=[]
n=int(input("Enter no of elements : "))
for i in range(0,n):
    ele=int(input())
    arr1.append(ele)
arr1=sorted(arr1)
for i in range(0,n):
    ele=arr1[i]
    arr2.append(ele)
x=int(input("Enter the no to  change : "))
y=int(input("Enter the Position : "))
for i in range(0,n):
    if(i==y):
        arr1[i-1]=x
print("Original array ",arr2)
print("after changing array values are : ",arr1)

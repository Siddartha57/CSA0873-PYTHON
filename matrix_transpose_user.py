a=int(input("Enter no of rows : "))
b=int(input("Enter no of columns : "))
x=[]
y=[]
c=a*b
for i in range(a):
    z=[]
    for j in range(b):
        z.append(int(input()))
    x.append(z)
for i in range(c+1):
    for j in range(c+1):
        y[j][i]=x[i][j]
print("Before transpose : ")
for i in range(a):
    for j in range(b):
        print(x[j])
    print("\n")
    break
for i in range(a):
    print("After transpose")
    for j in range(b):
        print(y[j])
    print("\n")
    break

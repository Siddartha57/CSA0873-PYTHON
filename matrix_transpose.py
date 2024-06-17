x=[[1,2,3],
   [4,5,6],
   [7,8,9]]
y=[[0,0,0],
   [0,0,0],
   [0,0,0]]
for i in range(len(x)):
    for j in range(len(x)):
        y[j][i]=x[i][j]
print("Before transpose : ")
for i in range(len(y)):
    for j in range(len(y)):
        print(x[j])
    print("\n")
    break
for i in range(len(y)):
    print("After transpose")
    for j in range(len(y)):
        print(y[j])
    print("\n")
    break

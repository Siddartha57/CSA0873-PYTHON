n=int(input("enter 1st number : "))
m=int(input("enter 2nd number : "))
for i in range(n,m):
    for j in range(2,i):
        if(i==j):
            continue
        elif i%j==0:
            print(i)
            break

            
            

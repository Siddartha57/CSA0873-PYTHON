n=int(input("Enter n value : "))
sum=0
fact=1
for i in range(1,n+1):
    for j in range(1,i+1):
        fact=fact*j
        ele=fact
    sum=sum+ele
    fact=1
print(sum)
        

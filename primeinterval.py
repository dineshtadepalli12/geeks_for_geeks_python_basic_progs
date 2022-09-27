l = int(input("Enter the lower bound"))
u = int(input("Enter the upper bound"))

for num in range(l,u+1):
    if num ==0 or num==1:
        continue
    for j in range(2,num):
        if num%j==0:
            break
    else:
        print(num,end=" ")

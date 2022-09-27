num = int(input("enter the number to check: "))
count=0
for i in range(1, num+1):
    if num%i==0:
        count+= 1
if count==2:
    print(f"The number {num} is prime")
else:
    print("composite")

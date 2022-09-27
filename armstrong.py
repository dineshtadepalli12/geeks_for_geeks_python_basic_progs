
n = 153
s = n
b = len(str(n))
sum = 0

while n>0:
    r = n%10
    sum = sum + (r**b)
    n = n//10

if s == sum:
    print("the given number {0} is an armstrong number".format(s))
else:
    print("not an armstrong number")

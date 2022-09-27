
"""
def facto(n):

    if n<0:
        return 0
    if n==0 or n==1:
        return 1
    else:
        fact = 1
        while (n>1):
            fact = fact * n
            n = n-1
        return fact
n = 5
facto(n)
print("the factorial is",facto(n))
"""


#or
#does have a problem if number is less than 1
import numpy
n=-1
x=numpy.prod([i for i in range(1,n+1)])
print(x)
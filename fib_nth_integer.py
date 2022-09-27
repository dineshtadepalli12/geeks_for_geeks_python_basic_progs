"""
#method1 using arrays
def fibonacci (n):
    if n<= 0:
        return "Incorrect Output"
    data = [0, 1]
    if n == 1:
        return data[0]
    elif n == 2:
        return data[1]
    else:
        for i in range (2, n):
            data.append(data[i-1] + data[i-2])
        return data[n-1]

print(fibonacci(5))

"""


def fib(n):
    a = 0
    b = 1
    if n<=0:
        print("enter greater than or equal to 0!")
    elif n == 1:
        return a
    else:
        for i in range(2,n):
            c = a+b
            a = b
            b = c
        return b
print(fib(9))
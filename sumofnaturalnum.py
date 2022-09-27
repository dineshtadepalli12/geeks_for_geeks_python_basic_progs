def nat(n):
    a = 0
    for i in range(1,n+1):
        b = i*i
        a = b + a
    return a

print(nat(3))

#0r

def nat(n):
    sum = 0
    for i in range(1,n+1):
        sum = sum + (i*i)

print(nat(3))
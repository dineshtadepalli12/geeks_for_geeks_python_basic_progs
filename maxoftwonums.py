"""
def maxi(a,b):
    if a>b:
        print("the max num is {0}".format(a))
    elif a==b:
        print("the max is none")
    else:
        print("the max num is {0} ".format(b))

a = 14
b = 11
maxi(a,b)
"""

#or

a = 10
b = 20

x = [a if a>b else b]
print('the maximum number is',x)
print(type(x))

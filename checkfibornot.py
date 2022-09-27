def fibonacci(n):
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
        return data

print(fibonacci(10))

for i in range(1,10):
    if i in fibonacci(10):
        print(f"{i} is fibonacci number")
    else:
        print(f"{i} is not a fibonacci number")

def func(a):
    sum = 0
    for i in range(0, a):
        sum += i ** 3
    return sum

a = int(input("a: "))
b = func(a)
print("result: ", b)



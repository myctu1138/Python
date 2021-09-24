num = int(input("insert number"))

condition = 0
if num > 1:
    for i in range(2, num//2):
        if (num % i) == 0:
            condition = 1
            break
else:
    print(num, "is a prime number:")
if condition == 1:
    print(num, "is not a prime number:")
else:
    print(num, "is a prime number:")

import cmath
for i in range(2):
    try:
        r = float(input("r= "))
    except ValueError:
        print("NaN")
    else:
        print(cmath.pi * 2 * r)

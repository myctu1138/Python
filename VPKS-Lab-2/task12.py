import cmath
x1, y1 = int(input("x1: ")), int(input("y1: "))
x2, y2 = int(input("x2: ")), int(input("y2: "))
a = (x1-x2) ** 2
b = (y1-y2) ** 2
c = cmath.sqrt(a + b)
print("distance: ", c)
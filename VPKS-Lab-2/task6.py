a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))
if(a == b and b == c):
    s = 3 * (a + b + c)
else:
    s = (a + b + c)
print("result: %d" %s)
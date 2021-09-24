a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))
if(a == b or b == c or c == a):
    result = 0
else:
    result = a + b + c
print("result: %d" %result)
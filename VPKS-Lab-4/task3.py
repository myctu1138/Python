list1 = [5,7,3,2,0.2]
def myfunction1(somelist):
    mul = 1
    for i in somelist:
        mul = mul * i
    return mul
print(myfunction1(list1))

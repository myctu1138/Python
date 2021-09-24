number = input("Insert number:")
def myfunction(number):
    r = range(2, 125)
    if(number in r):
        return True
    else:
        return False
print(myfunction(int(number)))
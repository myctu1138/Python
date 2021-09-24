string = input ("Insert string:")
def myfunction4(string):
    Capitalized = 0
    notCapitalized = 0
    for i in range(len(string)):
        if (ord(string[i]) >= 97 and ord(string[i]) <= 122):
            notCapitalized += 1
        elif (ord(string[i]) >= 65 and ord(string[i]) <= 90):
            Capitalized += 1
        else:
            continue
    print("Capitalized:%d\nNot Capitalized:%d" %(Capitalized, notCapitalized))

myfunction4(string)

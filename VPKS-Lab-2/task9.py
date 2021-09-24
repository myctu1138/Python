integers = [5,2,3,7,1,2,3,5,4,1,8,79,56,75,34,54,54,234,62,12,69]
a = int(input("enter a number: "))
counter = 0
for element in integers:
    if(element == a):
        counter = counter + 1
if(counter>0):
    print("yes")
else:
    print("no")
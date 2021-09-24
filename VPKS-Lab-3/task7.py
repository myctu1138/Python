list = [*range(1,31)]

for el in list:
    if(el%2 == 0):
        list.remove(el)
print(list)
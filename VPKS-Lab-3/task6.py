list1 = [*range(1,31)]
list2 = []

print(list1)
for el in list1:
    list2.append(el**2)
print(list2[:+5])
print(list2[-5:])
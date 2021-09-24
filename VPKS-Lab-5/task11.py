dic = {'a': "Apple", 'b':"Banana", 'c':"Tomato"}
key = 'a'
if key in dic:
    print ("Key exists")
    del dic[key]
else:
    print ("Key does not exist")
print(dic)
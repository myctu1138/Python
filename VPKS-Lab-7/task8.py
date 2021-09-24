string = "Technical University"
string2 = ''

for i in range(len(string)):
    if(i%2==0):
        string2 += string[i]
print(string2)
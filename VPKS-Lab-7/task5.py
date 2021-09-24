str1 = "Technical university"
str2 = ''
if(len(str1)>=3):
    if(str1[-3:]=='ing'):
        str2 = str1+'ly'
    else:
        str2 = str1+'ing'
print(str2)
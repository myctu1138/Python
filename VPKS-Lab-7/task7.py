str1 = "Technical University"
str2 = str1.replace(str1[0], str1[-1])
str3 = str2[0]+str2[1:].replace(str2[-1], str1[0])
print(str3)
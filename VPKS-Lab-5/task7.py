dict ={1: 1,
       2: 4,
       3: "asd",
       4: 23,
       5: 25,
       6: "lsdza",
       7: 49,
       8: 64,
       9: 0,
       10: 9}
for i, j in dict.items():
    if(j == i*i):
        print("%d = %d" %(i, j))
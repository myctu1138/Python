arr = [3,5,7,2,8,0,5,22,55,42,99,15,252,256,128,18,15]
for i in range(30):
    try:
        if(arr[i]%2==0):
            print(arr[i])
    except IndexError:
        print("Out of bounds element")
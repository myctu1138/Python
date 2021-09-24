for i in range(2):
    try:
        a = float(input("insert a:"))
        b = float(input("insert b:"))
    except ValueError:
        print("NaN")
    else:
        c = a*b
        print(c)
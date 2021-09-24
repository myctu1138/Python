import datetime
from datetime import time
from datetime import datetime
dt_string = "12/11/2018 09:15:32"
dt_object1 = datetime.strptime(dt_string, "%d/%m/%Y %H:%M:%S")
print(dt_object1)

now = datetime.now()
printformat = now.strftime("%d/%m/%Y %H:%M:%S")
print(printformat)
printformat = now.strftime("%Y")
print(printformat)
printformat = now.strftime("%m")
print(printformat)
printformat = now.strftime("%W")
print(printformat)
printformat = now.strftime("%a(%w)")
print(printformat)
printformat = now.strftime("%j")
print(printformat)
printformat = now.strftime("%d")
print(printformat)
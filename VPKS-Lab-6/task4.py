from datetime import datetime
dt_string = "12/11/2018 09:15:32"
dt_object1 = datetime.strptime(dt_string, "%d/%m/%Y %H:%M:%S")
print(dt_object1)
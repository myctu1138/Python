from datetime import datetime
date_format = "%H:%M:%S"

time_start = str("09:00:00")
time_end = str("18:00:00")
diff = datetime.strptime(time_end, date_format)-datetime.strptime(time_start, date_format)
result = diff.seconds
print(result)
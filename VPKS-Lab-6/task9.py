from datetime import date
birth = date(1998,11,3)
today = date.today()
delta = today - birth
print(delta.days)
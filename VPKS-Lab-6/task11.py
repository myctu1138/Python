from datetime import date

birth = date(1998,11,3)
today = date.today()
age = today.year - birth.year - ((today.month,today.day)<(birth.month,birth.day))
print(age)
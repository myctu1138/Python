number = int(input("Enter a number:"))
def recur_factorial(number):
   if number == 1:
       return number
   else:
       return number*recur_factorial(number-1)
print(recur_factorial(number))
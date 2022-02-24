var_leap = input("Enter Year which you want to check :")
if len(var_leap) != 4:
 print(" please provide value in YYYY format  ")
 var_leap = int(input("Enter your value again in YYYY format:"))


def leap_year(year):
   if year % 4 == 0 and not(year % 100 == 0 and not(year % 400 == 0)):
    print(year, "is a leap year")
   else:
    print(year, "is not a leap year")


leap_year(int(var_leap))

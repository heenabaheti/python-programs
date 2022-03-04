"""
   program to show where the given year is leap year or not
"""

var = input("Enter Year which you want to check :")
if len(var) != 4:
 print(" please provide value in YYYY format  ")
 var = int(input("Enter your value again in YYYY format:"))


def leap_year(year):
   if year % 4 == 0 and not(year % 100 == 0 and not(year % 400 == 0)):
    print(year, "is a leap year")
   else:
    print(year, "is not a leap year")


leap_year(int(var))


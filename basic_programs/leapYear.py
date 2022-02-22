var_leap = input("Enter Year which you want to check :")
if len(var_leap) != 4:
 print(" please provide value in YYYY format  ")
 var_leap = int(input("Enter your value again in YYYY format:"))


def leap_year(var):
   if var % 4 == 0:
    print(var, "is a leap year")
   else:
    print(var, "is not a leap year")


leap_year(int(var_leap))

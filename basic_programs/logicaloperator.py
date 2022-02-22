num1 = 10
num2 = 10
num3 = -10


#logical And Operator
''' Returns True if both statements are true'''
if num1 > 0 and num2 > 0:
    print("The numbers are greater than 0")

if num1 > 0 and num2 > 0 and num3 > 0:
    print("The numbers are greater than 0")
else:
    print("numbers are not greater than 0")

#logical OR operator
'''Returns True if one of the statements is true'''

if num1 > 0 or num2 > 0:
    print("Either of the number is greater than 0")
else:
    print("No number is greater than 0")

# logical Not Operator
'''Reverse the result, returns False if the result is true'''
if not (num1 % 3 == 0 or num1 % 5 == 0):
    print("10 is not divisible by either 3 or 5")
else:
    print("10 is divisible by either 3 or 5")
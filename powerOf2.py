var_Num = int(input("Enter  number which lies from 1 to 31 "))
while var_Num < 0 or var_Num >= 31:
    print("Please enter correct input")
    var_Num = int(input("Enter  number which lies from 1 to 31 "))
i = 0
var_Power = 1
print("Table of powers of 2 is : ")
while i <= var_Num:
    print(i, var_Power)
    var_Power = 2 * var_Power
    i = i + 1



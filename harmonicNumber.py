var_Num = int(input("Enter Harmonic value  : "))
while var_Num <= 0:
    n = int(input("please enter greater than zero value : "))

var_Sum = 0.0
i = 1
while i <= var_Num:
    var_Sum += 1.0/i
    i = i+1

print("Nth Harmonic value :", round(var_Sum, 2))


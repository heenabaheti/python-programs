import math

"""program to print quadratic Equation"""

print("Quadratic Equation: a * x^2 + b * x + c")
a = int(input("Enter the value for a: "))
b = int(input("Enter the value for b: "))
c = int(input("Enter the value for c: "))

delta = pow(b, 2) - 4*a*c
print(delta)
"""method sqrt () returns the square root of x for x > 0. 
so if function has been used"""
if delta > 0:
    print("Two roots of x,  are :", end=" ")
    root1ofx = (((-b) + math.sqrt(delta))/(2*a))
    root2ofx = (((-b) - math.sqrt(delta))/(2*a))
    print(round(root1ofx, 2), "and", round(root2ofx, 2))
else:
    print("square root is not present")




import math

""" this program is taking two integer command line arguments x
and y and prints the Euclidean distance from the point (x, y) to the origin (0, 0). """
x = int(input("Enter the value for x : "))
y = int(input("Enter the value for y : "))
x2 = pow(x, 2)
y2 = pow(y, 2)
distance = math.sqrt(x2 + y2)
print("Euclidean Distance from", (x, y), "to Origin(0, 0) =", round(distance, 2))

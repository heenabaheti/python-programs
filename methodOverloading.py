"""program for method overloading """


# Takes two argument and print their sum
def addition(val1, val2):
    result = val1 * val2
    print(result)


# Takes three argument and print their sum
def addition(val1, val2, val3):
    result = val1 + val2 + val3
    print(result)

# the below line shows an error
addition(4, 5)

# This line will call the second product method
addition(4, 5, 5)

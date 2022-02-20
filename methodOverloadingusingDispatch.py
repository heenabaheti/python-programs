from multipledispatch import dispatch


# dispatch selects the appropriate method on bases of parameter passed'''
@dispatch(int, int, int)   # passing int parameters
def product(first, second, third):
    result = first * second * third
    print(result)


# you can also pass data type of any value as per requirement
@dispatch(float, float, float)
def product(first, second, third):
    result = first * second * third
    print(result)


# calling product method with arguments
product(2, 3, 2)  # this will give output of 12
product(2.2, 3.4, 2.3)  # this will give output of 17.204

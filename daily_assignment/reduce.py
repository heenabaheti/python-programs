import functools

arr = [1, 3, 5, 6, 2]

print("The sum of the list elements is : ", end=" ")
print(functools.reduce(lambda a, b: a + b, arr))


"""A program for reading in 2D arrays of integers, doubles or
 boolean from standard input and printing them out to standard output"""


'''taking row & col size'''
row = int(input("Enter the size of row: "))
col = int(input("Enter the size of col: "))

# creating empty list and entering value into this
element = []
print("Enter Array Elements : ")
for val1 in range(row):
    # creating temp list for storing value
    temp = []
    for val2 in range(col):
        print("enter", val1+1, "row", val2+1, "col value:")
        temp.append(int(input()))
    element.append(temp)

# printing value from array
for val1 in range(row):
    for val2 in range(col):
        print(element[val1][val2], end=" ")
    print()


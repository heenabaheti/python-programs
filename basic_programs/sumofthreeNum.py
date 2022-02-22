"""a program to raed N numbers and count the
number of triplets that sum is exactly 0"""


# creating a function
def findTriplets(arr, num):
    tripletIsPresent = 0
    print("Triplets are : ", end=" ")
    for val1 in range(0, num - 2):
        for val2 in range(val1 + 1, num - 1):
            for val3 in range(val2 + 1, num):
                if arr[val1] + arr[val2] + arr[val3] == 0:
                    print(arr[val1], arr[val2], arr[val3], ",", end=" ")
                    tripletIsPresent += 1
    return tripletIsPresent

# creating a list & inserting value to it

number = int(input("Enter the size of Array : "))
array = []
print("Enter", number, "Element into the array : ")
for eachVal in range(0, number):
    enteredValue = int(input())
    array.append(enteredValue)

'''storing value which is returning by the function findTriplets into the count'''
isPresent = findTriplets(array, number)
if isPresent == 0:
    print("Not exist")
else:
    print("\nTotal Number of  triplet :", isPresent)

def binarySearch(array, search):
    """
    program to search a string using binary search tree method
    :param array: array in which string has to be search
    :param search: sting which you want to search
    :return: position of string where it found
    """

    position = 0
    length = len(array)
    while position <= length:
        mid = position + ((length - position) // 2)
        res = (search == array[mid])
        # res will store true or false value
        # Check if x is present at mid
        if res == 0:
            return mid - 1

        # If x greater, ignore left half
        if res > 0:
            position = mid + 1

        # If x is smaller, ignore right half
        else:
            length = mid - 1

    return -1


if __name__ == "__main__":

    arr = ["practice", "makes", "man", "perfect"]
    x = "man"
    result = binarySearch(arr, x)

    if result == -1:
        print("Element not present")
    else:
        print("Element found at index", result)

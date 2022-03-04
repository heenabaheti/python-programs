def bubbleSort(int_num):
    """
    sort integer numbers  list using bubble sort
    :param int_num: is a list of input values given by user
    :return: sorted list using bubble sort
    """

    length = len(int_num)
    # Traverse through all array elements
    for i in range(0, length - 1):
        for j in range(0, length - 1):
            # swapping if condition is true
           if int_num[j] > int_num[j + 1]:
               temp = int_num[j]
               int_num[j] = int_num[j + 1]
               int_num[j + 1] = temp
    return int_num


def main():
    values = []
    for i in range(1, 6):
        num = input(f"Enter your {i} value = ")
        values.append(num)
    print(f"your values are  : ", values)
    arr = bubbleSort(values)
    print("Sorted list is : ")
    print(arr)

if __name__ == "__main__":
    main()

def insertion_sort(array):
    """
    sorting string array using insertion method
    :param array: value of array which want to sort
    :return: sorted string
    """
    # loop over all the elements in the list
    for i in range(1, len(array)):

        val = array[i]
        # assigning array current position into to the val
        # assigning array (current position -1) position into to occur
        occur = i - 1
        while occur >= 0 and val < array[occur]:
            # move elements of list [0..i-1], that are greater than val
            array[occur + 1] = array[occur]
            occur -= 1
        array[occur + 1] = val

    return array


sample_string = input("Enter the string which you want to sort:")
arr = [i for i in sample_string]
sorted_arr = insertion_sort(arr)
print(f"String before sorting: {sample_string}")
print(f"Sorted String: {'  '.join(sorted_arr)}")


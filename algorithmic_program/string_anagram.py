from insertion_sort import insertion_sort
# importing insertion sort


def anagram(string_1, string_2):
    """
    One string is an anagram of another if the second is simply an rearrangement of the first
    :param string_1: your first string value
    :param string_2: your second string value
    :return: both string matches or not
    """
    list_1 = insertion_sort(string_1)
    list_2 = insertion_sort(string_2)
    position = 0
    matches = True
    while position < len(string_1) and matches:
        if list_1[position] == list_2[position]:
            position = position + 1
        else:
            matches = False

    return matches


def main():
    value_1 = input("Enter your first string = ")
    arr_1 = [i for i in value_1]     # creating list and putting string value into that one by one char
    value_2 = input("Enter your Second string = ")
    arr_2 = [i for i in value_2]
    output = anagram(arr_1, arr_2)
    if output:
        print(f"String {value_1} is anagram of string {value_2}")
    else:
        print(f"String {value_1} is not anagram of string {value_2}")

if __name__ == "__main__":
    main()


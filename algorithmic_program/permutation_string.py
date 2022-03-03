def permutation_string(new_string):
    if len(new_string) == 1:
        return new_string
    # Creating an empty list
    permutation_list = []
    for i in new_string:
        remaining = [j for j in new_string if j != i]

        for k in permutation_string(remaining):
            permutation_list.append(i + k)
    return permutation_list


def main():
    new_string = input("Enter a string: ")
    combinations = permutation_string(new_string)
    print(combinations)

if __name__ == "__main__":
    main()

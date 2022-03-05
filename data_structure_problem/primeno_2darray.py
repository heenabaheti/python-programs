def prime_no(hi, low):
    prime_list = []
    for num in range(hi, low):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                prime_list.append(num)
    return prime_list


def printing():
    new_array = []
    for i in range(0, 1000, 100):
        prime_num = prime_no(i, i + 100)
        new_array.append(prime_num)
    i = 0
    for j in range(0, 1000, 100):    # printing value of array
        print(f"The prime numbers in the range {j} to {j + 100} is :")
        print(new_array[i])
        i += 1
    return


def main():
    printing()

if __name__ == "__main__":
    main()
class Prime():
    def prime_number():
        """
        Take a range of 0 - 1000 Numbers and find the Prime numbers in that range.
        :return: prime number in the given range
        """
        number = int(input("Enter Number till you want prime number from 0 to 1000 "))
        prime_numbers = []
        for val in range(2, number + 1):
            flag = 0
            if val < 2:
                continue
            if val == 2:
                prime_numbers.append(2)
                continue
            for x in range(2, val):
                if val % x == 0:
                    flag = 1
                    break
            if flag == 0:
                prime_numbers.append(val)

        return prime_numbers

    def palingdrom(temp):
        """
        given prime numbers are palingdrom or not
        param temp: output of the prime number function
        :return: list of prime number
        """
        palingdrom = []
        maximum = max(temp)
        for num in range(0, maximum + 1):
            _num = num
            rev = 0
            while (_num > 0):
                dig = _num % 10
                rev = rev * 10 + dig
                _num = _num // 10
            if rev == num:
               palingdrom.append(num)
               continue

        return palingdrom


def main():
    pr = Prime
    arr = pr.prime_number()
    arr1 = pr.palingdrom(arr)
    print("Prime no are :", arr)
    print("palingdrom numbers are :", arr1)



if __name__ == "__main__":
    main()

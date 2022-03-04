def binary_to_decimal(binary_num):
      """
      converting binary number into the decimal number
      :param binary_num: binary value taking by user
      :return: decimal converted value
      """
      n = len(str(binary_num))
      result = 0
      for i in range(1, n + 1):
         result = result + int(binary_num[i - 1]) * 2 ** (n - i)
      result = str(result)
      print("The decimal of the given binary is ", result)
      return result


def decimal_to_binary(decimal_num):
    """
    converting decimal value into the binary value
    :param decimal_num: decimal value taken by user
    :return: converting decimal value in binary and returning result
    """
    decimal_num = int(decimal_num)
    i = 1
    result = 0
    while decimal_num > 0:
       rem = int(decimal_num % 2)
       result = result + (i * rem)
       decimal_num = int(decimal_num / 2)
       i = i * 10
    result = str(result)
    print("The binary of the given number is ", result)
    return result


def main():
   print("1 :- Enter 1 for Binary to Decimal Conversation")
   print("2 :- Enter 2 for Decimal to Binary Conversation")
   choice = int(input("Enter your choice"))
   if choice == 1:
      binary_num = input('Enter binary to be converted: ')
      binary_to_decimal(binary_num)
   else:
      decimal_num = input("Enter decimal to be converted: ")
      decimal_to_binary(decimal_num)


if __name__ == "__main__":
   main()


def binary_to_decimal(binary_num):
   n = len(str(binary_num))
   result = 0
   for i in range(1, n + 1):
      result = result + int(binary_num[i - 1]) * 2 ** (n - i)
   print("The decimal of the given binary is ", result, '.')
   return result


def decimal_to_binary(decimal_num):
   i = 1
   result = 0
   while decimal_num > 0:
       rem = int(decimal_num % 2)
       result = result + (i * rem)
       decimal_num = int(decimal_num / 2)
       i = i * 10
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
      decimal_num = int(input("Enter decimal to be converted: "))
      decimal_to_binary(decimal_num)


if __name__ == "__main__":
   main()


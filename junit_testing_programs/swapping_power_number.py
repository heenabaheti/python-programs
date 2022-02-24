# Importing binary_to_decimal(binary_num) method from binary_to_decimal file for Conversion to Binary Representation.
from binary_to_decimal import decimal_to_binary
from binary_to_decimal import binary_to_decimal


# Function for swap nibble
def swap(number):
    """
     taking integer number and converting them in binary number & Swapping the two nibbles
    :param number: binary number.
    :return: binary number after swapping nibbles.
    """
    return number[4:9] + number[0:4]


def main():
    decimal_num = input("Enter a decimal number to swap value: ")
    # Converting Decimal to Binary Representation
    binary_number = decimal_to_binary(decimal_num)
    str(binary_number)
    swapped_number = swap(binary_number)
    swapped_converted = binary_to_decimal(swapped_number)
    print(f"swapping nibbles is: {swapped_number}, Converted value is: {swapped_converted} ")


if __name__ == "__main__":
    main()

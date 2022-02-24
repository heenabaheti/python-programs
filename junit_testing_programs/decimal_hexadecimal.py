def decimal_to_hex(decimal):
    # Conversion table of remainders to
    # hexadecimal equivalent
    conversion_table = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4',
                        5: '5', 6: '6', 7: '7',
                        8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C',
                        13: 'D', 14: 'E', 15: 'F'}

    # function which converts decimal value
    # to hexadecimal value
    hexadecimal = ''
    while decimal > 0:
        remainder = decimal % 16
        hexadecimal = conversion_table[remainder] + hexadecimal
        decimal = decimal // 16

    return hexadecimal


def hex_to_decimal(hex_num):
    hex_decimal_conversion = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
                              'A': 10, 'a': 10, 'B': 11, 'b': 11, 'C': 12, 'c': 12, 'D': 13, 'd': 13, 'E': 14,
                              'e': 14, 'F': 15, 'f': 15}
    p = len(hex_num) - 1
    decimal = 0

    for c in hex_num:
        decimal += hex_decimal_conversion[c] * (16 ** p)
        p -= 1

    return decimal


def main():
    print("1 :- Enter 1 for decimal to Hex-Decimal Conversation")
    print("2 :- Enter 2 for hex-Decimal to decimal Conversation")
    choice = int(input("Enter your choice"))
    if choice == 1:
        any_num = int(input('Enter the Decimal value: '))
        hex_decimal = decimal_to_hex(any_num)
        print(f'Decimal of {any_num} is {hex_decimal}')

    else:
        any_num = input('Enter the hexadecimal value: ')
        decimal = hex_to_decimal(any_num)
        print(f'Decimal of {any_num} is {decimal}')


if __name__ == "__main__":
    main()

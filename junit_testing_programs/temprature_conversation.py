class Conversion:

    """
    program to Convert Temperature from Celsius to Fahrenheit and Fahrenheit to Celsius.
    :parameter degree - Unit provided by user to take the temperature.
    """

    @staticmethod
    def cel_to_feh(degree):  # Conversion from Celsius to Fahrenheit

        print("Conversion from Celsius to Fahrenheit:")
        fahrenheit = (degree * (9 / 5)) + 32
        print("{} Celsius = {} Fahrenheit".format(degree, fahrenheit))
        return degree, fahrenheit

    # Conversion from Fahrenheit to Celsius
    @staticmethod
    def feh_to_cel(degree):
        print("Conversion from Fahrenheit to Celsius:")
        celsius = (degree - 32) * (5 / 9)
        print("{} Fahrenheit = {} Celsius".format(degree, celsius))
        return degree, celsius


def main():
    print("Choose the unit of temperature as input")
    value = int(input("(Press '1' for Celsius to fahrenheit or '2' for Fahrenheit to celsius): "))
    # temp is an instance of class Conversion
    temp = Conversion()
    if value == 1:
        degree = float(input("Enter temperature in Celsius: "))
        temp.cel_to_feh(degree)
    else:
        degree = float(input("Enter temperature in Fahrenheit: "))
        temp.feh_to_cel(degree)


if __name__ == "__main__":
    main()


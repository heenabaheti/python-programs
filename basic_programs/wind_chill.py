def get_wind_chill(temp, speed):
    """
    Returns Effective Temperature as per Weather Service formula.
    :param temp: Weather temperature given by user.
    :param speed: Wind Speed given by user.
    :return: Wind Chill/ Effective temperature calculated by the formula
    """
    wind_speed = 35.74 + 0.6215 * temp + (0.4275 * temp - 3.75) * speed ** 0.16
    return wind_speed


def main():
    temp = int(input("Enter the temperature to get the effective temperature: "))
    speed = int(input("Enter the wind speed to get the effective temperature: "))
    if temp > 50 or temp < -50 or speed > 120 or speed < 3:
       print("value doesn't lie in between given range t!>50 and v from 3 to 120 ")
    else:
        print(" Effective Temperature is.", get_wind_chill(temp, speed))


if __name__ == "__main__":
    main()



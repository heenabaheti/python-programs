# import datetime


class Dayofweek:
    @staticmethod
    def day_of_week(m, d, y):
        """
       create dayOfWeek static function that takes a date as input and
        prints the day of the week that date falls on
        :parameter y - user given input
        :parameter m - user given input
        :parameter d -  user given Input.
        :return: Day starting from 0 in the week calculated using Gregorian calendar.
        """

        # for the Gregorian calendar.
        y0 = y - (14 - m) // 12
        x = y0 + (y0 // 4) - (y0 // 100) + (y0 // 400)
        m1 = m + 12 * ((14 - m) // 12) - 2
        d0 = (d + x + (31 * m1) // 12) % 7
        print(d0)
        # Creating a dictionary to print out the day in the week.
        day_dict = {0: 'Sunday', 1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday', 5: 'Friday', 6: 'Saturday'}
        return day_dict[d0]


def main():
    year = int(input('Enter a year: '))
    month = int(input('Enter a month: '))
    day = int(input('Enter a day: '))

    _day = Dayofweek()  # _day is an instance of class Dayofweek
    day_of_the_week = _day.day_of_week(month, day, year)
    print(day_of_the_week)


if __name__ == "__main__":
    main()

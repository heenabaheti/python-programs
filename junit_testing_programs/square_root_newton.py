class SquareRoot:

    @staticmethod
    def square_root(c):
        """
        Calculates Square Root of the given non-negative number by user using Newton's method.
        :param c: non-negative number provided by the user.
        :return: square root of given number.
        """
        epsilon = 1e-15
        t = c    # initialization
        while abs(t - c / t) > epsilon * t:
            t = (c / t + t) / 2
        return t


def main():
        c = abs(int(input("Enter a non negative number: ")))
        sq = SquareRoot()
        # sq is an instance of class square root
        square = sq.square_root(c)
        # calling & storing value in param(square) returning by square_root method
        print("Square root of non negative is ", square)


if __name__ == "__main__":
    main()

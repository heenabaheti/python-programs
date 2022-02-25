class GuessGame:
    @staticmethod
    def find_value():
        """
        takes a command-line argument N, asks you to think of a number between 0 and N-1,
        where N = 2^n, and always guesses the answer with n questions
        :return: > Print the intermediary number and the final answer
        """
        low = 0
        high = 100
        while low != high:
            mid = (low + high) // 2
            print("enter 1 if no is between ", low, " - ", mid, "\nEnter 2 if no is between ", (mid + 1), " - ", high)
            choice = int(input("1 or 2 : "))
            if choice == 1:
                high = mid
            else:
                low = mid + 1
        return low


def main():
    int(input("guess a no between 0 to 100 "))
    game = GuessGame
    value = game.find_value()
    print("guessed no is ", value)

if __name__ == "__main__":
    main()

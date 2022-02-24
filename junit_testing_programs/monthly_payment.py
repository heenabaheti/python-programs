
def monthly_payment(rate, year, principal):
    """
    Calculates Monthly Payment Amount for Loan of given Principal, Years and Rate of interest.
    :param R: Rate of Interest of Loan provided by user.
    :param Y: Years of Loan provided by the user.
    :param P: Principal Amount taken as a Loan by the user
    :return: monthly payment upon loan
    """
    r = rate / 1200
    n = 12 * year
    payment = principal * r / (1 + r) ** (-n)
    print(f"Monthly Payment upon take amount {principal} = ", payment)
    return payment


def main():
    # taking input from user
    _rate = int(input("please enter interest rate = "))
    _year = int(input("enter year to pay off = "))
    _principal = int(input("enter principal loan amount = "))
    print()
    monthly_payment(_rate, _year, _principal)


if __name__ == main():
    main()

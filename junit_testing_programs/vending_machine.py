def return_change(amount):
    """
    Returns balance in coins.
    """
    coin = [1000, 500, 200, 100, 50, 20, 10, 5, 1]
    print("**************")
    print("currency Change ")
    change = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    for key, value in zip(coin, change):
        if amount >= key:
            value = amount // key
            amount = amount - value * key
            change.append(value)
            # change[coin.index(key)] += 1
        print(key, " : ", value)


def main():
    money = int(input("Enter amount"))
    # money = 337
    return_change(money)
    # assert return_change(money) == money

if __name__ == "__main__":
    main()






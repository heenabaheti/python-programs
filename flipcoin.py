import random
num_of_flip = int(input("Enter the number of coin to be flipped: "))
if num_of_flip <= 0:
 print("Please enter only positive number..!")
 num_of_flip = int(input("Enter the number of coin to be flipped: "))


def flipCoin(no_flip):
    heads = 0
    tails = 0

    for i in range(no_flip):
        coin = random.random()
        if coin < 0.5:
            heads += 1
        else:
            tails += 1
    head_percentage = float(heads) * (100/no_flip)
    tail_percentage = float(tails) * (100/no_flip)
    print("Total Number of Heads    :", heads)
    print("Total Number of Tails    :", tails)
    print("Percentage of Head       :", round(head_percentage, 2))
    print("Percentage of Tail       :", round(tail_percentage, 2))


flipCoin(num_of_flip)

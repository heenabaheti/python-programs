import random
import sys

# created dict. for snake bite if snake bites your position goes down
snake = {
     18: 2,
     26: 10,
     32: 12,
     39: 5,
     48: 26,
     51: 6,
     56: 1,
     60: 23,
     62: 17,
     75: 28,
     83: 45,
     88: 24,
     90: 48,
     92: 25,
     97: 78,
}

# created dict. for ladder if you got ladder your position goes up
ladder = {
         1: 38,
         4: 14,
         8: 30,
         28: 76,
         21: 42,
         50: 67,
         71: 93,
         80: 99
}

# created list for printing msg after snake bite and getting ladder
snake_bite = ["boohoo, not again!", "oh no its snake bite"]
ladder_jump = ["wow, its Ladder", "hurray, time to climb"]

start_Position = 0
Win_point = 100
# new_position = 0


# this function is taking name of players
def get_player_names():
    player1_name = input("Enter first Player Name ").strip()
    player2_name = input("Enter second Player Name ").strip()
    return player1_name, player2_name


# getting dice value
def get_dice_value():
    dice_value = random.randint(1, 6)
    print("Its a " + str(dice_value))
    return dice_value


def got_snake_bite(old_value, current_value, player_name):
    print("\n" + random.choice(snake_bite))
    print("\n" + player_name + " got a snake bite. Down from " + str(old_value) + " to " + str(current_value))


def got_ladder_jump(old_value, current_value, player_name):
    print("\n" + random.choice(ladder_jump))
    print("\n" + player_name + " climbed the ladder from " + str(old_value) + " to " + str(current_value))


# checking snake/ladder is there on position
def snake_ladder(player_name, current_value, dice_value):
    old_value = current_value
    current_value = current_value + dice_value

    if current_value > Win_point:
        print("You need " + str(Win_point - old_value) + " to win this game. Next turn.")
        return old_value

    print("\n" + player_name + " moved from " + str(old_value) + " to " + str(current_value))
    if current_value in snake:
        final_value = snake.get(current_value)
        got_snake_bite(current_value, final_value, player_name)
    elif current_value in ladder:
        final_value = ladder.get(current_value)
        got_ladder_jump(current_value, final_value, player_name)
    else:
        final_value = current_value

    return final_value


# checking win position
def check_win(player_name, position):
    if Win_point == position:
        print("Congratulations " + player_name + " won the game.")
        sys.exit(1)


def start():
    player1_name, player2_name = get_player_names()
    player1_current_position = 0
    player2_current_position = 0

    while True:

       # input("\n" + player1_name + ":   press enter to roll dice: ")
        dice_value = get_dice_value()
        player1_current_position = snake_ladder(player1_name, player1_current_position, dice_value)
        check_win(player1_name, player1_current_position)

        # input("\n" + player2_name + ":  press enter to roll dice: ")
        dice_value = get_dice_value()
        player2_current_position = snake_ladder(player2_name, player2_current_position, dice_value)
        check_win(player2_name, player2_current_position)


if __name__ == "__main__":
    start()

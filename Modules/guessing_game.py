import sys
from random import randint


def is_an_int(num_str):

    # if there is a signed number isdigit method sees it as str
    # eliminate the sign
    if num_str[0] == "-" or num_str[0] == "+":
        return num_str[1:].isdigit()

    else:
        return num_str.isdigit()


def get_valid_input(lower_limit,upper_limit):
    while True:
        guess = input(f"enter an integer in range [{lower_limit},{upper_limit}]")
        if is_an_int(guess):
            guess = int(guess)
            if lower_limit <=guess <= upper_limit:
                return guess
            else:
                print("enter an integer in the correct range")

        else:
            print("enter an integer!")


def guessing_game(lower_limit,upper_limit,guess_limit):

    number = randint(lower_limit,upper_limit)
    curr_guess_num = 0
    playing = True

    while playing:
        curr_guess_num += 1

        # max guess limit has been reached
        # stop the game
        if curr_guess_num == guess_limit:
            print(f"you lost the number was {number}")
            playing = False

        else:
            # forces user to enter a valid input
            guess = get_valid_input(lower_limit,upper_limit)

            if guess == number:
                print(f"congrats you won on your {curr_guess_num} try")
                playing = False
            elif guess > number:
                print("try a smaller number")
            else:
                print("try a bigger number")


if __name__ == "__main__":
    guessing_game(int(sys.argv[1]), int(sys.argv[2]),8)
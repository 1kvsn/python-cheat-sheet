# do_stuff function is for the tests written in test.py

def do_stuff(num):
    try:
        if num or num == 0:
            return int(num) + 5
        else:
            return 'please enter a number'
    except ValueError as err:
        return err

# ==============================================================

# Number Guessing Game
# Tests written in file named test_guessing_game.py

import random

def run_guess(guess, answer):
    if  0 < guess < 11:
        if guess == answer:
            print('you are a genius!')
			# used this returned True for Test assertion and also this replaced break
            return True # WE USED THIS BOOLEAN TO BREAK OUT OF THE LOOP BELOW
    else:
        print('hey bozo, I said 1~10')
		# again, this helps while assertion
        return False

if __name__ == '__main__': # this ensures the game doesn't run when the tests are run
    answer = random.randint(1, 10)
    while True:
        try:
            guess = int(input('guess a number 1~10:  '))
			# USING THE BOOLEAN TO BREAK OUT OF THE LOOP
            if (run_guess(guess, answer)):
                break
        except ValueError:
            print('please enter a number')
            continue

# =========================================================================================
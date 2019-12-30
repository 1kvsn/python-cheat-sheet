# Number guessing game

# How to play ?
	#- Open terminal in the directory containing this file, run the file using command `python3 [this_file_name.py] [argument1] [argument2]`. No need to include square brackets.
	# if argument1 is 1 and argument2 is 100, then you'll have to guess the number between 1 and 100

from random import randint
# you will need to run this on your machine and not this website for the sys.argv to work!
import sys

r1 = int(sys.argv[1])
r2 = int(sys.argv[2])
answer = randint(r1, r2)

while True:
    try:
        guess = int(input(f'guess a number {r1}~{r2}:  '))
        if  r1 < guess < r2:
            if guess == answer:
                print('you are a genius!')
                break
        else:
            print('hey bozo, I said 1~10')
    except ValueError:
        print('please enter a number')
        continue

# =============================================================================
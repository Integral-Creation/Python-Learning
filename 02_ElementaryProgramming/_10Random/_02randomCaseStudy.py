import random

lowest_num = 1
highest_num = 100

answer = random.randint(lowest_num, highest_num)
guesses = 0

is_running = True

print("Python Number Guessing Game")
print(f"Select a number between {lowest_num} and {highest_num}")

while is_running:
    guess = input('Enter your guess: ')

    if guess.isdigit():
        guess = int(guess)
        guesses += 1

        if guess < lowest_num or guess > highest_num:
            print("that number is out of range")
            print(f"Please select a number between {lowest_num} and {highest_num}")
        elif guess < answer:
            print("Too low! Try again!")
        elif guess > answer:
            print("Too high! Try again")
        else:
            print(f"CORRECT! the answer was {answer}")
            print(f"NUmber of guesses: {guesses}")
            is_running = False

    else:
        print("Invalid guess")
        print(f"Please select a number between {lowest_num} and {highest_num}")

"""
Output:
        Python Number Guessing Game
        Select a number between 1 and 100
        Enter your guess: 5
        Too low! Try again!
        Enter your guess: 45
        Too low! Try again!
        Enter your guess: 67
        Too low! Try again!
        Enter your guess: 78
        Too high! Try again
        Enter your guess: 69
        Too low! Try again!
        Enter your guess: 75
        CORRECT! the answer was 75
        NUmber of guesses: 6
"""
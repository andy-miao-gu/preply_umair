import random

def start_game():
    target_number = random.randint(1, 100)
    attempts = 0
    return target_number, attempts

def guess(target_number, guess_number):
    attempts = 1
    if guess_number < target_number:
        return "Too low! Try again.", attempts
    elif guess_number > target_number:
        return "Too high! Try again.", attempts
    else:
        return "Congratulations! You guessed it right.", attempts

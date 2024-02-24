# game_logic.py
import random

def generate_random_number():
    return random.randint(1, 100)

def is_guess_correct(target_number, user_guess):
    return user_guess == target_number

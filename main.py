# main.py
import random

def generate_random_number():
    return random.randint(1, 100)

def get_user_guess():
    try:
        guess = int(input("Enter your guess (between 1 and 100): "))
        return guess
    except ValueError:
        print("Invalid input. Please enter a number.")
        return get_user_guess()

def play_game():
    print("Welcome to Eaddaa Game!")
    target_number = generate_random_number()
    attempts = 0

    while True:
        user_guess = get_user_guess()
        attempts += 1

        if user_guess < target_number:
            print("Guess a larger number.")
        elif user_guess > target_number:
            print("Guess a smaller number.")
        else:
            print(f"Congratulations! You found the correct number in {attempts} attempts.")
            break

if __name__ == "__main__":
    play_game()

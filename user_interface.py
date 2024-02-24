# user_interface.py
def get_user_guess():
    try:
        guess = int(input("Enter your guess (between 1 and 100): "))
        return guess
    except ValueError:
        print("Invalid input. Please enter a number.")
        return get_user_guess()

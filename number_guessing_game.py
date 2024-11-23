import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    lower_bound = 1
    upper_bound = 100
    number_to_guess = random.randint(lower_bound, upper_bound)
    attempts = 0

    print(f"\nI have picked a number between {lower_bound} and {upper_bound}. Can you guess it?")
    
    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1
            if guess < number_to_guess:
                print("Too low! Try again.")
            elif guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed it in {attempts} attempts.")
                break
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    number_guessing_game()

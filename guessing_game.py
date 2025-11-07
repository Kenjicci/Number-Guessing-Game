import random

"""
Pseudocode for a guessing game:
1. Start the game
2. Get input for lower and upper bounds
3. Generate a random number between the bounds
4. Start a loop to allow user guesses
5. For each guess:
    a. Check if the guess is correct
    b. If correct, congratulate the user and end the game
    c. If incorrect, provide feedback (too high or too low)
"""

def guessing_game():

    lower_bound = int(input("Enter the lower bound: "))
    upper_bound = int(input("Enter the upper bound: "))

    random_number = random.randrange(lower_bound, upper_bound)

    while True:
        guess = int(input(f"Guess a number between {lower_bound} and {upper_bound}: "))

        if guess == random_number:
            print("Congratulations! You've guessed the correct number.")
            break
        elif guess < random_number:
            print("Too low! Try again.")
        elif guess > random_number:
            print("Too high! Try again.")
        
if __name__ == "__main__":
    guessing_game()
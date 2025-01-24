import random

# Generate a random number between 1 and 20
secret_number = random.randint(1, 20)

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 20. Can you guess it?")

# Initialize variables
guess = None
attempts = 0  # Counter to track the number of guesses

# Loop until the user guesses correctly
while guess != secret_number:
    try:
        # Ask the user for a guess and validate it
        guess = int(input("Enter your guess (1-20): "))

        # Check if the guess is within range
        if guess < 1 or guess > 20:
            print("Bruh, read the directions")
            continue  # Skip the rest of the loop and ask for input again

        # Increment the counter for valid guesses
        attempts += 1

        # Check the guess
        if guess < secret_number:
            print("MORE")
        elif guess > secret_number:
            print("Whoa, too much")
        else:
            print(f"Way to go! It only took you {attempts} attempts...")

    except ValueError:
        # Handle non-numeric input
        print("I said a NUMBER. Oye")
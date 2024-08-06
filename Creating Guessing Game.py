# Build a program that generates a random number and challenges the user to guess it. The program should prompt the
# user to input their guess, compare it to the generated number, and provide feedback if the guess is too high or too
# low. It should continue until the user correctly guesses the number and then display the number of attempts it took
# to win the game.



import random


def guess_the_number():
    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)

    attempts = 0
    guess = None

    print("Welcome to the Guess the Number game!")
    print("I'm thinking of a number between 1 and 100.")

    while guess != number_to_guess:
        try:
            # Prompt the user for their guess
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < number_to_guess:
                print("Too low! Try again.")
            elif guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number {number_to_guess} correctly.")
                print(f"It took you {attempts} attempts to guess the number.")

        except ValueError:
            print("Please enter a valid integer.")


def main():
    while True:
        guess_the_number()
        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            print("Thanks for playing! Goodbye.")
            break


if __name__ == "__main__":
    main()


# guess 73
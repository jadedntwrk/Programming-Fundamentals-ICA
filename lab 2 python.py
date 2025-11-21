#2025/11/11 Daniel Di Traglia 000882895
import random

# Print name and student number
print("Name: Daniel Di Traglia | Student Number: 000882895")

def play_game():
    #'secret_number' value generated randomly to be guessed by user
    secret_number = random.randint(1, 100)
    attempts = 0

    print("\nI'm thinking of a number between 1 and 1000.")

    while True:
        #Test to pass; 1,2,12,24,50... valid numbers between 1-100
        #test to fail: abcdef... 0,250,101,5.5... non numeric values and or out of range
        #user_input: raw input entered by the user before validation
        user_input = input("Enter your guess: ")

        #validate input: is the user input a numeric value?
        if not user_input.isdigit():
            print("Invalid input! Please enter a number between 1 and 100.")
            continue

        
        #guess; current user input/guess after validation
        guess = int(user_input)
        #validate: is the user input value between 1-100?
        if guess < 1 or guess > 100:
            print("Out of range! Guess must be between 1 and 100.")
            continue

        #'attempts' valid guess, increment counter +1 = total number of guesses

        attempts += 1 

        #Check guess comparitively to secret number
        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Correct! The secret number was {secret_number}.")
            print(f"You guessed it in {attempts} valid attempt(s).")
            break

def main():
    while True:
        play_game()
        #test 'again'; exit or continue? pass 'no' 'n' =  exit
        #test 'again'  fail; any input other than 'no' or 'n' = run module/routine again
        again = input("\nWould you like to play again? (yes/no): ").strip().lower()

        if again in ('no', 'n'):
            print("👋 Thanks for playing! Goodbye.")
            break

if __name__ == "__main__":
    main()

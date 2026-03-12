import random

def main():
    secret_number = random.randint(1, 100)
    attempts = 0
    guessed = False

    print("=== Welcome to Guess the number game. ===")
    print("I've random 1 to 100 can you guess it?")

    while not guessed:
        try:
            user_guess = int(input("\n enter your guess number: "))
            attempts += 1

            if user_guess < secret_number:
                print("Too low!")
            elif user_guess > secret_number:
                print("Too much!")
            else:
                print(f"Congratulation! the secret number is {secret_number}")
                print(f"You've tried {attempts} times")
                guessed = True

        except ValueError:
            print("Please enter number only")

if __name__ == "__main__":
    main()
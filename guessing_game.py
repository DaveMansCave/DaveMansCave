import random

def guessing_game():
    answer = random.randint(1, 53)  # Use randint for inclusive range
    tries = 4

    while tries > 0:
        try:
            guess = int(input("Guess a number between 1 and 53: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue  # Go to the next iteration of the loop
        
        if guess == answer:
            print("Wow, you got it right!")
            return  # Exit the function since they won

        if guess > answer:
            print("Your guess is high")
        else:
            print("Your guess is low")

        tries -= 1  # Decrement tries
        print(f"You have {tries} tries left.")

    print(f"You ran out of tries. The answer was {answer}.")

guessing_game()

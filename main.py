import random

number = random.randint(1, 100)

print("🎮 Welcome to Number Guessing Game")

while True:
    try:
        guess = int(input("Enter your guess (1-100): "))

        if guess == number:
            print("🎉 You guessed it right!")
            break
        elif guess < number:
            print("Too low 🔻")
        else:
            print("Too high 🔺")

    except ValueError:
        print("Please enter a valid number!")
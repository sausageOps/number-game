import random

print("=" * 30)
print("🎮 Number Guessing Game")
print("=" * 30)

while True:
    choice = input("Choose difficulty (easy / medium / hard): ").lower()

    if choice == "easy":
        max_num = 50
    elif choice == "medium":
        max_num = 100
    else:
        max_num = 200

    number = random.randint(1, max_num)
    max_attempts = 7
    attempts = 0

    while attempts < max_attempts:
        try:
            guess = int(input(f"Enter your guess (1-{max_num}): "))
            attempts += 1

            if guess == number:
                print(f"🎉 You guessed it in {attempts} attempts!")
                break

            elif guess < number:
                print("Too low 🔻")
            else:
                print("Too high 🔺")

            if abs(number - guess) <= 5:
                print("🔥 Very close!")

        except ValueError:
            print("Please enter a valid number!")

    else:
        print(f"💀 Game Over! The number was {number}")

    again = input("Play again? (y/n): ")
    if again != "y":
        print("Thanks for playing!")
        break
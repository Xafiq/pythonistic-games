import random

mystery_number = random.randint(1, 100)
max_attempts = 5

print("*** The Mystery Number Game! ***")
print(f"You have {max_attempts} attempts left.")

for attempts_left in range(max_attempts, 0, -1):
    guess = input("Guess the number: ")

    if not guess.isdigit():
        print("Please enter a valid number.")
        continue

    guess = int(guess)
    print(f"You have {attempts_left - 1} attempts left.")

    if guess == mystery_number:
        print(f"Congratulations! You found the mystery number in {max_attempts - attempts_left + 1} attempts.")
        break
    print("The mystery number is higher." if guess < mystery_number else "The mystery number is lower.")
else:
    print(f"Too bad! The mystery number was {mystery_number}.")
    print("Game over.")

#Xafiq
guess = int(input("What is your guess?: "))
correct_number = 5

guess_count = 1

while guess != correct_number:
    if guess < correct_number:
        guess = int(
            input("Wrong. You need to guess higher. What is your guess?: "))
    else:
        guess = int(
            input("Wrong. You need to guess lower. What is your guess?: "))
    guess_count += 1

print(
    f"Congrats! The right answe was {correct_number}. It took you {guess_count} guesses.")

import time
import random

name = input('Welcome to the gussing game!  \n What is your name?: ')

def entername():
    if len(name) <= 0:
        print("You did not enter your name.  Please try again.")
    exit()

def yourname():
    print(f"Hi {name}. I'm going to pick a number between 1 and 100.")
    time.sleep(2)
    print("Hold on a second while I pick a number...")
    time.sleep(5)

def pick():
    guess = int(input("What is your guess?: "))
    correct_number = random.randint(1, 100)
    guess_count = 1

    try:
        while guess != correct_number:
            if guess < correct_number:
                guess = int(
                    input("Wrong. You need to guess higher. What is your guess?: "))
            else:
                guess = int(
                    input("Wrong. You need to guess lower. What is your guess?: "))
            guess_count += 1

        print(f"\n CONGRATS {name.upper()}! The correct number is {correct_number}. \
            \n It took you {guess_count} guesses.")
    except:
        print("You did not make a guess.  Please restart the game.")

if __name__ == "__main__":
    entername()
    yourname()
    pick()
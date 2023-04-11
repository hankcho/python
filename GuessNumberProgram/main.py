import time
import random

self = input('Welcome to the gussing game!  \n What is your name?: ')

def name():
    print(f"Hi {self}. I'm going to pick a number between 1 and 100.")
    time.sleep(2)
    print("Picking a number...")
    time.sleep(5)

def pick():
    guess = int(input("What is your guess?: "))
    correct_number = random.randint(1, 100)
    guess_count = 1

    while guess != correct_number:
        if guess < correct_number:
            guess = int(
                input("Wrong. You need to guess higher. What is your guess?: "))
        else:
            guess = int(
                input("Wrong. You need to guess lower. What is your guess?: "))
        guess_count += 1

    print(f"\n CONGRATS {self.upper()}! The correct number is {correct_number}. \
          \n It took you {guess_count} guesses.")
    # print("CONGRATS " + self.upper()) 

if __name__ == "__main__":
    name()
    pick()
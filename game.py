import random

while True:
    try:
        level = int(input("Level: "))
        if level > 0:
            break
        else:
            level = int(input("Level: "))
    except ValueError:
        continue

secretNumber = random.randint(1, level)

guess = None

while guess != secretNumber:
    try:
        guess = int(input("Guess: "))
    except ValueError:
        continue

    if guess == secretNumber:
        print("Just Right!")
    if guess > secretNumber:
        print("Too large!")
    if guess < secretNumber:
        print("Too small!")

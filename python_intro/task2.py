import random

random_number = random.randint(0, 9)

guesses = []
while True:
    x = int(input("What is your guess? "))
    guesses.append(x)
    if x == random_number:
        print("Number of attempts:", len(guesses))
        print(f"Guesses: {guesses}")
        break

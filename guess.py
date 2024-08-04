import random

guesses_taken = 0

print("Hey! What's your name?")
name = input()
number = random.randint(1, 20)
print(f"so {name}, I'm guessing the number")

for guesses_taken in range(6):
    print("try to guess")
    guess = int(input())

    if guess > number:
        print("your number is bigger than mine")

    if guess < number:
        print("your number is smaller than mine")

    if guess == number:
        break

if guess == number:
    guesses_taken = str(guesses_taken + 1)
    print(f"great {name}, you did it in {guesses_taken} tries")

if guess != number:
    print(f"Alas, I had a number {number} in mind")

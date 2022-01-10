import random

hello

def guess(a, b):
    secret_number = random.randint(a, b)
    
    guess = int(input(f"Please guess a number from {a} to {b}: "))
    print(guess)
    
    while (guess != secret_number):
        if (guess < secret_number):
            guess = int(input("Too low, try again: "))
        else:
            guess = int(input("Too high, try again: "))
    print(f"Congratulations!!! You have guess {secret_number} correctly.")

print("Hello")
a, b = [int(c) for c in input("Specify number range: ").split()]


guess(a, b)




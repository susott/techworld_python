
# EXERCISE 6: Python Program 'Guessing Game'

# Write a program that:

#     runs until the user guesses a number (hint: while loop)
#     generates a random number between 1 and 9 (including 1 and 9)
#     asks the user to guess the number
#     then prints a message to the user, whether they guessed too low, too high
#     if the user guesses the number right, print out YOU WON! and exit the program

# Hint: Use the built-in random module to generate random numbers https://docs.python.org/3/library/random.html

# Concepts covered: Built-In Module, User Input, Comparison Operator, While loop

from random import randint

chosen_number = randint(1, 9)

while True:
    user_input = input('Please guess a number between 1 and 9.\n')

    try:
        guessed_number = int(user_input)
    except ValueError:
        print('Please insert a number')
        continue

    if guessed_number == chosen_number:
        print('YOU WON')
        break
    elif guessed_number < chosen_number:
        print(f"Guessed number {guessed_number} is too low.")
    else:
        print(f"Guessed number {guessed_number} is too high.")

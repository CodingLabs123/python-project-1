import random
from file import words


computer_choice1 = (random.choice(words))
computer_choice2 = set(computer_choice1)
guessed_letters = set()
while guessed_letters != computer_choice2:
    user_choice = input("guess a letter: ")
    guessed_letters.add(user_choice)
    print(f"the letter you have guessed: {', '.join(sorted(guessed_letters))}")
    display = ""
    for letter in computer_choice1:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    print(f"Word so far: {display}")
if guessed_letters == computer_choice2:
    print("You got it!")
else:
    print("Sorry, that's wrong try again.")





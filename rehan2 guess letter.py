import random
def  think (y):
    unknown_letter = random.choice (y)
    guess =0
    while guess != unknown_letter:
        guess = (input ('guess letter : '))
        if guess < unknown_letter:
            print ('your guess is not close')
        elif guess > unknown_letter:
            print ('your guess is way to close')
    print(f"congrates you have guessed the  letter {unknown_letter}")
think ( "abcdefghijk")
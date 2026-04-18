import random


def play():
    user = input("r rock, p paper, s scissor? ")
    computer = random.choice(["r", "p", "s"])

    if user == computer:
        return 'It is a tie!'

    if is_win(user, computer):
        return 'You won!'

    return 'You lose!'


def is_win(user, computer):
    if ( user== 'r' and computer == 's') or \
            (user == 's' and computer == 'p') or \
            (user == 'p' and computer == 'r'):
        return True
    return False


print(play())





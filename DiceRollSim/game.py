import random

def roll():
    return random.randint(1, 6)

def gamble(money, number_to_bet_on):
    n = roll()
    if n == number_to_bet_on:
        return f"You win ${money * 2}!"
    else:
        return "You Lose!"
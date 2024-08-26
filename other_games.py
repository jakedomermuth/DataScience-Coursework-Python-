import random
cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King', 'Ace', 'Joker']
suits = ['Diamonds', 'Spades', 'Hearts', 'Clubs']

dice_roll = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']

coin_flip = ['Heads', 'Tails']


def draw_card(card_input):
    if card_input == 'yes':
        card = random.choice(cards)
        suit = random.choice(suits)
        if card == 'Joker':
            return f'You Pulled a Joker!'
        return f'The {card} of {suit}'

    elif card_input == 'no':
        card_without = cards.copy()
        card_without.remove('Joker')
        card = random.choice(card_without)
        suit = random.choice(suits)
        return f'The {card} of {suit}'

    else:
        return 'Invalid input'

def roll_dice():
    return 2



def flip_coin():
        flip_result = random.choice(coin_flip)


import random
cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King', 'Ace', 'Joker']
suits = ['Diamonds', 'Spades', 'Hearts', 'Clubs']
dice_roll = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
coin_flip = ['Heads', 'Tails']


def game_choice(game_name, game_function):
    print(f"Starting the {game_name} game. Type 'quit' to exit at any time.")
    # letting the user know what game they selected and how to exit to hub
    while True:
        user_input = input('Press enter to play or type "quit" to exit: ')
        if user_input.lower() == 'quit':
            print(f"Exiting the {game_name} game...")
            break
            # breaking back to hub
        else:
            result = game_function()
            print(result)
            # playing whatever game was selected


def draw_card():
    card_input = input('Would you like a joker in the deck(yes/no) ')
    if card_input.lower() == 'yes':
        card = random.choice(cards)
        suit = random.choice(suits)
        # selecting a value and a suit from the list above to give a random card
        if card == 'Joker':
            return f'You Pulled a Joker!'
        # joker does not have a suit, so we need to catch and give a different output
        return f'The {card} of {suit}'

    elif card_input.lower() == 'no':
        card_without = cards.copy()
        # creating a new list so the original is not changed. Allows the game to be played multiple times and the user
        # can still have the option to include the joker card
        card_without.remove('Joker')
        card = random.choice(card_without)
        suit = random.choice(suits)
        return f'The {card} of {suit}'

    else:
        return 'Invalid input'


def roll_dice():
    num_of_sides = input('Select how many sides you want the dice to have: 6, 8, 10, 12 ')
    # using try and except to account for bad input
    # (we do not want an error ending the program because it an not become an integer)
    try:
        num_of_sides = int(num_of_sides)
        if num_of_sides in [6, 8, 10, 12]:
            dice_result = random.randint(1, num_of_sides)
            # using randint to select from list(allows selection to be dynamic)
            return f'You rolled a {dice_result} on a {num_of_sides} dice!'
        else:
            return 'Please choose: 6, 8, 10, 12'
            # catching input that can be an int, but not one of the correct numbers
    except ValueError:
        return 'Dice selection must be 6, 8, 10, or 12'


def flip_coin():
    return random.choice(coin_flip)
#refers to the list above

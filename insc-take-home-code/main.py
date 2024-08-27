from games import game_choice, flip_coin, roll_dice, draw_card
#importing functions


if __name__ == '__main__':
    #running hub option and selecting/playing a game until the user decides to exit
    while True:
        print('Welcome to the game hub!')
        game_input = input(
            'Would you like to flip a coin (1), roll a dice (2), or draw a card (3)? Type "quit" to exit: ')

        if game_input == '1':
            game_choice("Coin flip", flip_coin)
            # creating a name for printing purposes and calling the correct game function

        elif game_input == '2':
            game_choice("Dice roll", roll_dice)
            # creating a name for printing purposes and calling the correct game function

        elif game_input == '3':
            game_choice("Draw card", draw_card)
            # creating a name for printing purposes and calling the correct game function

        #Allowing user to exit the game hub
        elif game_input.lower() == 'quit':
            print('Thank you for playing!')
            break

        else:
            print('Invalid Selection. Please enter 1, 2, 3, or quit')
            print('Invalid Selection. Please enter 1, 2, 3, or quit')

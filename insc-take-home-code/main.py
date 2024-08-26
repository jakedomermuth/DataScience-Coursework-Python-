from other_games import draw_card, roll_dice, flip_coin

if __name__ == '__main__':
    while True:
        print('Welcome to the game hub')
        game_input = input('Would you like to flip a coin(1), roll a dice(2), or draw a card(3):' )

        if game_input == '1':
            while True:
                flip_result = flip_coin()
                print(flip_result)

        elif game_input == '2':
            while True:
                dice_input = input('Would you like a 6, 8, 10, or 12 sided dice: ')
                dice_result = roll_dice()
                print(dice_result)


        elif game_input == '3':
            while True:
                card_input = input('Would you like a Joker? yes or no ')
                card_result = draw_card(card_input)
                print(card_result)

        elif game_input == 'quit':
            break

        else:
            print('Invalid Selection. Please enter 1, 2, 3, or quit')
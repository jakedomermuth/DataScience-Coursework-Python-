import database


menu = '''\nPlease select one of the following options:
1. Add new game.
2. View upcoming game.
3. View all games.
4. Play a game.
5. View played games.
6. Exit

Your selection: '''
welcome = "Welcome to the Video Game Playlist App!"


print(welcome)
database.create_tables()


# <-------- Main, program starts here.
while (user_input := input(menu)) != "6":
    if user_input == "1":
        pass
    elif user_input == "2":
        pass
    elif user_input == "3":
        pass
    elif user_input == "4":
        pass
    elif user_input == "5":
        pass
    else:
        print("Invalid input. please try again.")

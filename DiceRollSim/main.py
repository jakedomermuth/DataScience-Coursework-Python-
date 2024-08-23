from game import roll, gamble

while True:
    print("Welcome")
    print("1. Roll a dice.\n2.Gamble on dice\n3. Exit")
    choice = input("Which do you choose? ")

    if choice == "1":
        n = roll()
        print(f"You rolled a {n}")
    elif choice == "2":
        money = float(input("How much do you want to bet? "))
        number_to_bet_on = int(input("What number do you want to bet on? "))
        print(gamble(money, number_to_bet_on))
    else:
        print("Exiting...")
        break

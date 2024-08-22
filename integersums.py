#Write a function, add_it_up(), that takes a single integer as input and returns the sum of the integers
#from zero to the input parameter.
#The function should return 0 if a non-integer is passed in.
non_int_return = 0

def add_it_up():
    int_sum = 0
    user_input = input('Select a Number ')
    try:
        user_input = int(user_input)
        while user_input != 0:
            int_sum = int_sum + user_input
            user_input -= 1
        print(int_sum)
    except ValueError:
        print(non_int_return)

add_it_up()



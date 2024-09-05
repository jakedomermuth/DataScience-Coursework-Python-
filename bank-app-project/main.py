from database import add_entry, get_entries, del_entry, get_last_entry

MENU = """
Welcome to the Banking App!

1. Add Entry
2. View Entries
3. Delete last entry
4. Exit


Selection: 
"""

# utility

def normalize(text):
    return text.strip().upper()


# prompt functions
def prompt_add_entry():
    content = input('How much money did you spend today? ')
    date = input("What is today's date ")
    return content, date

def prompt_view_entries():
    for row in my_data:
        print(f"{row['date']}: {row['content']}\n")

def prompt_del_entry(data_to_delete):
    a = normalize(input(f'Are you sure you want to delete {data_to_delete}\nSelection (Y/N)'))
    return a




while (user_input := input(MENU)) !='4':
    if user_input == '1':
        content, date = prompt_add_entry()
        add_entry(content, date)
    elif user_input == '2':
        my_data = get_entries()
        prompt_view_entries()
    elif user_input == '3':
        last_entry = get_last_entry()
        del_decision = prompt_del_entry(last_entry)
        if del_decision == 'Y':
            del_entry()

    else:
        print('Try Again')


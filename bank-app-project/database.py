

my_data = [] # {'content':content, 'date': date}


def add_entry(content, date):
    my_data.append({'content': content, 'date': date})

def get_last_entry():
    return my_data[-1]
def del_entry():
    my_data.pop()
#pop automatically removes the last entry

def get_entries():
    return my_data


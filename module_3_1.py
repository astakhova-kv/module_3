calls = 0

def count_calls():
    global calls
    calls += 1


def string_info(string):
    count_calls()
    my_list = []
    my_list.append(len(string))
    my_list.append(string.upper())
    my_list.append(string.lower())
    my_tuple = tuple(my_list)
    return my_tuple

def is_contains(string, list_to_search):
    count_calls()
    flag = False
    for i in list_to_search:
        if string.casefold() == i.casefold():
            flag = True
            break
    if flag == True:
        return True
    else:
        return False

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)
shopping_list = []


def show_help():
    print('''
    ==================================
    >  Enter  'DONE' to exit the app.
    >  Enter 'SHOW' to see your items.
    >  Enter 'HELP' to see help.
    >  Enter 'DEL' to remove item.
    >  Enter 'EDIT' to modify item.
    >  Enter 'CLEAR' to clear your list.
    ===================================
    ''')


show_help()


def show_list():
    print('Here is your shopping list')
    print("--------------------------")
    for index, item in enumerate(shopping_list):
        index += 1
        remove_white_space = str(item).replace(' ', '')
        print("{} {} ".format(index, remove_white_space.title()))
    print("__________________________________________________")
    if len(shopping_list) < 1:
        print("You haven't add anything yet in your shopping list")
    elif len(shopping_list) == 1:
        print("You have only {} item in your shopping list".format(len(shopping_list)))
    else:
        print("You have {} items in your shopping list".format(len(shopping_list)))


def edit_list():
    number = int(input("Number of the item to edit: "))
    number = number - 1
    new_todo = input("Enter new name: ")
    shopping_list[number] = new_todo


def delete_list():
    confirm = input("Are you sure you want to clear your list\n Y / N ")
    if confirm.upper() == 'Y':
        shopping_list.clear()
        print('You just cleared your shopping list\nStart adding')
    else:
        show_help()


def add_item(item):
    if item in shopping_list:
        print("=" * len(item))
        print(item, "!! already in the list.")
        print("=" * len(item))
        print('''
  ^ ^     
( o.o )
>> ^ <<
        ''')
    elif ',' in item:
        seperated = item.split(',')
        shopping_list.extend(seperated)
    else:
        shopping_list.append(item)


def remove_item():
    try:
        item_to_remove = input('What item you want to remove > ')
        shopping_list.remove(item_to_remove)
        print(item_to_remove, " remove from your list")

    except ValueError:
        print(item_to_remove, " is not available in your list")


while True:
    new_item = input("add item >>")

    if new_item.upper() == 'DONE':
        break
    if new_item.upper() == 'HELP':
        show_help()
        continue
    if new_item.upper() == 'SHOW':
        show_list()
        continue
    if new_item.upper() == 'EDIT':
        edit_list()
        continue
    if new_item.upper() == 'DEL':
        remove_item()
        continue
    if new_item.upper() == 'CLEAR':
        delete_list()
        continue
    add_item(new_item)

show_list()

# let user create new list with category name


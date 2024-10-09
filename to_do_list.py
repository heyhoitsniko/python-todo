import menu

todos = []

def tasklist():
    for i in range(len(todos)):
        item = todos[i]
        position = i + 1
        print(str(position)+ ". " + item)

    if len(todos) == 0:
        print("Your list is empty.")


def taskadd(entry):
    todos.append(entry)
    print("Added item:", entry)


def taskdel(arg):
    if len(todos) != 0: # todos list is not empty

        entry = arg
        if entry.isdigit(): # user entered a number (ie position in list)
            position = int(entry) - 1
            entry = todos[position] # set entry to the item at that position

        todos.remove(entry)
        print("Removed item:", entry)

    tasklist()

# def tasksel
#     if len(todos) != 0:  # todos list is not empty
#
#         entry = arg
#         if entry.isdigit():  # user entered a number (ie position in list)
#             position = int(entry) - 1
#             entry = todos[position]  # set entry to the item at that position


def process(command, arg):
    if command == "list":
        tasklist()
    elif command == "add":
        taskadd(arg)
    elif command == "get":
        if len(todos) > 0:
            position = int(arg) - 1
            print("item is", todos[position])
    elif command == "select":
        menu.selection = int(arg)
        # tasksel(arg)
    elif command == "deselect":
        menu.selection = None
    elif command == "del":
       taskdel(arg)
    else:
        print("Unknown input \"" + command + "\", please try again.")


menu.run(process)


import json
from functions import add_task, complete_task, delete_task, list_tasks, choice

while True:
    user_input = input("\nChoose between:\n1 - Add task\n2 - Complete task\n3 - Delete task\n4 - View tasks\nType 'q' to quit.\n\nYour choice:")

    if user_input.lower() == 'q':
        print("Goodbye !")
        break
    if user_input == '1':
        adding_task = input('What task do you wish to add?\n')
        add_task(adding_task)
        if choice() == 'quit':
            print("Goodbye!")
            break

    elif user_input == '2':
        completing_task = input('What task have you completed ?\n')
        completing_task = int(completing_task)
        complete_task(completing_task)
        if choice() == 'quit':
            print("Goodbye!")
            break

    elif user_input == '3':
        deleting_task = input('Which task would you like to delete?\n')
        deleting_task = int(deleting_task)
        delete_task(deleting_task)
        if choice() == 'quit':
            print("Goodbye!")
            break

    elif user_input == '4':
        list_tasks()
        if choice() == 'quit':
            print("Goodbye!")
            break

    else:
        print("Invalid input. Please choose 1, 2, 3, 4, or 'q'.")




import json
from functions import add_task, complete_task, delete_task, list_tasks

user_input = int(input("Choose between 1/2/3/4 to apply the code for adding/completing/deleting or viewing a task : "))

if user_input == 1:
    adding_task = input('What task do you wish to add?\n')
    add_task(adding_task)

elif user_input == 2:
    completing_task = input('What task have you completed ?\n')
    completing_task = int()
    complete_task(completing_task)

elif user_input == 3:
    deleting_task = input('Which task would you like to delete?\n')
    deleting_task = int()
    delete_task(deleting_task)

elif user_input == 4:
    list_tasks()




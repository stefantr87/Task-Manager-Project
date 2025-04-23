import json

def add_task(task_name):
    task = {}
    try:
        with open('tasks.json', 'r',encoding='utf-8') as f:
            tasks = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        tasks = []
    task = {
        'Task': task_name,
        'Status': 'Pending'
    }
    tasks.append(task)
    with open('tasks.json', 'w', encoding='utf-8') as f:
        json.dump(tasks, f, indent=4, ensure_ascii=False)
    print(f"Task '{task_name}' a fost adăugat cu succes!")

def complete_task(index):
    try:
        with open('tasks.json', 'r', encoding='utf-8') as f:
            tasks = json.load(f)
        tasks[index]['Status'] = ['Completed']
        with open('tasks.json', 'w', encoding='utf-8') as f:
            json.dump(tasks, f, indent=4, ensure_ascii=False)
        print(f"Task-ul {index} a fost marcat ca 'Completed'.")
    except (IndexError, FileNotFoundError, json.JSONDecodeError):
        print("Eroare: Task-ul nu există sau fișierul e invalid.")

def delete_task(index):
    try:
        with open('tasks.json', 'r', encoding='utf-8') as f:
            tasks = json.load(f)

        removed_task = tasks.pop(index)

        with open('tasks.json', 'w', encoding='utf-8') as f:
            json.dump(tasks, f, indent=4, ensure_ascii=False)
        print(f"Task-ul '{removed_task['Task']}' a fost șters cu succes!")
    except (IndexError, FileNotFoundError, json.JSONDecodeError):
        print("Eroare: Task-ul nu există sau fișierul e invalid.")

def list_tasks():
    with open('tasks.json', 'r',encoding='utf-8') as f:
        tasks = json.load(f)
    print(tasks)

def choice():
    choice = input('To quit the program type "q", for main menu press "m" : ')
    if choice.lower() == 'q':
        return 'quit'
    elif choice.lower() == 'm':
        return 'menu'
    else:
        print("Invalid choice, returning to menu.")
        return 'menu'
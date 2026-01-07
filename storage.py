import json

def load_tasks():
    try:
        with open('data/tasks.json', 'r') as file:
            Tasks = json.load(file)
    except (FileExistsError, json.JSONDecodeError):
        Tasks = []
    return Tasks
            
def save_tasks(Tasks):
    with open('data/tasks.json', 'w') as file:
        json.dump(Tasks, file, indent=4)

def add_tasks(title):
    Tasks = load_tasks()
    Tasks.append({'title':title, 'done':False})
    save_tasks(Tasks)
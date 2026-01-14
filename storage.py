import json

def load_tasks():
    try:
        with open('data/tasks.json', 'r') as file:
            Tasks = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        Tasks = []
    return Tasks
            
def save_tasks(tasks):
    with open('data/tasks.json', 'w') as file:
        json.dump(tasks, file, indent=4)

def add_tasks(tasks, title):
    tasks.append({'title':title, 'done':False})

def delete_tasks(tasks, index):
    if 0 <= index < len(tasks):
        del tasks[index]
        return True
    else:
        print("index invalide")
        return False

def edit_tasks(tasks, index, new_title, new_done):
    if 0 <= index < len(tasks):
        tasks[index]['title'] = new_title
        tasks[index]['done'] = new_done
        return True
    print('tache inexistante')
    return False

def clear_tasks(tasks):
    confirmer = input("Voulez-vous vraiment supprimer toutes les tâches ? (o/n) : ").lower()
    if confirmer == 'o':
        tasks.clear()
        save_tasks(tasks)
        print("Toutes les tâches ont été supprimées !")
    else:
        print("Suppression annulée.")

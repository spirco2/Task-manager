def list_tasks(tasks):
    if not tasks:
        print("aucune tache existante")
        return

    for i , task in enumerate(tasks):
        status = '✅' if task["done"] else '❌'
        print(f"{i}. {task['title']} [{status}]")
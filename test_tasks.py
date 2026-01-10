from storage import load_tasks, save_tasks, add_tasks, delete_tasks, edit_tasks, clear_tasks


tasks = load_tasks()
clear_tasks(tasks)

print("Toutes les tâches ont été supprimées !")

tasks = load_tasks()
print("initiale :", tasks)

add_tasks(tasks, "Tasks A")
add_tasks(tasks, "Tasks B")
save_tasks(tasks)
print("apres ajout :", tasks)
edit_tasks(tasks, 0, "Tâche A modifiée", True)
save_tasks(tasks)
print("Après modification :", tasks)

delete_tasks(tasks, 1)
save_tasks(tasks)
print("Après suppression :", tasks)
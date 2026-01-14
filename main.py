from storage import load_tasks, save_tasks
from tasks import list_tasks

def main():
    tasks = load_tasks()
    print("===Task Manager===")
    list_tasks(tasks)
    save_tasks(tasks)

if __name__ == "__main__":
    main()
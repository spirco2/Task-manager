from storage import load_tasks, save_tasks, add_tasks, delete_tasks, edit_tasks
from tasks import list_tasks

def main():
    while True:
        print("===Task Manager===")
        print("1.Afficher les taches")
        print("2.Ajouter des taches")
        print("3.Supprimer une tache")
        print("4.Modifier une tache")
        print("5.Quitter")
        
        choix = input("Choix : ")

        if choix == "1":
            tasks = load_tasks()
            list_tasks(tasks)

        elif choix == "2":
            title = input("title : ")
            add_tasks(title)
        
        elif choix == "3":
            indice = int(input("index : "))
            delete_tasks(indice)

        elif choix == "4":
            tasks = load_tasks()
            list_tasks(tasks)
            try:
                index = int(input("Entrez l'indice de la tache a modifier : "))
                new_title = input("Entrez votre titre : ")
                done_input = input("Tache termine?(o/n) : ")
                new_done = True if done_input.lower() == 'o' else False

                if edit_tasks(tasks, index, new_title, new_done):
                    save_tasks(tasks)
                    print("Tache modifier avec succes!!!")
            except ValueError:
                print("entre invalice")
        
        elif choix == "5":
            print("AU revoir")
            break

        else:
            print("choix invalide")


if __name__ == "__main__":
    main()


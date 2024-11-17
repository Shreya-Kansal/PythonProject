tasks = []
def add_task(task):
    tasks.append(task)
    print(f"task {task} added")

def view_tasks():
    if not tasks:
        print("task is not in list")
    else:
        for idx, task in enumerate(tasks,1):
            print(f"{idx}. {task}")

def remove_task(task_num):
    if 0 < task_num <= len(tasks):
        removed = tasks.pop(task_num - 1)
        print(f"task {removed} removed")
    else:
        print("invalid task number")

while True:
    print("\n To-Do List Menu:")
    print("1. Add Task")
    print("2. View Task")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("enter your choice(1-4):")   

    if choice == '1':
        task = input("enter the task:")
        add_task(task)

    elif choice == '2':
        view_tasks()  

    elif choice == '3':
        task_num = int(input("enter the task number to remove"))
        remove_task(task_num)   

    elif choice == '4':
        print("exiting the program")
        break
    else:
        print("Invalid choice. Please try again")      

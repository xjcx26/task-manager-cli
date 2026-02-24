import json
from datetime import datetime

def load_tasks():
    try:
        with open("tasks.json", "r") as file:
            tasks = json.load(file)
            for task in tasks:
                if "created_at" not in task:
                    task["created_at"] = "Unknown"
            return tasks
    except FileNotFoundError:
        return []

tasks = load_tasks()


def save_tasks(tasks):
    with open("tasks.json","w") as file:
        json.dump(tasks, file, indent=4)


def show_menu():
    print("\nPlease select one of the following options:")
    print("\n1. Add new task")
    print("\n2. View tasks")
    print("\n3. Mark task as completed")
    print("\n4. Delete a task")
    print("\n5. Clear completed tasks from list")
    print("\n6. Quit")


def add_task(tasks):
    task_input = input("\nPlease input the task you would like to add: ")
    task = {
        "title" : task_input,
        "completed": False,
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    tasks.append(task)
    save_tasks(tasks)
    print("Task Added!")
    view_tasks(tasks)


def view_tasks(tasks):
    if not tasks:
        print("No tasks to view.")
        return
    print("\nYour Tasks:")
    for i,task in enumerate(tasks, start=1):
        if task["completed"]:
            status = "[X]"
        else:
            status = "[ ]"
        print(f"{i}. {task['title']} - Completed: {status} - Created: {task['created_at']}")


def completed_task(tasks):
    if not tasks:
        print("No tasks to amend.")
        return
    view_tasks(tasks)

    try:
        completion_value = int(input("Which task would you like to mark as completed? "))

        if 1 <= completion_value <= len(tasks):
            if tasks[completion_value - 1]["completed"]:
                print("Task is already completed!")
            else:
                tasks[completion_value - 1]["completed"] = True
                save_tasks(tasks)
                print("Task is now marked as completed!")
                view_tasks(tasks)
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")


def delete_task(tasks):
    if not tasks:
        print("No tasks to amend.")
        return
    view_tasks(tasks)
    try:
        deletion_value = int(input("Which task would you like to delete from the list? "))

        if 1 <= deletion_value <= len(tasks):
            removed = tasks.pop(deletion_value - 1)
            save_tasks(tasks)
            print(f"Deleted task: {removed['title']}")
            view_tasks(tasks)
        else:
            print("Invalid choice!")
    except ValueError:
        print("Please enter a valid number.")

def clear_completed(tasks):
    if not tasks:
        print("No tasks to amend.")
        return
    view_tasks(tasks)
    clear_choice = input('"If you would like to clear the completed tasks, please input the letter "y":')
    if clear_choice.lower() == "y":
        og_count = len(tasks)
        tasks[:] = [task for task in tasks if not task["completed"]]
        removed_count = og_count - len(tasks)
        if removed_count > 0:
            save_tasks(tasks)
            print(f"{removed_count} completed tasks have been removed from the list.\nHere is the updated list:")
            view_tasks(tasks)
        else:
            print("No completed tasks to clear.")
    else:
        print("List has not been cleared.")


while True:
    print("Welcome to your Task List Program!")
    show_menu()
    choice = input("Please input your selection: ")
    
    if choice == "1":
        add_task(tasks)

    elif choice == "2":
        view_tasks(tasks)

    elif choice == "3":
        completed_task(tasks)

    elif choice == "4":
        delete_task(tasks)

    elif choice == "5":
        clear_completed(tasks)

    elif choice == "6":
        break

    else:
        print("Invalid Choice!")
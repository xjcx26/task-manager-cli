import json
from datetime import datetime

class TaskManager:
    def __init__(self, filename):
        self.filename = filename
        self.tasks = self.load_tasks()
    
    def save_tasks(self):
        with open(self.filename,"w") as file:
            json.dump(self.tasks, file, indent=4)

    def load_tasks(self):
        try:
            with open(self.filename, "r") as file:
                tasks = json.load(file)
                for task in tasks:
                    if "created_at" not in task:
                        task["created_at"] = "Unknown"
                return tasks
        except FileNotFoundError:
            return []
    
    def add_task(self, title):
        task = {
            "title" : title,
            "completed": False,
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.tasks.append(task)
        self.save_tasks()
        print("Task Added!")
        self.view_tasks()
        

    def view_tasks(self):
        if not self.tasks:
            print("No tasks to view.")
            return
        
        print("\nYour Tasks:")
        for i,task in enumerate(self.tasks, start=1):
            if task["completed"]:
                status = "[X]"
            else:
                status = "[ ]"
            print(f"{i}. {task['title']} - Completed: {status} - Created: {task['created_at']}")

    def completed_task(self, index): 
        if not self.tasks:
            print("No tasks to amend.")   
            return
        if not 1 <= index <= len(self.tasks):
            print("Invald task number.")
            return
        
        if self.tasks[index - 1]["completed"]:
            print("Task is already completed!") 
            return        
        
        self.tasks[index - 1]["completed"] = True
        self.save_tasks()
        print("Task is now marked as completed!")
        self.view_tasks()      

    def delete_task(self, index):
        if not self.tasks:
            print("No tasks to amend.")   
            return
        
        if not 1 <= index <= len(self.tasks):
            print("Invalid choice!") 
            return
        removed = self.tasks.pop(index - 1)
        self.save_tasks()
        print(f"Deleted task: {removed['title']}")
        self.view_tasks()
                          


    def clear_completed(self):
        if not self.tasks:
            print("No tasks to amend.")           
            return
        
        self.view_tasks()
        og_count = len(self.tasks)
        self.tasks[:] = [task for task in self.tasks if not task["completed"]]
        removed_count = og_count - len(self.tasks)
        self.save_tasks()
        print(f"{removed_count} completed tasks have been removed from the list.\nHere is the updated list:")
        self.view_tasks()

def show_menu():
    for key, option in actions.items():
        print(f"{key}. {option['label']}")
    print("6. Quit")

def pause():
    input("Press enter to return to menu...")
              
def handle_complete():
    manager.view_tasks()

    try:
        index = int(input("Which task number would you like to mark as complete?"))
        manager.completed_task(index)
    except ValueError:
        print("Please enter a valid number.")

def handle_clear():
    manager.view_tasks()

    try:
        confirm = input("Type 'y' to remove completed: ")

        if confirm.lower() == "y":
            manager.clear_completed()
        else:
            print("Operation cancelled.")
    except ValueError:
        print("Please enter a valid number.")

def handle_delete():
    manager.view_tasks()

    try:
        index = int(input("Please state the number of the task that you would like to remove:"))
        manager.delete_task(index)
    except ValueError:
        print("Please enter a valid number.")

manager = TaskManager("tasks.json")

actions = {
    "1" : {"label": "Add new task", "action": lambda: manager.add_task(input("Please input the task you would like to add: "))},
    "2" : {"label": "View tasks", "action":  manager.view_tasks},
    "3" : {"label": "Mark task as completed", "action": handle_complete},
    "4" : {"label": "Delete a task", "action":  handle_delete},
    "5" : {"label": "Clear completed tasks from list", "action":  handle_clear}
}

print("Welcome to your Task List Program!")

while True:
    show_menu()
    choice = input("Please input your selection: ")

    if choice == "6":
        break

    option = actions.get(choice)

    if option:
        option["action"]()
    else:
        print("Invalid Choice!")
        
    pause()
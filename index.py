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
        
    def get_tasks(self):
        return list(self.tasks) 

    def completed_task(self, index): 
        if not 1 <= index <= len(self.tasks):
            raise ValueError("Invalid Choice!")
        
        if self.tasks[index - 1]["completed"]: 
            return False    
        else:
            self.tasks[index - 1]["completed"] = True
            self.save_tasks()
            return True     

    def delete_task(self, index):
        
        if not 1 <= index <= len(self.tasks): 
            raise ValueError("Invalid Choice") 
        removed = self.tasks.pop(index - 1)
        self.save_tasks()
        return removed
                          
    def clear_completed(self):
        og_count = len(self.tasks)
        self.tasks[:] = [task for task in self.tasks if not task["completed"]]
        removed_count = og_count - len(self.tasks)
        self.save_tasks()
        return removed_count

def show_menu():
    for key, option in actions.items():
        print(f"{key}. {option['label']}")
    print("6. Quit")

def pause():
    input("Press enter to return to menu...")
              
def handle_complete():
    tasks = manager.get_tasks()
    display_tasks(tasks)
    try:
        index = int(input("Which task number would you like to mark as complete?"))
        result = manager.completed_task(index)
        if result:
            print("Task is now marked as completed!")
            display_tasks(manager.get_tasks())
        else:
            print("Task is already completed!")
    except ValueError as e:
        print(e)

def handle_clear():
    tasks = manager.get_tasks()
    display_tasks(tasks)
    try:
        confirm = input("Type 'y' to remove completed: ")

        if confirm.lower() == "y":
            removed = manager.clear_completed()
            print(f"{removed} completed tasks have been removed from the list.\nHere is the updated list:")
            display_tasks(manager.get_tasks())
        else:
            print("Operation cancelled.")
    except ValueError:
        print("Please enter a valid number.")

def handle_delete():
    tasks = manager.get_tasks()
    display_tasks(tasks)
    try:
        index = int(input("Please state the number of the task that you would like to remove:"))
        choice = manager.delete_task(index)
        print(f"Deleted task: {choice['title']}")
    except ValueError as e:
        print(e)

def handle_add():
    title = input("Please enter the task you would like to add: ")
    manager.add_task(title)
    print("Task Added!")
    tasks = manager.get_tasks()
    display_tasks(tasks)
    
def handle_view():
    display_tasks(manager.get_tasks())

def display_tasks(tasks):
    if not tasks:
        print("There are no tasks on record.")
    else:
        print("\nYour Tasks:")
        for i,task in enumerate(tasks, start=1):
            if task["completed"]:
                status = "[X]"
            else:
                status = "[ ]"
            print(f"{i}. {task['title']} - Completed: {status} - Created: {task['created_at']}")

manager = TaskManager("tasks.json")

actions = {
    "1" : {"label": "Add new task", "action": handle_add},
    "2" : {"label": "View tasks", "action":  handle_view},
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
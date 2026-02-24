import json
from datetime import datetime


def show_menu():
    print("\nPlease select one of the following options:")
    print("\n1. Add new task")
    print("\n2. View tasks")
    print("\n3. Mark task as completed")
    print("\n4. Delete a task")
    print("\n5. Clear completed tasks from list")
    print("\n6. Quit")

def pause():
    input("Press enter to return to menu...")

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
    
    def add_task(self):
        task_input = input("\nPlease input the task you would like to add: ")
        task = {
            "title" : task_input,
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

    def completed_tasks(self):
        if not self.tasks:
            print("No tasks to amend.")
            return   
        try:
            self.view_tasks()
            completion_value = int(input("Which task would you like to mark as completed? "))
            if 1 <= completion_value <= len(self.tasks):
                if self.tasks[completion_value - 1]["completed"]:
                    print("Task is already completed!")         
                else:
                    self.tasks[completion_value - 1]["completed"] = True
                    self.save_tasks()
                    print("Task is now marked as completed!")
                    self.view_tasks()
            else:
                print("Invalid task number.")     
        except ValueError:
            print("Please enter a valid number.")    

    def delete_task(self):
        if not self.tasks:
            print("No tasks to amend.")   
            return
        self.view_tasks()
        try:
            deletion_value = int(input("Which task would you like to delete from the list? "))

            if 1 <= deletion_value <= len(self.tasks):
                removed = self.tasks.pop(deletion_value - 1)
                self.save_tasks()
                print(f"Deleted task: {removed['title']}")
                self.view_tasks()
            else:
                print("Invalid choice!")               
        except ValueError:
            print("Please enter a valid number.") 

    def clear_completed(self):
        if not self.tasks:
            print("No tasks to amend.")           
            return
        self.view_tasks()
        clear_choice = input('"If you would like to clear the completed tasks, please input the letter "y":')
        if clear_choice.lower() == "y":
            og_count = len(self.tasks)
            self.tasks[:] = [task for task in self.tasks if not task["completed"]]
            removed_count = og_count - len(self.tasks)
            if removed_count > 0:
                self.save_tasks()
                print(f"{removed_count} completed tasks have been removed from the list.\nHere is the updated list:")
                self.view_tasks()
            else:
                print("No completed tasks to clear.")                
        else:
            print("List has not been cleared.")
              

manager = TaskManager("tasks.json")

actions = {
    "1" : manager.add_task,
    "2" : manager.view_tasks,
    "3" : manager.completed_tasks,
    "4" : manager.delete_task,
    "5" : manager.clear_completed
}

print("Welcome to your Task List Program!")

while True:
    show_menu()
    choice = input("Please input your selection: ")

    if choice == "6":
        break

    action = actions.get(choice)

    if action:
        action()
    else:
        print("Invalid Choice!")
        
    pause()
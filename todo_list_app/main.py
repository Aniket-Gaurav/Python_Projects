import tkinter as tk
import json


# Task class definition
class Task:
    def __init__(self, name, description, due_date=None, priority=1, completed=False):
        self.name = name
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.completed = completed

    def mark_as_completed(self):
        self.completed = True


# Create window function
def create_window():
    window = tk.Tk()
    window.title("To-Do List App")
    window.geometry("400x400")

    global task_entry, task_listbox
    task_entry = tk.Entry(window)
    task_entry.pack()

    task_listbox = tk.Listbox(window)
    task_listbox.pack()

    add_button = tk.Button(window, text="Add Task", command=add_task)
    add_button.pack()

    delete_button = tk.Button(window, text="Delete Task", command=delete_task)
    delete_button.pack()

    mark_button = tk.Button(
        window, text="Mark Completed", command=mark_completed)
    mark_button.pack()

    window.mainloop()


# Global list to store tasks
tasks = []


# Function to save tasks to a file
def save_tasks():
    with open('tasks.json', 'w') as file:
        json.dump([task.__dict__ for task in tasks], file)


# Function to load tasks from a file
def load_tasks():
    try:
        with open('tasks.json', 'r') as file:
            task_data = json.load(file)
            for task in task_data:
                tasks.append(Task(**task))
                # Display task names in the listbox
                task_listbox.insert(tk.END, task['name'])
    except FileNotFoundError:
        pass


# Function to add a new task
def add_task():
    task_name = task_entry.get()
    if not task_name:
        return
    new_task = Task(task_name, "No Description")
    tasks.append(new_task)
    # Add the new task to the listbox
    task_listbox.insert(tk.END, new_task.name)


# Function to delete a selected task
def delete_task():
    selected_task_index = task_listbox.curselection()
    if selected_task_index:
        selected_task_index = selected_task_index[0]
        task_listbox.delete(selected_task_index)  # Remove from the listbox
        tasks.pop(selected_task_index)  # Remove from the task list


# Function to mark a selected task as completed
def mark_completed():
    selected_task_index = task_listbox.curselection()
    if selected_task_index:
        selected_task_index = selected_task_index[0]
        # Mark task as completed
        tasks[selected_task_index].mark_as_completed()
        # Optionally, you can update the task's appearance in the listbox
        # Highlight the completed task
        task_listbox.itemconfig(selected_task_index, {'bg': 'lightgreen'})


# Load tasks when the app starts
load_tasks()

# Create the window with the UI
create_window()

import tkinter as tk
from tkinter import simpledialog

class ToDoList:
    def __init__(self, master):
        self.master = master
        master.title("To-Do App")

       
        self.label = tk.Label(master, text="Tasks:")
        self.label.pack(padx=10, pady=10)

        self.tasks_listbox = tk.Listbox(master, width=30)
        self.tasks_listbox.pack(padx=10, pady=10)

        
        add_button = tk.Button(master, text="Add Task", command=self.add_task)
        add_button.pack(pady=5)

        remove_button = tk.Button(master, text="Remove Task", command=self.remove_task)
        remove_button.pack(pady=5)

        self.tasks = []

    def add_task(self):
        task = simpledialog.askstring("Add Task", "Enter a new task:")
        if task:
            self.tasks.append(task)
            self.tasks_listbox.insert(tk.END, task)

    def remove_task(self):
        selected_indices = self.tasks_listbox.curselection()
        for index in reversed(selected_indices):
            task = self.tasks_listbox.get(index)
            self.tasks.remove(task)
            self.tasks_listbox.delete(index)

root = tk.Tk()
todo_list = ToDoList(root)
root.mainloop()
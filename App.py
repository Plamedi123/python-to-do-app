import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from datetime import datetime

# Function to add a task
def add_task():
    task = entry_task.get()
    priority = combo_priority.get()
    category = combo_category.get()
    due_date = entry_due_date.get()

    if task:
        task_info = f"{task} (Priority: {priority}, Category: {category}, Due Date: {due_date})"
        listbox_tasks.insert(tk.END, task_info)
        entry_task.delete(0, tk.END)
        entry_due_date.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

# Function to delete a task
def delete_task():
    try:
        task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(task_index)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete.")

# Create the main window
root = tk.Tk()
root.title("Enhanced To-Do List App")

# Create widgets
frame_tasks = tk.Frame(root)
frame_tasks.pack()

listbox_tasks = tk.Listbox(frame_tasks, width=80, height=15, font=("Helvetica", 12))
listbox_tasks.pack(side=tk.LEFT, fill=tk.BOTH)

scrollbar_tasks = tk.Scrollbar(frame_tasks)
scrollbar_tasks.pack(side=tk.RIGHT, fill=tk.BOTH)

listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
scrollbar_tasks.config(command=listbox_tasks.yview)

entry_task = tk.Entry(root, width=80, font=("Helvetica", 12))
entry_task.pack()

# Priority dropdown
combo_priority = ttk.Combobox(root, values=["High", "Medium", "Low"], width=10, font=("Helvetica", 12))
combo_priority.set("Priority")
combo_priority.pack()

# Category dropdown
combo_category = ttk.Combobox(root, values=["Work", "Personal", "Study", "Other"], width=10, font=("Helvetica", 12))
combo_category.set("Category")
combo_category.pack()

entry_due_date = tk.Entry(root, width=20, font=("Helvetica", 12))
entry_due_date.insert(0, "YYYY-MM-DD")
entry_due_date.pack()

button_add_task = tk.Button(root, text="Add Task", command=add_task, font=("Helvetica", 12))
button_add_task.pack()

button_delete_task = tk.Button(root, text="Delete Task", command=delete_task, font=("Helvetica", 12))
button_delete_task.pack()

button_quit = tk.Button(root, text="Quit", command=root.destroy, font=("Helvetica", 12))
button_quit.pack()

# Run the application
root.mainloop()

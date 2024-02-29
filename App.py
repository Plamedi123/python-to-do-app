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
root.geometry("600x400")

# Create style for widgets
style = ttk.Style()
style.configure("TFrame", background="#f0f0f0")
style.configure("TLabel", background="#f0f0f0")
style.configure("TButton", background="#4CAF50", foreground="white")

# Create widgets
frame_tasks = ttk.Frame(root)
frame_tasks.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

listbox_tasks = tk.Listbox(frame_tasks, width=60, height=15, font=("Helvetica", 12))
listbox_tasks.pack(side=tk.LEFT, fill=tk.BOTH, padx=10, pady=10)

scrollbar_tasks = tk.Scrollbar(frame_tasks, orient=tk.VERTICAL, command=listbox_tasks.yview)
scrollbar_tasks.pack(side=tk.RIGHT, fill=tk.Y)

listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)

entry_task = ttk.Entry(root, width=50, font=("Helvetica", 12))
entry_task.pack(padx=10, pady=5)

combo_priority = ttk.Combobox(root, values=["High", "Medium", "Low"], width=10, font=("Helvetica", 12))
combo_priority.set("Priority")
combo_priority.pack(padx=10, pady=5)

combo_category = ttk.Combobox(root, values=["Work", "Personal", "Study", "Other"], width=10, font=("Helvetica", 12))
combo_category.set("Category")
combo_category.pack(padx=10, pady=5)

entry_due_date = ttk.Entry(root, width=20, font=("Helvetica", 12))
entry_due_date.insert(0, "YYYY-MM-DD")
entry_due_date.pack(padx=10, pady=5)

button_add_task = ttk.Button(root, text="Add Task", command=add_task)
button_add_task.pack(padx=10, pady=5)

button_delete_task = ttk.Button(root, text="Delete Task", command=delete_task)
button_delete_task.pack(padx=10, pady=5)

button_quit = ttk.Button(root, text="Quit", command=root.destroy)
button_quit.pack(padx=10, pady=5)

# Run the application
root.mainloop()

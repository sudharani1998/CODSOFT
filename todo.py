import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_entry.get()
    if task:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def remove_task():
    selected_task_index = task_listbox.curselection()
    if selected_task_index:
        task_listbox.delete(selected_task_index)

def clear_tasks():
    task_listbox.delete(0, tk.END)

# Create the main application window
root = tk.Tk()
root.title("To-Do List")

# Task entry field
task_entry = tk.Entry(root, width=40)
task_entry.pack(pady=10)

# Add task button
add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack()

# Remove task button
remove_button = tk.Button(root, text="Remove Task", command=remove_task)
remove_button.pack()

# Clear tasks button
clear_button = tk.Button(root, text="Clear All Tasks", command=clear_tasks)
clear_button.pack()

# Task listbox
task_listbox = tk.Listbox(root, width=50)
task_listbox.pack()

# Start the main application loop
root.mainloop()

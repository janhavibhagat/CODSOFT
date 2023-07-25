import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def delete_task():
    try:
        index = listbox.curselection()
        listbox.delete(index)
    except:
        messagebox.showwarning("Warning", "Please select a task.")

def update_task():
    try:
        index = listbox.curselection()
        task = entry.get()
        if task:
            listbox.delete(index)
            listbox.insert(index, task)
            entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task.")
    except:
        messagebox.showwarning("Warning", "Please select a task.")

def clear_tasks():
    listbox.delete(0, tk.END)

root = tk.Tk()
root.title("To-Do List")

# Create GUI elements
label = tk.Label(root, text="Enter a task:")
label.pack()

entry = tk.Entry(root, width=30)
entry.pack()

add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack()

delete_button = tk.Button(root, text="Delete Task", command=delete_task)
delete_button.pack()

update_button = tk.Button(root, text="Update Task", command=update_task)
update_button.pack()

clear_button = tk.Button(root, text="Clear All Tasks", command=clear_tasks)
clear_button.pack()

listbox = tk.Listbox(root, width=50)
listbox.pack()

root.mainloop()

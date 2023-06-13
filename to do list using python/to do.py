import tkinter as tk
from tkinter import messagebox
from tkinter import font
from datetime import datetime

tasks = []
stopwatch_running = False
start_time = None

def add_task():
    task = entry.get()
    if not task:
        messagebox.showerror("Error", "Please enter a task.")
        return

    tasks.append(task)
    listbox.insert(tk.END, task)
    entry.delete(0, tk.END)

def remove_task():
    selected_task = listbox.curselection()
    if not selected_task:
        messagebox.showerror("Error", "Please select a task.")
        return

    task_index = selected_task[0]
    task = listbox.get(task_index)
    tasks.remove(task)
    listbox.delete(task_index)

def clear_tasks():
    tasks.clear()
    listbox.delete(0, tk.END)

def update_time():
    current_time = datetime.now().strftime("%H:%M:%S")
    time_label.config(text=current_time)
    time_label.after(1000, update_time)

def update_date():
    current_date = datetime.now().strftime("%Y-%m-%d")
    date_label.config(text=current_date)

def export_tasks():
    if len(tasks) == 0:
        messagebox.showinfo("Information", "No tasks to export.")
        return

    file_name = "task_list.txt"
    with open(file_name, "w") as file:
        for task in tasks:
            file.write(f"{task}\n")

    messagebox.showinfo("Information", f"Tasks exported to {file_name}.")

def start_stopwatch():
    global stopwatch_running, start_time
    if not stopwatch_running:
        stopwatch_running = True
        start_time = datetime.now()
        stopwatch_button.config(text="Stop Stopwatch")
        stopwatch_button.config(command=stop_stopwatch)
        update_stopwatch()
        
def stop_stopwatch():
    global stopwatch_running
    if stopwatch_running:
        stopwatch_running = False
        stopwatch_button.config(text="Start Stopwatch")
        stopwatch_button.config(command=start_stopwatch)
        
def update_stopwatch():
    if stopwatch_running:
        elapsed_time = datetime.now() - start_time
        stopwatch_label.config(text=str(elapsed_time))
    stopwatch_label.after(1000, update_stopwatch)

def on_enter(event):
    add_task()

# Create GUI
window = tk.Tk()
window.title("To-Do List")
window.geometry("800x61000")
window.resizable(False, False)
window.configure(bg="black")

font_style = font.Font(family="Times New Roman", size=20)

label = tk.Label(window, text="Task:", fg="red", bg="black", font=font_style)
label.pack(pady=2)

entry = tk.Entry(window, width=30, font=font_style)
entry.pack(pady=2)
entry.bind("<Return>", on_enter)

add_button = tk.Button(window, text="Add Task", command=add_task, fg="red", bg="black", font=font_style)
add_button.pack(pady=2)

remove_button = tk.Button(window, text="Remove Task", command=remove_task, fg="red", bg="black", font=font_style)
remove_button.pack(pady=2)

clear_button = tk.Button(window, text="Clear All Tasks", command=clear_tasks, fg="red", bg="black", font=font_style)
clear_button.pack(pady=2)

listbox = tk.Listbox(window, fg="red", bg="black", font=font_style)
listbox.pack(pady=2)

time_label = tk.Label(window, text="", fg="red", bg="black", font=font_style)
time_label.pack(pady=2)

date_label = tk.Label(window, text="", fg="red", bg="black", font=font_style)
date_label.pack(pady=2)

export_button = tk.Button(window, text="Export Tasks", command=export_tasks, fg="red", bg="black", font=font_style)
export_button.pack(pady=2)

stopwatch_button = tk.Button(window, text="Start Stopwatch", command=start_stopwatch, fg="red", bg="black", font=font_style)
stopwatch_button.pack(pady=2)

stopwatch_label = tk.Label(window, text="00:00:00", fg="red", bg="black", font=font_style)
stopwatch_label.pack(pady=2)

update_time()
update_date()

window.mainloop()

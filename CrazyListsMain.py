import tkinter as tk


def display_tasks():
    task_list.delete(0, tk.END)
    try:
        with open("todo.txt", "r") as file:
            tasks = file.readlines()
            if tasks:
                for task in tasks:
                    task_list.insert(tk.END, task.strip())
            else:
                task_list.insert(tk.END, "No tasks in your list.")
    except FileNotFoundError:
        task_list.insert(tk.END, "No tasks in your list.")


def add_task():
    task = task_entry.get()
    if task:
        with open("todo.txt", "a") as file:
            file.write(task + "\n")
        task_entry.delete(0, tk.END)
        display_tasks()


def remove_task():
    selected_task = task_list.curselection()
    if selected_task:
        task_index = selected_task[0]
        task_number = int(task_index) + 1
        try:
            with open("todo.txt", "r") as file:
                tasks = file.readlines()
            with open("todo.txt", "w") as file:
                if 1 <= task_number <= len(tasks):
                    removed_task = tasks.pop(task_number - 1)
                    file.writelines(tasks)
                    task_list.delete(selected_task)
        except FileNotFoundError:
            pass


def quit_app():
    root.destroy()


root = tk.Tk()
root.title("Todo List Application")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

task_label = tk.Label(frame, text="Enter a task:")
task_label.pack()

task_entry = tk.Entry(frame)
task_entry.pack()

add_button = tk.Button(frame, text="Add Task", command=add_task)
add_button.pack()

remove_button = tk.Button(frame, text="Remove Task", command=remove_task)
remove_button.pack()

display_button = tk.Button(frame, text="Display Tasks", command=display_tasks)
display_button.pack()

quit_button = tk.Button(frame, text="Quit", command=quit_app)
quit_button.pack()

task_list = tk.Listbox(frame, selectmode=tk.SINGLE)
task_list.pack()

display_tasks()

root.mainloop()

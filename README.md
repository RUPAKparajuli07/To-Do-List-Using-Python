## To-Do List Application Documentation

This documentation provides an overview and explanation of the code for a To-Do List application implemented using the Tkinter library in Python.

### Requirements

- Python 3.x
- Tkinter library

### Code Overview

The code implements a graphical user interface (GUI) for a To-Do List application. It allows users to add tasks, remove tasks, clear all tasks, export tasks to a file, and use a stopwatch feature.

The code begins by importing the required libraries:

```python
import tkinter as tk
from tkinter import messagebox
from tkinter import font
from datetime import datetime
```

Then, it defines some global variables:

```python
tasks = []
stopwatch_running = False
start_time = None
```

These variables are used to store the tasks, manage the stopwatch state, and track the start time.

The code defines several functions to handle different functionalities of the application:

- `add_task()`: This function is called when the user clicks the "Add Task" button or presses the Enter key. It retrieves the task text from the entry field, validates it, adds it to the task list, and updates the listbox to display the new task.

- `remove_task()`: This function is called when the user clicks the "Remove Task" button. It retrieves the selected task from the listbox, removes it from the task list, and updates the listbox accordingly.

- `clear_tasks()`: This function is called when the user clicks the "Clear All Tasks" button. It clears all the tasks from the task list and updates the listbox.

- `update_time()`: This function is responsible for updating the current time displayed in the application. It uses the `datetime.now()` function to get the current time and updates the time label every second.

- `update_date()`: This function updates the current date displayed in the application. It uses the `datetime.now()` function to get the current date and updates the date label.

- `export_tasks()`: This function is called when the user clicks the "Export Tasks" button. It checks if there are any tasks to export, creates a text file named "task_list.txt", and writes each task from the task list to the file.

- `start_stopwatch()`: This function is called when the user clicks the "Start Stopwatch" button. It starts the stopwatch by setting the `stopwatch_running` variable to `True`, recording the start time using `datetime.now()`, and updating the stopwatch button text and command.

- `stop_stopwatch()`: This function is called when the user clicks the "Stop Stopwatch" button. It stops the stopwatch by setting the `stopwatch_running` variable to `False` and updates the stopwatch button text and command.

- `update_stopwatch()`: This function continuously updates the stopwatch display while the stopwatch is running. It calculates the elapsed time by subtracting the start time from the current time and updates the stopwatch label.

- `on_enter(event)`: This function is called when the user presses the Enter key. It is used to trigger the `add_task()` function.

The code then creates the GUI window and sets its properties:

```python
window = tk.Tk()
window.title("To-Do List")
window.geometry("800x600")
window.resizable(False, False)
window.configure(bg="black")
```

Next, it defines a font style for the labels and buttons:

```python
font_style = font.Font(family="Times New Roman", size=20)
```

After that, it creates and configures various GUI elements, including labels, an entry field, buttons, a listbox, time and date labels, and a stopwatch label. These elements are packed and positioned within the window.

Finally, the code calls the `update_time()` and `update_date()` functions to start updating the time and date displays, and then starts the GUI main loop using `window.mainloop()`.

### How to Use the Application

1. Run the script using Python.
2. The To-Do List application window will appear.
3. Enter a task in the text entry field and press Enter or click the "Add Task" button to add it to the list.
4. To remove a task, select it from the listbox and click the "Remove Task" button.
5. To clear all tasks, click the "Clear All Tasks" button.
6. To export the tasks to a file, click the "Export Tasks" button. If there are no tasks, a message box will inform you.
7. To start the stopwatch, click the "Start Stopwatch" button. The stopwatch will begin counting.
8. To stop the stopwatch, click the "Stop Stopwatch" button.
9. The current time and date are displayed at the top of the window, and they update automatically.
10. To exit the application, close the window or press the close button.

Contributing
Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

License
The To-Do List Application is licensed under the
MIT License.

That concludes the documentation for the To-Do List application code. The provided code offers basic functionality, but you can modify and extend it to suit your specific requirements.

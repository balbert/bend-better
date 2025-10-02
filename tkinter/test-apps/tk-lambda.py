
# Example 1c - using lambda

import tkinter as tk

def greet_user(name):
    """
    This function will be called when the button is clicked.
    """
    print(f"Hello, {name}!")

# Create the main window
root = tk.Tk()
root.title("Tkinter Lambda Example")

# Text entry field
name_entry = tk.Entry(root)
name_entry.pack(padx=20, pady=10)

# Use lambda to pass the entry value to the handler
greet_button = tk.Button(root, text="Greet", command=lambda: greet_user(name_entry.get()))
greet_button.pack(padx=20, pady=10)

# Start the Tkinter event loop
root.mainloop()

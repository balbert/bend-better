
# Example 1a - using global functions

import tkinter as tk

def button_click_handler():
    """
    This function will be called when the button is clicked.
    """
    print("Button clicked!")

# Create the main window
root = tk.Tk()
root.title("Tkinter Button Example")

# Create a button and assign the handler function
my_button = tk.Button(root, text="Click Me", command=button_click_handler)
my_button.pack(pady=20)

# Start the Tkinter event loop
root.mainloop()

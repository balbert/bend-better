
# Example 1c - using a nested function

import tkinter as tk

''' function to create a button '''
def create_button_with_args(parent, text, message):
    """
    This function will be called when the button is clicked.
    """
    def button_handler():
        print(message)

    # Create a button
    button = tk.Button(parent, text=text, command=button_handler)
    return button

# Create the main window
root = tk.Tk()
root.title("Tkinter Nested Function Example")

# Button 1
button1 = create_button_with_args(root, "Button 1", "This is message 1")
button1.pack(padx=20, pady=10)

# Button 2
button2 = create_button_with_args(root, "Button 2", "This is message 2")
button2.pack(padx=20, pady=10)

# Start the Tkinter event loop
root.mainloop()

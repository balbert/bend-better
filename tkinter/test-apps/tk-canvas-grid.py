import tkinter as tk

def create_grid(canvas, step_size=20, line_color="lightgray"):
    """
    Draws a grid on the given Tkinter canvas.

    Args:
        canvas (tk.Canvas): The canvas widget to draw the grid on.
        step_size (int): The distance between grid lines in pixels.
        line_color (str): The color of the grid lines.
    """
    canvas_width = canvas.winfo_width()
    canvas_height = canvas.winfo_height()

    # Clear any existing grid lines (optional, good for redrawing on resize)
    canvas.delete("grid_line")

    # Draw vertical lines
    for i in range(0, canvas_width, step_size):
        canvas.create_line(i, 0, i, canvas_height, fill=line_color, tags="grid_line")

    # Draw horizontal lines
    for i in range(0, canvas_height, step_size):
        canvas.create_line(0, i, canvas_width, i, fill=line_color, tags="grid_line")

# Create the main window
root = tk.Tk()
root.title("Tkinter Canvas Grid")

# Create a canvas
canvas = tk.Canvas(root, bg="white", width=400, height=300)
canvas.pack(fill=tk.BOTH, expand=True)

# Bind the create_grid function to the <Configure> event to redraw on resize
canvas.bind("<Configure>", lambda event: create_grid(canvas))

# Initial drawing of the grid (after the window has been rendered and dimensions are available)
root.update_idletasks() # Ensure dimensions are updated
create_grid(canvas)

root.mainloop()
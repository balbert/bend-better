
import tkinter as tk

''' function create_grid() '''
def create_grid(canvas, grid_size=20):
    """Draws a grid on the given Tkinter canvas."""
    canvas.delete("grid_line")  # Delete existing grid lines if any

    width = canvas.winfo_width()
    height = canvas.winfo_height()

    # Draw vertical lines
    for i in range(0, width, grid_size):
        canvas.create_line([(i, 0), (i, height)], tag="grid_line", fill="lightgray")

    # Draw horizontal lines
    for i in range(0, height, grid_size):
        canvas.create_line([(0, i), (width, i)], tag="grid_line", fill="lightgray")

''' function on_configured() '''
def on_configure(event, canvas, grid_size):
    """Callback for when the canvas is resized."""
    create_grid(canvas, grid_size)

''' main entry point '''
if __name__ == "__main__":
    # Create the main window
    root = tk.Tk()
    root.title("Tkinter Canvas Grid")

    # Create the canvas
    canvas = tk.Canvas(root, bg="white", width=400, height=400)
    canvas.pack(fill=tk.BOTH, expand=True)

    # Define the spacing between grid lines
    grid_spacing = 20

    # Bind the create_grid function to the <Configure> event to redraw on resize
    canvas.bind("<Configure>", lambda event: on_configure(event, canvas, grid_spacing))

    # Initial grid creation
    root.update_idletasks()  # Ensure canvas dimensions are available
    create_grid(canvas, grid_spacing)

    root.mainloop()

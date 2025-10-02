
import tkinter as tk

class Gui():
    def __init__(self, root):
        self.root = root
        self._step_x = 20
        self._step_y = 20

        self.entry = tk.Entry(root)

        # Create a frame
        frame = tk.Frame(self.root)
        frame.grid(row=0, column=0, sticky="n")

        # Create a combobox
        stvar = tk.StringVar()
        stvar = tk.StringVar(value="one")

        self.option = tk.OptionMenu(frame, stvar, "one", "two", "three")
        self.option.grid(row=0, column=1, sticky="nwe")

        # Create a Canvas widget
        self.canvas = tk.Canvas(root, bg="white", width=400, height=300)
        self.canvas.grid(row=0, column=1)

        # Bind the create_grid function to the <Configure> event to redraw on resize
        self.canvas.bind("<Configure>", lambda event: self.create_grid())

        label1 = tk.Label(frame, text="label1").grid(row=0, column=0, sticky="nw")
        label2 = tk.Label(frame, text="label2").grid(row=1, column=0, sticky="w")
        label3 = tk.Label(frame, text="label3").grid(row=2, column=0, sticky="w")

        entry1 = tk.Entry(frame).grid(row=1, column=1, sticky=tk.E + tk.W)
        entry2 = tk.Entry(frame).grid(row=2, column=1, sticky=tk.E)

        Button1 = tk.Button(frame, text="Draw").grid(row=3, column=1, sticky="we")

        #figure1 = self.canvas.create_rectangle(80, 80, 120, 120, fill="blue")

        # Initial grid creation (optional, as it will be redrawn on configure)
        self.create_grid()

    ''' function create_grid() '''
    def create_grid(self):
        """ Draws a grid on the given canvas. """
        # Delete existing grid lines if any
        self.canvas.delete("grid_line")

        # Get window dimensions
        width = self.canvas.winfo_width()
        height = self.canvas.winfo_height()

        # Draw vertical lines
        for i in range(0, width, self._step_x):
            self.canvas.create_line([(i, 0), (i, height)], tag="grid_line", fill="lightgray")

        # Draw horizontal lines
        for i in range(0, height, self._step_y):
            self.canvas.create_line([(0, i), (width, i)], tag="grid_line", fill="lightgray")

        #Grid.columnconfigure(self.root, 1, weight=1, size=200)


if __name__== '__main__':
    # Main window setup
    root = tk.Tk()
    root.title("Harmonica - Bend Better")

    gui = Gui(root)

    root.mainloop()


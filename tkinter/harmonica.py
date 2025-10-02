
import tkinter as tk

class Gui():
    def __init__(self, root):
        self.main_wnd = root
        self._step_x = 20
        self._step_y = 20

    def create(self):
        # Create a frame (left side)
        frame = tk.Frame(self.main_wnd, bg="grey")
        frame.grid(row=0, column=0, sticky="nsw")

        # Create a group box - child
        group = tk.LabelFrame(frame, text="Controls", padx=5, pady=5)
        group.grid(row=0, column=0, padx=5, pady=5, sticky="nsw")

        # Label 1
        label1 = tk.Label(group, text="Label 1")
        label1.grid(row=0, column=0, sticky="nw")

        # Combobox
        var1 = tk.StringVar(value="Selection 1")
        self.option = tk.OptionMenu(group, var1, "Selection 1", "Selection 2", "Selection 3")
        self.option.grid(row=0, column=1, sticky="nw")

        # Label 2
        label2 = tk.Label(group, text="Label 2")
        label2.grid(row=1, column=0, sticky="nw")
 
        # Textbox 1
        text1 = tk.Entry(group)
        text1.grid(row=1, column=1, sticky="nw")
 
        # Label 3
        label3 = tk.Label(group, text="Label 3")
        label3.grid(row=2, column=0, sticky="nw")
 
        # Textbox 2
        text2 = tk.Entry(group)
        text2.grid(row=2, column=1, sticky="nw")
 
        # Button 1
        button1 = tk.Button(group, text="Button 1")
        button1.grid(row=3, column=1, sticky="nw")

        # Canvas widget (right side)
        # self.canvas = tk.Canvas(self.main_wnd, bg="white", width=400, height=300)
        # self.canvas.grid(row=0, column=1, sticky=tk.E+tk.N+tk.S)
        self.canvas = tk.Canvas(self.main_wnd, bg="white")
        self.canvas.grid(row=0, column=1, sticky="nsew")

        # Initial grid creation (optional, as it will be redrawn on configure)
        # self.create_grid()

        # Bind the create_grid function to the <Configure> event to redraw on resize
        # self.canvas.bind("<Configure>", lambda event: self.create_grid())

        frame.rowconfigure(0, weight=1)
        frame.columnconfigure(0, weight=1)

        group.rowconfigure(0, weight=1)
        group.columnconfigure(0, weight=1)
        group.columnconfigure(1, weight=1)

        root.rowconfigure(0, weight=1)
        root.columnconfigure(1, weight=1)


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

''' Main entry point '''
if __name__== '__main__':
    # The root window
    root = tk.Tk()
    root.title("Harmonica - Bend Better")

    # GUI
    gui = Gui(root)
    gui.create()

    # Process
    root.mainloop()


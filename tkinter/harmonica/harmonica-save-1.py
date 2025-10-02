
import tkinter as tk

class Gui():
    def __init__(self, root):
        self.main_wnd = root
        self._step_x = 20
        self._step_y = 20

    def create(self):

        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        # Create a frame (left side)
        frame1 = tk.Frame(self.main_wnd)
        frame1.grid(row=0, column=0, sticky=(tk.N, tk.S, tk.W))

        # Create a group box - child
        group1 = tk.LabelFrame(frame1, text=" Controls ", padx=5, pady=5)
        group1.grid(row=0, column=0, padx=5, pady=5, sticky=(tk.N, tk.S, tk.W))

        # Label 1
        label1 = tk.Label(group1, text="Label 1")
        label1.grid(row=0, column=0, pady=11, sticky=(tk.N, tk.W))

        # Combobox
        var1 = tk.StringVar(value="Selection 1")
        self.option = tk.OptionMenu(group1, var1, "Selection 1", "Selection 2", "Selection 3")
        self.option.grid(row=0, column=1, pady=5, sticky=(tk.N, tk.W))

        # Label 2
        label2 = tk.Label(group1, text="Label 2")
        label2.grid(row=1, column=0, pady=7, sticky=(tk.N, tk.W))

        # Textbox 1
        text1 = tk.Entry(group1)
        text1.grid(row=1, column=1, pady=5, sticky=(tk.N, tk.W))

        # Label 3
        label3 = tk.Label(group1, text="Label 3")
        label3.grid(row=2, column=0, pady=7, sticky=(tk.N, tk.W))

        # Textbox 2
        text2 = tk.Entry(group1)
        text2.grid(row=2, column=1, pady=5, sticky=(tk.N, tk.W))

        # Button 1
        button1 = tk.Button(group1, text="Button 1")
        button1.grid(row=3, column=1, pady=5, sticky=(tk.N, tk.W))

        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        # Create a frame (right side)
        frame2 = tk.Frame(self.main_wnd)
        frame2.grid(row=0, column=1, sticky=(tk.N, tk.S, tk.E, tk.W))

        # Create a group box - child
        #group2 = tk.LabelFrame(frame2)
        #group2.grid(row=0, column=0, sticky=(tk.N, tk.S, tk.E, tk.W))

        # Canvas widget (right side)
        #self.canvas1 = tk.Canvas(group2, bd=1, relief='sunken')
        self.canvas1 = tk.Canvas(frame2, bd=1, relief='ridge')
        self.canvas1.grid(row=0, column=0, sticky=(tk.N, tk.S, tk.E, tk.W))

        # Initial grid creation (optional, as it will be redrawn on configure)
        self.create_grid()

        # Bind the create_grid function to the <Configure> event to redraw on resize
        self.canvas1.bind("<Configure>", lambda event: self.create_grid())

        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        frame1.rowconfigure(0, weight=1)
        frame1.columnconfigure(0, weight=1)

        #group1.rowconfigure(0, weight=1)
        #group1.columnconfigure(0, weight=1)
        #group1.columnconfigure(1, weight=1)

        frame2.rowconfigure(0, weight=1)
        frame2.columnconfigure(0, weight=1)

        #group2.rowconfigure(0, weight=1)
        #group2.columnconfigure(0, weight=1)

        root.rowconfigure(0, weight=1)
        #root.columnconfigure(0, weight=1)
        root.columnconfigure(1, weight=1)


    ''' function create_grid() '''
    def create_grid(self):
        """ Draws a grid on the given canvas. """
        # Delete existing grid lines if any
        self.canvas1.delete("grid_line")

        # Get window dimensions
        width = self.canvas1.winfo_width()
        height = self.canvas1.winfo_height()

        # Draw vertical lines
        for i in range(0, width, self._step_x):
            self.canvas1.create_line([(i, 0), (i, height)], tag="grid_line", fill="gray")

        # Draw horizontal lines
        for i in range(0, height, self._step_y):
            self.canvas1.create_line([(0, i), (width, i)], tag="grid_line", fill="gray")

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


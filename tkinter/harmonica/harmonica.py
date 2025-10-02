
import tkinter as tk

''' Class GUI '''
class Gui():
    """
    Create a harmonica drawing...
    """

    def set_x(self, rhs):
        self._step_x = rhs


    def set_y(self, rhs):
        self._step_y = rhs


    def __init__(self, root):
        self.main_wnd = root
        self._step_x = 20
        self._step_y = 20


    def create(self):
        # Create a frame (left side)
        frame1 = tk.Frame(self.main_wnd)
        frame1.grid(row=0, column=0, sticky=(tk.N, tk.S, tk.W))

        # Create a group box - child
        group1 = tk.LabelFrame(frame1, text="Controls", padx=5, pady=5)
        #group1.grid(row=0, column=0, padx=5, pady=5, sticky=(tk.N, tk.S, tk.W))
        group1.grid(row=0, column=0, sticky=(tk.N, tk.S, tk.W))

        # Label 1
        label1 = tk.Label(group1, text="Label 1", width=10)
        label1.grid(row=0, column=0, pady=11, sticky=(tk.N, tk.W))

        # Combobox
        var1 = tk.StringVar(value="Selection 1")
        self.option = tk.OptionMenu(group1, var1, "Selection 1", "Selection 2", "Selection 3")
        self.option.config(width=15)
        self.option.grid(row=0, column=1, pady=5, sticky=(tk.N, tk.W))

        # Label 2
        label2 = tk.Label(group1, text="Label 2", width=10)
        label2.grid(row=1, column=0, pady=7, sticky=(tk.N, tk.W))

        # Textbox 1
        text1 = tk.Entry(group1, width=20)
        text1.grid(row=1, column=1, pady=5, sticky=(tk.N, tk.W))

        # Label 3
        label3 = tk.Label(group1, text="Label 3", width=10)
        label3.grid(row=2, column=0, pady=7, sticky=(tk.N, tk.W))

        # Textbox 2
        text2 = tk.Entry(group1, width=20)
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
        self.draw_grid()

        # Bind the create_grid function to the <Configure> event to redraw on resize
        self.canvas1.bind("<Configure>", lambda event: self.draw_grid())

        #self.draw_harmonica()

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
    def draw_grid(self):
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

    def draw_harmonica(self):

        # ♭ - flat
        # ♯ - sharp

        key_c_list = [
            'Bb', 
            'Eb', 'Gb', 'B', 
            'C', 'E', 'G', 'C', 'E', 'G', 'C', 'E', 'G', 'C',
            'D', 'G', 'B', 'D', 'F', 'A', 'B', 'D', 'F', 'A',
            'Db', 'Gb', 'Bb', 'Db', 'Ab',
            'F', 'A',
            'Ab'
            ]

        # label_offsets = [
        #     (9, 0), 
        #     (7, 1), (8, 1), (9, 1), 
        #     (0, 2), (1, 2), (2, 2), (3, 2), (4, 2), (5, 2), (6, 2), (7, 2), (8, 2), (9, 2),
        #     (0, 4), (1, 4), (2, 4), (3, 4), (4, 4), (5, 4), (6, 4), (7, 4), (8, 4), (9, 4),
        #     (0, 5), (1, 5), (2, 5), (3, 5), (5, 5), 
        #     (1, 6), (2, 6),
        #     (2, 7) 
        # ]

        label_offsets = [
            (10, 1),
            (8, 2), (9, 2), (10, 2),
            (0, 3), (1, 3), (2, 3), (3, 3), (4, 3), (5, 3), (6, 3), (7, 3), (8, 3), (9, 3), (10, 3), (11, 3),
            (0, 5), (1, 5), (2, 5), (3, 5), (4, 5), (5, 5), (6, 5), (7, 5), (8, 5), (9, 5), (10, 5), (11, 5),
            (0, 6), (1, 6), (2, 6), (3, 6), (4, 6),
            (0, 7), (2, 7), (3, 7),
            (3, 8) 
        ]

        key_c_array = [
            [  '',   '',   '',   '',  '',   '',  '',   '',   '', 'Bb'],
            [  '',   '',   '',   '',  '',   '',  '', 'Eb', 'Gb',  'B'],
            [ 'C',  'E',  'G',  'C', 'E',  'G', 'C',  'E',  'G',  'C'],
            [ 'D',  'G',  'B',  'D', 'F',  'A', 'B',  'D',  'F',  'A'],
            ['Db', 'Gb', 'Bb', 'Db',  '', 'Ab',  '',   '',   '',   ''],
            [  '',  'F',  'A',   '',  '',   '',  '',   '',   '',   ''],
            [  '',   '', 'Ab',   '',  '',   '',  '',   '',   '',   '']
            ]

        group1 = tk.LabelFrame(self.canvas1)
        group1.grid(row=0, column=0, columnspan=10)

        label_array = []
        note_index = 0
        for index, (offset_x, offset_y) in enumerate(label_offsets):
            print (f"{index}: ({offset_x}, {offset_y})")
            if offset_x == 0 | offset_x == 11:
                label = tk.Label(self.canvas1, width=4, height=2, bd=2, relief="solid")
            else:
                label = tk.Label(self.canvas1, text=note_index, width=4, height=2, bd=2, relief="solid")
                note_index += 1

            label.grid(row=offset_y, column=offset_x, padx=2, pady=2, sticky="w")
            label_array.append(label)

        group2 = tk.LabelFrame(self.canvas1, height=50, width=450, bd=2, relief="solid")
        group2.grid(row=4, column=0, columnspan=10)



        # key_labels_array = []
        # for index, item in enumerate(key_c_list):
        #     if index == 0:
        #         offset_x = [9]
        #         offset_y = 0
        #         print(f"ROW 1 - x: {offset_x}, y: {offset_y}")
        #     if 1<= index <= 3:
        #         offset_x = [7, 8, 9]
        #         offset_y = 1
        #         print(f"ROW 2 - x: {offset_x}, y: {offset_y}")
        #     if 4 <= index <= 13:
        #         offset_x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        #         offset_y = 2
        #         print(f"ROW 3 - x: {offset_x}, y: {offset_y}")
        #     if 14 <= index <= 23:
        #         offset_x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        #         offset_y = 3
        #         print(f"ROW 4 - x: {offset_x}, y: {offset_y}")
        #     if 24 <= index <= 28:
        #         offset_x = [0, 1, 2, 3, 5]
        #         offset_y = 4
        #         print(f"ROW 5 - x: {offset_x}, y: {offset_y}")
        #     if 29 <= index <= 30:
        #         offset_x = [1, 2]
        #         offset_y = 5
        #         print(f"ROW 6 - x: {offset_x}, y: {offset_y}")
        #     if index == 31:
        #         offset_x = [2]
        #         offset_y = 6
        #         print(f"ROW 7 - x: {offset_x}, y: {offset_y}")







        # Draws a line from (50,50) to (200,150)
        self.canvas1.create_line(50, 50, 200, 50, width=3)

''' Main entry point '''
if __name__== '__main__':

    # The root window
    root = tk.Tk()
    root.title("Harmonica - Bend Better")

    # GUI
    gui = Gui(root)
    gui.set_x(10)
    gui.set_y(10)
    gui.create()

    gui.draw_harmonica()
    
    # Process
    root.mainloop()


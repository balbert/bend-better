
import tkinter as tk

class MyApp:

    def __init__(self, parent):
        self.myContainer1 = tk.Frame(parent)
        self.myContainer1.pack()

        self.button1 = tk.Button(self.myContainer1)
        self.button1["text"] = "Hello, World!"
        self.button1["background"] = "green"
        self.button1.pack()

        self.button2 = tk.Button(self.myContainer1)
        self.button2.configure(text="Off to join the circus!")
        self.button2.configure(background="tan")
        self.button2.pack()


        self.button3 = tk.Button(self.myContainer1)
        self.button3.configure(text="Join me?", background="cyan")
        self.button3.pack()

        self.button4 = tk.Button(self.myContainer1, text="Goodbye!", background="red")
        self.button4.pack()


root = tk.Tk()
myapp = MyApp(root)
root.mainloop()

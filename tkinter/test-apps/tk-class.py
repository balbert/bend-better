
import tkinter as tk

class GUI(tk.Frame):

    def __init__(self,master=None):
        tk.Frame.__init__(self, master)
        self.grid()

        self.fnameLabel = tk.Label(master, text="First Name")
        self.fnameLabel.grid()

        self.fnameEntry = tk.StringVar()
        self.fnameEntry = tk.Entry(textvariable=self.fnameEntry)
        self.fnameEntry.grid()

        self.lnameLabel = tk.Label(master, text="Last Name")
        self.lnameLabel.grid()

        self.lnameEntry = tk.StringVar()
        self.lnameEntry = tk.Entry(textvariable=self.lnameEntry)
        self.lnameEntry.grid()

        def buttonClick():
            print("You pressed Submit!")
            print(self.fnameEntry.get() + " " + self.lnameEntry.get() + ", you clicked the button!")

        self.submitButton = tk.Button(master, text="Submit", command=buttonClick)
        self.submitButton.grid()

if __name__ == "__main__":
    guiFrame = GUI()
    guiFrame.mainloop()

from tkinter import *
from tkinter import scrolledtext

master_window = Tk()
master_window.title("Tk - Resize Example")

# --------- Child of root 1
# Buttons frame (0, 0)
buttons_frame = Frame(master_window)
buttons_frame.grid(row=0, column=0, sticky=W+E)

# --------- Children of frame 1
# 1st button (0, 0)
btn_Image = Button(buttons_frame, text='Image')
btn_Image.grid(row=0, column=0, padx=(10), pady=10)

# 2nd button (0, 1)
btn_File = Button(buttons_frame, text='File')
btn_File.grid(row=0, column=1, padx=(10), pady=10)

# 3rd button (0, 2)
btn_Folder = Button(buttons_frame, text='Folder')
btn_Folder.grid(row=0, column=2, padx=(10), pady=10)

# --------- Child of root 2
# Group Frame (1, 0)
group1 = LabelFrame(master_window, text="Text Box", padx=5, pady=5)
group1.grid(row=1, column=0, columnspan=3, padx=10, pady=10, sticky=E+W+N+S)

# --------- Child of frame 2
# Create the textbox (0, 0)
txtbox = scrolledtext.ScrolledText(group1, width=40, height=10)
txtbox.grid(row=0, column=0, sticky=E+W+N+S)

group1.rowconfigure(0, weight=1)
group1.columnconfigure(0, weight=1)

master_window.columnconfigure(0, weight=1)
master_window.rowconfigure(1, weight=1)

mainloop()
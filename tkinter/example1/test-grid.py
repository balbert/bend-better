# test-grid

import tkinter as tk

USE_BUTTON = False

root = tk.Tk()
root.title("The Bend it Better Application")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Creating an oval:
#   create_oval(x0, y0, x1, y1, options)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Creating an arc:
#   create_arc(x0, y0, x1, x1, options)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Creating a line:
#   create_line(x0, y0, x1, y1, ..., xn, yn, options)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Creating a polygon:
#   create_polygon(x0, y0, x1, y1, ...xn, yn, options)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

C = tk.Canvas(
    height=250, width=300
    )


for row in range(3):
    for col in range(3):
        line = C.create_line(
            108, 120,
            320, 40,
            fill="green"
            )



# arc = C.create_arc(
#     180, 150,
#     80, 210,
#     start=0,
#     extent=220,
#     fill="red"
#     )

# oval = C.create_oval(
#     80, 30,
#     140, 150,
#     fill="blue"
#     )

C.pack()



# for row in range(3):
    # for col in range(3):
        # if USE_BUTTON:
            # tk.Button(
                # root,
                # text=f"Cell ({row}, {col})",
                # width=10,
                # height=5,
            # ).grid(row=row, column=col)
        # else:
            # tk.Label(
                # root,
                # text=f"Cell ({row}, {col})",
                # width=10,
                # height=5,
                # relief="flat",
                # relief="raised",
                # relief="sunken",
                # relief="ridge",
                # relief="solid",
                # relief="groove",
                # borderwidth=2,
            # ).grid(row=row, column=col)


# tk.Button(root, text="Span 2 columns", height=5).grid(
#     row=3,
#     column=0,
#     columnspan=2,
#     sticky="ew",
# )

# tk.Button(root, text="Span 2 rows", width=10, height=10).grid(
#     row=4,
#     column=0,
#     rowspan=2,
#     sticky="ns",
# )

root.mainloop()

from tkinter import (
    Label,
    Button,
    CENTER,
    NW,
    X,
    mainloop,
    Tk,
    Entry,
    END,
    Checkbutton,
    PhotoImage,
    E,
    W,
)

# creating main tkinter window/toplevel
master = Tk()

# this will create a label widget
l1 = Label(master, text="Height")
l2 = Label(master, text="Width")

l1.grid(row=0, column=0, sticky=W, pady=2)
l2.grid(row=1, column=0, sticky=W, pady=2)

# entry widgets, used to take entry from user
e1 = Entry(master)
e2 = Entry(master)

# this will arrange entry widgets
e1.grid(row=0, column=1, pady=2)
e2.grid(row=1, column=1, pady=2)

# checkbutton widget
c1 = Checkbutton(master, text="Preserve")
c1.grid(row=2, column=0, sticky=W, columnspan=2)


# button widget
b1 = Button(master, text="Zoom in")
b2 = Button(master, text="Zoom out")

# arranging button widgets
b1.grid(row=2, column=2, sticky=E)
b2.grid(row=2, column=3, sticky=E)

mainloop()

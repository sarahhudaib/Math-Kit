from tkinter import TOP, Tk, mainloop
from tkinter.ttk import Button

# from class filedialog
from tkinter.filedialog import askopenfile

root = Tk()
root.geometry("200x100")


def open_file():
    file = askopenfile(mode="r", filetypes=[("Python Files", "*.py")])
    if file is not None:
        content = file.read()
        print(content)


btn = Button(root, text="Open", command=open_file)
btn.pack(side=TOP, pady=10)

mainloop()

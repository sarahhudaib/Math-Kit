from tkinter import Tk, Button
from tkinter import messagebox

main = Tk()


def check():
    messagebox.askquestion(
        "Form",
        "Please check your information again and submit if correct.",
        icon="question",
    )


main.geometry("100x100")
B1 = Button(main, text="check", command=check)
B1.pack()

main.mainloop()

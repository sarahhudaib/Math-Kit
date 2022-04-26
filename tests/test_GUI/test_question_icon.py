from tkinter import Tk, Button, messagebox


main = Tk()


def check():
    messagebox.showinfo(
        "Form",
        "Please check your information again and submit if correct.",
        icon="info", 
        
    )


main.geometry("100x100")
B1 = Button(main, text="check", command=check)
B1.pack()

main.mainloop()

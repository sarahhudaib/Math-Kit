from tkinter import *
from math import *  # we import all the math functions


class RandomGeneratorPage:
    
    # def __init__(self, master, tools):
    #     self.master = master
    #     self.tools = tools
        
    #     width = int(tools.screen_width*0.8)
    #     height = int(tools.screen_height*0.8)
        
    #     self.randomizer_frame = Frame(master, width=width, height=height, bg=tools.pallete["gray"])
    #     self.master.add(self.randomizer_frame)

    def __init__(self, master):
        self.master = master        
        
        self.randomizer_frame = Frame(self.master, width=50, height=50, bg="#D3D8DE")
        self.master.grid_rowconfigure(0, weight=1)

        self.container = Frame(self.randomizer_frame, width=50, height=50, bg="#D3D8DE")
        self.container.pack()

        self.list_input = Label(self.container, text="list", font= ("Helvetica", 25),
                                bg="#D3D8DE")
        self.list_input.grid(row=0, column=0, columnspan=4, sticky="w")

        self.list_input_variable = StringVar()
        self.randomize = Label(self.container, text="Randomize", font= ("Helvetica", 25),
                                bg="#D3D8DE")
        self.randomize.grid(row=1, column=0)

        self.user_input = DoubleVar()
        self.user_input_entry = Entry(self.container, textvariable=self.user_input, width=20,
                                       font= ("Helvetica", 15))
        self.user_input_entry.grid(row=1, column=1)

        self.from_variable = StringVar()



if __name__ == "__main__":
    root = Tk()
    root.title("Random Generator")
    root.geometry("{}x{}".format(800, 600))
    root.resizable(False, False)
    root.configure(background="#D3D8DE")

    page = RandomGeneratorPage(root)

    root.mainloop()
    
        
        


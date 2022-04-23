from tkinter import *
from math import *  # we import all the math functions
import random
import numpy as np


class RandomGeneratorPage:
    """
    This class is used to generate random list of numbers, using random and numpy modules in python.
    """

    def __init__(self, master, tools):
        """
        This method is used to initialize the class.  It contains the following:
        - A frame that contains the following:
            - A label that displays the title of the page  (Label)  
            - A label that displays the length of the list  (Label)
            - A label that displays the seed value of the list  (Label)
            - A label that displays the high of the list(Label)
            - A label that displays the result  (Label)            
        """
        self.master = master
        #self.tools = tools
        #width = int(tools.screen_width*0.8)
        #height = int(tools.screen_height*0.8)
        #self.randomizer_frame = Frame(master, width=width, height=height, bg=tools.pallete["gray"])
        #self.master.add(self.randomizer_frame)
        self.master.title("Random Number Generator")
        self.master.resizable(True, True)
        self.randomizer_frame = Frame(self.master,  width=1000, height=1000, bg="#D3D8DE")
        self.randomizer_frame.grid(row=30, column=30)
        

        self.container = Frame(self.randomizer_frame, width=88888, height=88888, bg="#D3D8DE")
        self.container.pack()

        self.length_of_list_label = Label(self.container, text="length of list: ", font=("Helvetica", 15), )
        self.length_of_list_label.grid(row=0, column=0)

        self.length_of_list_entry = Entry(self.container)
        self.length_of_list_entry.grid(row=0, column=1, padx=5, pady=2)

        self.seed_label = Label(self.container, text="seed or low value : ", font=("Helvetica", 15))
        self.seed_label.grid(row=1, column=0)

        self.seed_entry = Entry(self.container)
        self.seed_entry.grid(row=1, column=1, padx=5, pady=2)

        self.high_label = Label(self.container, text="high value: ", font=("Helvetica", 15))
        self.high_label.grid(row=2, column=0)

        self.high_entry = Entry(self.container)
        self.high_entry.grid(row=2, column=1, padx=5, pady=2)

        self.generate_button = Button(self.container, text="generate",
                                          command=lambda: self.generate_list())
        self.generate_button.grid(row=3, column=0)

        self.result_label = Label(self.container, text="result: ", font=("Helvetica", 15))
        self.result_label.grid(row=3, column=1)

        self.result_variable = StringVar()
        self.result_entry = Entry(self.container, textvariable=self.result_variable, width=20,
                                   font= ("Helvetica", 15))
        self.result_entry.grid(row=5, column=1, columnspan=5, sticky="w")

        self.container.mainloop()

    def generate_list(self):
        """
        This method is used to generate a random list of numbers.  It contains:
        - A try/except block to catch the error if the user enters a non-integer value for the length of the list.

        """
        try:
            length_of_list_threshold = int(self.length_of_list_entry.get())
            seed_threshold = int(self.seed_entry.get())
            high_threshold = int(self.high_entry.get())
            random_list = np.random.randint(low= seed_threshold, high=high_threshold, size=length_of_list_threshold)
            self.result_variable.set(random_list)
        except Exception as e:
            print(e)


if __name__ == "__main__":
    root = Tk()
    root.geometry("500x500")
    app = RandomGeneratorPage(root, tools=None)
    root.mainloop()
        


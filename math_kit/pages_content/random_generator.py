import random
from tkinter import END, Frame, Label, Entry, Button, StringVar, LabelFrame, Checkbutton, messagebox, BooleanVar, IntVar 
import numpy as np


class RandomGeneratorPage:
    """
    This method is used to initialize the class.  It contains the following:
    - A frame that contains the following:
        - A label that displays the title of the page  (Label)  
        - A label that displays the length of the list  (Label)
        - A label that displays the seed value of the list  (Label)
        - A label that displays the high of the list(Label)
        - A label that displays the result  (Label)            
    """

    def __init__(self, master, tools):
        self.tools = tools
        
        width = int(tools.screen_width*0.8)
        height = int(tools.screen_height*0.8)
        
        self.randomizer_frame = Frame(master, width=width, height=height, bg=tools.pallete["gray"])
        master.add(self.randomizer_frame)
        
        headline = """Have you seen a digital random generator before!
        Generate a random numeric list or insert a list of your own"""
        
        self.title = Label(self.randomizer_frame, text=headline, justify="center",
                           bg=tools.pallete["gray"], fg=tools.pallete["purple"],
                           font=("Berlin Sans FB", int(tools.screen_width*0.02)))
        self.title.pack(pady=int(tools.screen_height*0.02))
        
        self.container = Frame(self.randomizer_frame, width=88888, height=88888, bg="#D3D8DE")
        self.container.pack()
        
        self.box_background_color = tools.pallete["gray"]
        self.entries_color = tools.pallete["dark blue"]
        self.entry_text_color = tools.pallete["white"]
        self.text_color = "black"
        
        self._LeftFrame()
        self._RightFrame()
        
        
        
    def _LeftFrame(self):
        """ Function to initialize the left frame items """
        self.left_frame = LabelFrame(self.container, bg=self.box_background_color,
                                height=int(self.tools.screen_height*0.5))
        self.left_frame.grid(row=0, column=0, padx=20, pady=10, sticky="nsew")

        self.left_title = Label(self.left_frame, text="Generate a random list", bg=self.box_background_color,
                                font=("Berlin Sans FB", int(self.tools.screen_width*0.02)), 
                                fg=self.text_color)
        
        
        self.length_of_list_label = Label(self.left_frame, text="Length of list: ", font=("Helvetica", 18),
                                          bg=self.box_background_color, fg=self.text_color)
        self.length_of_list_entry = Entry(self.left_frame, font=("Helvetica", 18), bg=self.entries_color,
                               fg=self.entry_text_color, width=8)

        self.low_label = Label(self.left_frame, text="Lower value : ", font=("Helvetica", 18),
                                          bg=self.box_background_color, fg=self.text_color)
        self.low_entry = Entry(self.left_frame, font=("Helvetica", 18), bg=self.entries_color,
                               fg=self.entry_text_color, width=8)

        self.high_label = Label(self.left_frame, text="Upper value: ", font=("Helvetica", 18),
                                          bg=self.box_background_color, fg=self.text_color)
        self.high_entry = Entry(self.left_frame, font=("Helvetica", 18), bg=self.entries_color,
                                fg=self.entry_text_color, width=8)

        self.generate_button = Button(self.left_frame, text="Generate", font=("Helvetica", 20, "bold"), cursor="hand2",
                                      bg=self.tools.pallete["blue"], fg=self.tools.pallete["white"],
                                      activebackground=self.tools.pallete["purple"],
                                      command=lambda: self._GenerateList())

        self.result_variable = StringVar()
        self.result_entry = Entry(self.left_frame, textvariable=self.result_variable,
                               fg=self.entry_text_color, font=("Helvetica", 18), bg=self.entries_color)
        
        
        self.left_title.grid(row=0, column=0, columnspan=2, sticky="nsew")
        
        self.length_of_list_label.grid(row=1, column=0)
        self.length_of_list_entry.grid(row=1, column=1)
        
        self.low_label.grid(row=2, column=0)
        self.low_entry.grid(row=2, column=1)
        
        self.high_label.grid(row=3, column=0)
        self.high_entry.grid(row=3, column=1)

        self.generate_button.grid(row=4, column=0, columnspan=2, sticky="ns")

        self.result_entry.grid(row=5, column=0, columnspan=2, sticky="nsew")
        
        
        for child in self.left_frame.winfo_children():
            child.grid_configure(padx=10, pady=10)       
        
        
        
        
    def _RightFrame(self):
        """ Function to initialize the right frame items"""
        self.right_frame = LabelFrame(self.container, bg=self.box_background_color)
        self.right_frame.grid(row=0, column=1, padx=20, pady=10, sticky="nsew")

        self.right_title = Label(self.right_frame, text="Create your list", bg=self.box_background_color,
                                font=("Berlin Sans FB", int(self.tools.screen_width*0.02)), fg=self.text_color)

        self.add_button = Button(self.left_frame, text="Add", font=("Helvetica", 15, "bold"), cursor="hand2",
                        bg=self.tools.pallete["blue"], fg=self.tools.pallete["white"],
                        activebackground=self.tools.pallete["purple"], command=lambda: self._AddItem())



        self.right_title.grid(row=0, column=0, columnspan=2, sticky="nsew")
        
        
        for child in self.right_frame.winfo_children():
            child.grid_configure(padx=10, pady=10)   
        

    def _AddItem(self):
        """ Function to add an item to the list """
        self.list_of_items.append(self.item_entry.get())
        self.item_entry.delete(0, END) 
        self.item_entry.insert(0, "")
        self.list_of_items_label.config(text="List of items: " + str(self.list_of_items))

    def _DeleteItem(self):
        """Function to delete an item from the list"""
        self.list_of_items.pop() 
        self.list_of_items_label.config(text="List of items: " + str(self.list_of_items))


    def _ClearItems(self):
        """ Function to clear the list of items """
        self.list_of_items = []
        self.list_of_items_label.config(text="List of items: " + str(self.list_of_items))

    def _PickItem(self):
        """ Function to pick an item from the list """
        self.picked_item = random.choice(self.list_of_items)
        self.picked_item_label.config(text="Picked item: " + str(self.picked_item))
    
    def _GenerateList(self):
        """
        This method is used to generate a random list of numbers.  It contains:
        - A try/except block to catch the error if the user enters a non-integer value for the length of the list.

        """
        
        
        try:
            length_of_list_threshold = int(self.length_of_list_entry.get())
            seed_threshold = int(self.low_entry.get())
            high_threshold = int(self.high_entry.get())
            random_list = np.random.randint(low= seed_threshold, high=high_threshold, size=length_of_list_threshold)
            self.result_variable.set(random_list)
        
        except:
            messagebox.showerror("Invalid Selections !", "You have to fill all fields with valid selections.")
            




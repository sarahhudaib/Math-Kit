from tkinter import Frame, Label, Entry, Button, StringVar, LabelFrame, messagebox, Scrollbar, Listbox, IntVar, Checkbutton, END
from PIL import Image, ImageDraw, ImageFilter, ImageTk
import numpy as np
import random


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
        
        self.container = Frame(self.randomizer_frame, width=width, bg=tools.pallete["gray"])
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
        
        self.length_of_list_variable = StringVar()
        self.length_of_list_entry = Entry(self.left_frame, font=("Helvetica", 18), bg=self.entries_color,
                               fg=self.entry_text_color, width=8, textvariable=self.length_of_list_variable)

        self.low_label = Label(self.left_frame, text="Lower value:", font=("Helvetica", 18),
                                          bg=self.box_background_color, fg=self.text_color)
        
        self.low_variable = StringVar()
        self.low_entry = Entry(self.left_frame, font=("Helvetica", 18), bg=self.entries_color,
                               fg=self.entry_text_color, width=8, textvariable=self.low_variable)

        self.high_label = Label(self.left_frame, text="Upper value:", font=("Helvetica", 18),
                                          bg=self.box_background_color, fg=self.text_color)
        
        self.high_variable = StringVar()
        self.high_entry = Entry(self.left_frame, font=("Helvetica", 18), bg=self.entries_color,
                                fg=self.entry_text_color, width=8, textvariable=self.high_variable)

        self.generate_button = Button(self.left_frame, text="Generate", font=("Helvetica", 20, "bold"), cursor="hand2",
                                      bg=self.tools.pallete["blue"], fg=self.tools.pallete["white"],
                                      activebackground=self.tools.pallete["purple"],
                                      command=lambda: self._GenerateList())

        self.csv_left_button = Button(self.left_frame, text="CSV", font=("Helvetica", 15, "bold"), cursor="hand2",
                        bg=self.tools.pallete["blue"], fg=self.tools.pallete["white"],
                        activebackground=self.tools.pallete["purple"], command=lambda: self._ExportCSV("left"))

        clear_fieald_image_size = int(self.tools.screen_width*0.02)
        self.clear_field_icon = Image.open(r"../math_kit/assets/icons/clear.png")
        self.clear_field_icon = self.clear_field_icon.resize((clear_fieald_image_size, clear_fieald_image_size))
        self.clear_field_icon_img = ImageTk.PhotoImage(self.clear_field_icon)
        self.clear_field_img_button = Button(self.left_frame, image=self.clear_field_icon_img, 
                                              bg=self.tools.pallete["blue"], bd=1, cursor="hand2", 
                                              activebackground=self.tools.pallete["purple"], 
                                            command=lambda: self._ClearFields())
        self.clear_field_img_button.image = self.clear_field_icon_img
        
        
        self.result_variable = StringVar()
        self.result_entry = Entry(self.left_frame, textvariable=self.result_variable,
                               fg=self.entry_text_color, font=("Helvetica", 18), bg=self.entries_color)
        
        
        self.left_title.grid(row=0, column=0, columnspan=4, sticky="nsew")
        
        self.length_of_list_label.grid(row=1, column=0, columnspan=2)
        self.length_of_list_entry.grid(row=1, column=2, columnspan=2)
        
        self.low_label.grid(row=2, column=0, columnspan=2)
        self.low_entry.grid(row=2, column=2, columnspan=2)
        
        self.high_label.grid(row=3, column=0, columnspan=2)
        self.high_entry.grid(row=3, column=2, columnspan=2)

        self.generate_button.grid(row=4, column=0, columnspan=2, sticky="ns")
        self.csv_left_button.grid(row=4, column=2, sticky="e")
        self.clear_field_img_button.grid(row=4, column=3, sticky="w")

        self.result_entry.grid(row=5, column=0, columnspan=4, sticky="nsew")
        
        
        for child in self.left_frame.winfo_children():
            child.grid_configure(padx=10, pady=10)       
        
        
    def _RightFrame(self):
        """ Function to initialize the right frame items"""
        self.right_frame = LabelFrame(self.container, bg=self.box_background_color)
        self.right_frame.grid(row=0, column=1, padx=20, pady=10, sticky="nsew")

        self.right_title = Label(self.right_frame, text="Create your own list", bg=self.box_background_color,
                                font=("Berlin Sans FB", int(self.tools.screen_width*0.02)), fg=self.text_color)

        self.add_item_button = Button(self.right_frame, text="Add", font=("Helvetica", 15, "bold"), cursor="hand2",
                        bg=self.tools.pallete["blue"], fg=self.tools.pallete["white"],
                        activebackground=self.tools.pallete["purple"], command=lambda: self._AddItem())
        
        self.add_item_variable = StringVar()
        self.add_item_entry = Entry(self.right_frame, font=("Helvetica", 18), bg=self.entries_color,
                               fg=self.entry_text_color, width=8, textvariable=self.add_item_variable)
        
        self.x_times_label = Label(self.right_frame, text="x", font=("Helvetica", 18),
                                          bg=self.box_background_color, fg=self.text_color)

        self.x_times_variable = StringVar()        
        self.x_times_entry = Entry(self.right_frame, font=("Helvetica", 18), bg=self.entries_color,
                               fg=self.entry_text_color, width=4, textvariable=self.x_times_variable)
        self.x_times_variable.set("1")
        
        

        self.delete_item_button = Button(self.right_frame, text="Delete", font=("Helvetica", 15, "bold"), cursor="hand2",
                        bg=self.tools.pallete["blue"], fg=self.tools.pallete["white"],
                        activebackground=self.tools.pallete["purple"], command=lambda: self._DeleteItem())

        self.clear_item_button = Button(self.right_frame, text="Clear", font=("Helvetica", 15, "bold"), cursor="hand2",
                        bg=self.tools.pallete["blue"], fg=self.tools.pallete["white"],
                        activebackground=self.tools.pallete["purple"], command=lambda: self._ClearItems())
        
        self.number_label = Label(self.right_frame, text="#Samples:", font=("Helvetica", 18),
                                          bg=self.box_background_color, fg=self.text_color)
        
        self.picked_number_variable = StringVar()        
        self.picked_number = Entry(self.right_frame, font=("Helvetica", 18), bg=self.entries_color,
                               fg=self.entry_text_color, width=4, textvariable=self.picked_number_variable)
        self.picked_number_variable.set("1")
        
        self.unique_variable = IntVar()
        self.unique_checkbox = Checkbutton(self.right_frame, text="Unique", variable=self.unique_variable,
                                           cursor="hand2", bg=self.tools.pallete["gray"], fg=self.text_color, 
                                           font=("Helvetica", 14))
        
        self.csv_right_button = Button(self.right_frame, text="CSV", font=("Helvetica", 15, "bold"), cursor="hand2",
                        bg=self.tools.pallete["blue"], fg=self.tools.pallete["white"],
                        activebackground=self.tools.pallete["purple"], command=lambda: self._ExportCSV("right"))
        
        self.pick_item_button = Button(self.right_frame, text="Pick", font=("Helvetica", 15, "bold"), cursor="hand2",
                        bg=self.tools.pallete["blue"], fg=self.tools.pallete["white"],
                        activebackground=self.tools.pallete["purple"], command=lambda: self._PickItem())
        
        self.picked_result_variable = StringVar()
        self.picked_result_entry = Entry(self.right_frame, font=("Helvetica", 18), bg=self.entries_color,
                               fg=self.entry_text_color, textvariable=self.picked_result_variable)
        
        self.items_box = Scrollbar(self.right_frame, width=int(self.tools.screen_width*0.02))
        self.items_list = Listbox(self.right_frame, yscrollcommand=self.items_box.set)
        self.items_box.config(command=self.items_list.yview)
        
        
        
        



        self.right_title.grid(row=0, column=0, columnspan=5, sticky="nsew")
        
        self.add_item_button.grid(row=1, column=0, sticky="ew")
        self.add_item_entry.grid(row=1, column=1, sticky="ew")
        self.x_times_label.grid(row=1, column=2, sticky="ew")
        self.x_times_entry.grid(row=1, column=3, sticky="ew")
        
        self.items_box.grid(row=1, column=4, rowspan=5, sticky="nsew")
        self.items_list.grid(row=1, column=4, rowspan=5, sticky="nsew")
        
        self.delete_item_button.grid(row=2, column=0, columnspan=2, sticky="ew")
        self.clear_item_button.grid(row=2, column=2, columnspan=2, sticky="ew")
        
        self.number_label.grid(row=3, column=0)
        self.picked_number.grid(row=3, column=1)
        self.unique_checkbox.grid(row=3, column=2, columnspan=2)
        
        self.pick_item_button.grid(row=4, column=0, columnspan=3, sticky="ew")
        self.csv_right_button.grid(row=4, column=3)
        self.picked_result_entry.grid(row=5, column=0, columnspan=4, sticky="ew")
        

        
        
        for child in self.right_frame.winfo_children():
            child.grid_configure(padx=10, pady=10)   
        
        

    def _AddItem(self):
        
        x = self.x_times_entry.get()
        item = self.add_item_entry.get()
        
        if x.isdigit():
            if item.strip() != "":
                for i in range(int(x)):
                    self.items_list.insert("end", item) 
            else:
                messagebox.showerror("Invalid Input !", "You have to enter a text in the field after the (add).")        
        else:
            messagebox.showerror("Invalid Input !", "You have to enter a number in the field after the (x times).")
    
    
    def _DeleteItem(self):
        self.items_list.delete("anchor") 


    def _ClearItems(self):
        for i in range(self.items_list.size()):
            self.items_list.delete(0)


    def _PickItem(self):
        is_unique = int(self.unique_variable.get())
        number = self.picked_number.get()
        items = list(self.items_list.get(0, END))
        
        if number.isdigit():
            if len(items) != 0:
                if is_unique:
                    result = random.sample(items, k=int(number))
                else:
                    result = random.choices(items, k=int(number))
                
                self.picked_result_variable.set(result)
                
            else:
                messagebox.showerror("Invalid Input !", "The list is empty.")            
        else:
            messagebox.showerror("Invalid Input !", "You have to enter a number in the field after the (#Samples).")
            
            
    def _ExportCSV(self, entry):
        
        if entry == "right":
            pass
        else:
            pass
    
    
    def _CopyRandomList(self):
        """" Function to copy the random list to the clipboard """
        self.clipboard_clear()
        self.clipboard_append(str(self.list_of_items))
        
    
    def _ClearFields(self):
        self.length_of_list_variable.set("")
        self.low_variable.set("")
        self.high_variable.set("")
        
        
    def _GenerateList(self):
        """
        This method is used to generate a random list of numbers.  It contains:
        - A try/except block to catch the error if the user enters a non-integer value for the length of the list.

        """
     
        try:
            length_of_list_threshold = int(self.length_of_list_entry.get())
            lower_threshold = int(self.low_entry.get())
            upper_threshold = int(self.high_entry.get())
            random_list = np.random.randint(low= lower_threshold, high=upper_threshold, size=length_of_list_threshold)
            self.result_variable.set(random_list)
        
        except:
            messagebox.showerror("Invalid Selections !", "You have to fill all fields with valid selections.")

        



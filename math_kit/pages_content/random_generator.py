from tkinter import Frame, Label, Entry, Button, StringVar, LabelFrame, messagebox, Scrollbar, Listbox, IntVar, Checkbutton, END, filedialog
from turtle import width
from PIL import Image, ImageTk
import numpy as np
import random
import csv
import shutil
import customtkinter


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
        
        self.randomizer_frame = customtkinter.CTkFrame(master, width=width, height=height)
        master.add(self.randomizer_frame)
        
        headline = """Have you seen a digital random generator before!
        Generate a random numeric list or insert a list of your own"""
        
        self.title = customtkinter.CTkLabel(self.randomizer_frame, text=headline, justify="center",
                          text_font=("Berlin Sans FB", int(tools.screen_width*0.02)))
        self.title.pack(pady=int(tools.screen_height*0.02))
        
        self.container = Frame(self.randomizer_frame, width=width, bg=tools.pallete["dark mode"])
        self.container.pack()
        
        self.box_background_color = tools.pallete["dark mode"]
        self.text_color = "black"
        self.entries_color = "white"
        self.entry_text_color = "black"
        
        self._LeftFrame()
        self._RightFrame()
        
        
    def _LeftFrame(self):
        """ Function to initialize the left frame items """
        self.left_frame = LabelFrame(self.container, bg=self.box_background_color,
                                height=int(self.tools.screen_height*0.5))
        self.left_frame.grid(row=0, column=0, padx=20, pady=10, sticky="nsew")

        self.left_title = customtkinter.CTkLabel(self.left_frame, text="Generate a random list", 
                            text_font=("Berlin Sans FB", int(self.tools.screen_width*0.02)))
        
        
        self.length_of_list_label = customtkinter.CTkLabel(self.left_frame, text="Length of list: ", 
                    text_font=("Helvetica", 18))
        
        self.length_of_list_variable = StringVar()
        self.length_of_list_entry = customtkinter.CTkEntry(self.left_frame, text_font=("Helvetica", 18), 
                                         width=140, textvariable=self.length_of_list_variable)
        self.length_of_list_variable.set("10")

        self.low_label = customtkinter.CTkLabel(self.left_frame, text="Lower value:", 
                        text_font=("Helvetica", 18))
        
        self.low_variable = StringVar()
        self.low_entry = customtkinter.CTkEntry(self.left_frame, text_font=("Helvetica", 18),
                                        width=140, textvariable=self.low_variable)
        self.low_variable.set("0")

        self.high_label = customtkinter.CTkLabel(self.left_frame, text="Upper value:", text_font=("Helvetica", 18))
        
        self.high_variable = StringVar()
        self.high_entry = customtkinter.CTkEntry(self.left_frame, text_font=("Helvetica", 18),
                                            width=140, textvariable=self.high_variable)
        self.high_variable.set("1000")

        self.generate_button = customtkinter.CTkButton(self.left_frame, text="Generate", 
                            text_font=("Helvetica", 20, "bold"), cursor="hand2",
                            command=lambda: self._GenerateList(), hover_color=self.tools.pallete["purple"])

        self.csv_left_button = customtkinter.CTkButton(self.left_frame, text="CSV", 
                        text_font=("Helvetica", 15, "bold"), cursor="hand2", width=70,
                        command=lambda: self._ExportCSV("left"), hover_color=self.tools.pallete["purple"])

        clear_fieald_image_size = int(self.tools.screen_width*0.02)
        self.clear_field_icon = Image.open(r"../math_kit/assets/icons/clear.png")
        self.clear_field_icon = self.clear_field_icon.resize((clear_fieald_image_size, clear_fieald_image_size))
        self.clear_field_icon_img = ImageTk.PhotoImage(self.clear_field_icon)
        self.clear_field_img_button = customtkinter.CTkButton(self.left_frame, image=self.clear_field_icon_img, 
                            cursor="hand2", command=lambda: self._ClearFields(), text="", 
                            hover_color=self.tools.pallete["purple"], width=clear_fieald_image_size,
                            height=clear_fieald_image_size)
        self.clear_field_img_button.image = self.clear_field_icon_img
        
        
        self.result_variable = StringVar()
        self.result_entry = customtkinter.CTkEntry(self.left_frame, textvariable=self.result_variable,
                               text_font=("Helvetica", 18))
        
        
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

        self.right_title = customtkinter.CTkLabel(self.right_frame, text="Create your own list", 
                                text_font=("Berlin Sans FB", int(self.tools.screen_width*0.02)))

        self.add_item_button = customtkinter.CTkButton(self.right_frame, text="Add", 
                        text_font=("Helvetica", 15, "bold"), cursor="hand2",
                        command=lambda: self._AddItem(), hover_color=self.tools.pallete["purple"])
        
        self.add_item_variable = StringVar()
        self.add_item_entry = customtkinter.CTkEntry(self.right_frame, text_font=("Helvetica", 18),
                            width=100, textvariable=self.add_item_variable)
        self.add_item_variable.set("red ball")
        
        self.x_times_label = customtkinter.CTkLabel(self.right_frame, text="x", text_font=("Helvetica", 18),
                                                    width=5)

        self.x_times_variable = StringVar()        
        self.x_times_entry = customtkinter.CTkEntry(self.right_frame, text_font=("Helvetica", 18), 
                                    width=50, textvariable=self.x_times_variable)
        self.x_times_variable.set("1")
        

        self.delete_item_button = customtkinter.CTkButton(self.right_frame, text="Delete", 
                    text_font=("Helvetica", 15, "bold"), cursor="hand2", width=100,
                    command=lambda: self._DeleteItem(), hover_color=self.tools.pallete["purple"])

        self.clear_item_button = customtkinter.CTkButton(self.right_frame, text="Clear", 
                    text_font=("Helvetica", 15, "bold"), cursor="hand2", width=100,
                    command=lambda: self._ClearItems(), hover_color=self.tools.pallete["purple"])
        
        clear_field_2_image_size = int(self.tools.screen_width*0.02)
        self.clear_field_2_icon = Image.open(r"../math_kit/assets/icons/clear.png")
        self.clear_field_2_icon = self.clear_field_2_icon.resize((clear_field_2_image_size, clear_field_2_image_size))
        self.clear_field_2_icon_img = ImageTk.PhotoImage(self.clear_field_2_icon)
        self.clear_field_2_img_button = customtkinter.CTkButton(self.right_frame, image=self.clear_field_2_icon_img, 
                            cursor="hand2", command=lambda: self._ClearFields2(), text="", 
                            hover_color=self.tools.pallete["purple"], width=clear_field_2_image_size,
                            height=clear_field_2_image_size)
        self.clear_field_2_img_button.image = self.clear_field_2_icon_img
                
        
        self.number_label = customtkinter.CTkLabel(self.right_frame, text="#Samples:", 
                                                   text_font=("Helvetica", 18))
        
        self.picked_number_variable = StringVar()        
        self.picked_number = customtkinter.CTkEntry(self.right_frame, text_font=("Helvetica", 18), 
                                        width=100, textvariable=self.picked_number_variable)
        self.picked_number_variable.set("3")
        
        self.unique_variable = IntVar()
        self.unique_checkbox = customtkinter.CTkCheckBox(self.right_frame, text="Unique", 
                    variable=self.unique_variable, cursor="hand2", text_font=("Helvetica", 14))
        
        self.csv_right_button = customtkinter.CTkButton(self.right_frame, text="CSV", 
                        text_font=("Helvetica", 15, "bold"), cursor="hand2",
                         command=lambda: self._ExportCSV("right"), hover_color=self.tools.pallete["purple"])
        
        self.pick_item_button = customtkinter.CTkButton(self.right_frame, text="Pick", 
                        text_font=("Helvetica", 15, "bold"), cursor="hand2",
                        command=lambda: self._PickItem(), hover_color=self.tools.pallete["purple"])
        
        self.picked_result_variable = StringVar()
        self.picked_result_entry = customtkinter.CTkEntry(self.right_frame, text_font=("Helvetica", 18), 
                        textvariable=self.picked_result_variable)
        
        self.items_box = Scrollbar(self.right_frame, width=int(self.tools.screen_width*0.02))
        self.items_list = Listbox(self.right_frame, yscrollcommand=self.items_box.set)
        self.items_box.config(command=self.items_list.yview)
        

        self.right_title.grid(row=0, column=0, columnspan=5, sticky="nsew")
        
        self.add_item_button.grid(row=1, column=0, sticky="ew")
        self.add_item_entry.grid(row=1, column=1)
        self.x_times_label.grid(row=1, column=2, sticky="ew")
        self.x_times_entry.grid(row=1, column=3, sticky="w")
        
        self.items_box.grid(row=1, column=4, rowspan=7, sticky="nsew")
        self.items_list.grid(row=1, column=4, rowspan=7, sticky="nsew")
        
        self.delete_item_button.grid(row=2, column=0, sticky="ew")
        self.clear_item_button.grid(row=2, column=1, sticky="ew")
        self.clear_field_2_img_button.grid(row=2, column=3, columnspan=1, sticky="e")
        
        self.number_label.grid(row=3, column=0)
        self.picked_number.grid(row=3, column=1)
        self.unique_checkbox.grid(row=3, column=2, columnspan=2, sticky="e")
        
        self.pick_item_button.grid(row=4, column=0, columnspan=2, sticky="ew")
        self.csv_right_button.grid(row=4, column=2, columnspan=2)
        self.picked_result_entry.grid(row=7, column=0, columnspan=4, sticky="ew")
        

        
        
        for child in self.right_frame.winfo_children():
            child.grid_configure(padx=10, pady=10)   
          

    def _GenerateList(self):
        """
        This method is used to generate a random list of numbers.  It contains:
        - A try/except block to catch the error if the user enters a non-integer value for the length of the list.

        """
     
        try:
            length_of_list_threshold = int(self.length_of_list_entry.get().strip())
            lower_threshold = int(self.low_entry.get().strip())
            upper_threshold = int(self.high_entry.get().strip())
            random_list = np.random.randint(low=lower_threshold, high=upper_threshold, size=length_of_list_threshold)
            self.result_variable.set(" ".join([str(i) for i in list(random_list)]))
            
            self._SaveAsCSV(random_list, "left")
        
        except:
            messagebox.showerror("Invalid Selections !", "You have to fill all fields with valid selections.")

        
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
                    random_list = random.sample(items, k=int(number))
                else:
                    random_list = random.choices(items, k=int(number))
                
                self.picked_result_variable.set(" ".join([str(i) for i in list(random_list)]))
                
                self._SaveAsCSV(random_list, "right")
                
            else:
                messagebox.showerror("Invalid Input !", "The list is empty.")            
        else:
            messagebox.showerror("Invalid Input !", "You have to enter a number in the field after the (#Samples).")
            
            
    def _SaveAsCSV(self, result, entry):
        
        if entry == "left":
            with open(r'../math_kit/assets/csv/left_result.csv', 'w') as f:
                write = csv.writer(f)
                write.writerow(result)
                # write.writerows(rows)        
        else:
            with open(r'../math_kit/assets/csv/right_result.csv', 'w') as f:
                write = csv.writer(f)
                write.writerow(result)
                # write.writerows(rows)
      
    def _ExportCSV(self, entry):
                
        filename = filedialog.asksaveasfile(
            mode='w', 
            defaultextension=".csv",
            initialdir=r"C:", 
            title="Select a directory and name the image")
            
        if filename is None:
            messagebox.showerror("Error", "Couldn't save the file !!")
            return
        
        if entry == "left":    
            try:
                shutil.copy(r"../math_kit/assets/csv/left_result.csv", filename.name) 
            except:
                messagebox.showerror("Error", "Couldn't save the file !!")
                
        else:
            try:
                shutil.copy(r"../math_kit/assets/csv/right_result.csv", filename.name) 
            except:
                messagebox.showerror("Error", "Couldn't save the file !!")
            
    
    def _CopyRandomList(self):
        """" Function to copy the random list to the clipboard """
        self.clipboard_clear()
        self.clipboard_append(str(self.list_of_items))
        
    
    def _ClearFields(self):
        self.length_of_list_variable.set("")
        self.low_variable.set("")
        self.high_variable.set("")
        self.result_variable.set("")
        
    
    def _ClearFields2(self):
        self.add_item_variable.set("")
        self.x_times_variable.set("")
        self.picked_number_variable.set("")
        self.picked_result_variable.set("")
        




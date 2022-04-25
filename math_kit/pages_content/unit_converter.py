from tkinter import Label, Tk, StringVar, Entry, Button, Frame, ttk, DoubleVar, messagebox
from PIL import Image, ImageDraw, ImageFilter, ImageTk


UCdict = {
    "length": {
        "meters": {
            "meters": lambda x: x,
            "yards": lambda x: 1.0936 * x,
            "feet": lambda x: 3.28084 * x,
            "centimeters": lambda x: 100 * x,
            "kilometers": lambda x: x / 1000.0,
            "miles": lambda x: x / 1000.0 / 1.60934
        },
        "yards": {
            "yards": lambda x: x,
            "meters": lambda x: x / 1.0936,
            "centimeters": lambda x: x / 1.0936 * 100,
            "feet": lambda x: 3 * x,
            "kilometers": lambda x: 0.0009144 * x,
            "miles": lambda x: 0.0009144 * x / 1.60934
        },
        "centimeters": {
            "centimeters": lambda x: x,
            "meters": lambda x: x / 100.0,
            "yards": lambda x: x * 1.0936 / 100,
            "feet": lambda x: x * 3.28084 / 100,
            "miles": lambda x: x * 100 * 1000 / 1.60934
        },
        "feet": {
            "feet": lambda x: x,
            "meters": lambda x: x / 3.28084,
            "yards": lambda x: x / 3.0,
            "centimeters": lambda x: x * 100 / 3.28084,
            "kilometers": lambda x: x * 3.28084 / 1000,
            "miles": lambda x: x * 3.28084 / 1000 / 1.60934
        },
        "miles": {
            "miles": lambda x: x,
            "kilometers": lambda x: 1.60934 * x,
            "meters": lambda x: 1.60934 * x * 1000,
            "centimeters": lambda x: 1.60934 * x * 1000 * 100,
            "feet": lambda x: 5280 * x,
            "yards": lambda x: 5280 * x / 3.0
        },
        "kilometers": {
            "kilometers": lambda x: x,
            "meters": lambda x: x * 1000,
            "centimeters": lambda x: x * 1000 * 100,
            "miles": lambda x: x / 1.60934,
            "yards": lambda x: x * 1093.61,
            "feet": lambda x: x * 1093.61 * 3
        }
    },
    "temperature": {
        "celsius": {
            "celsius": lambda x: x,
            "fahrenheit": lambda x: 1.8 * x + 32,
            "kelvin": lambda x: x + 273,
        },
        "fahrenheit": {
            "fahrenheit": lambda x: x,
            "celsius": lambda x: (x - 32) * 5.0 / 9.0,
            "kelvin": lambda x: (x - 32) * 5.0 / 9.0 + 273,
        },
        "kelvin": {
            "kelvin": lambda x: x,
            "celsius": lambda x: x - 273,
            "fahrenheit": lambda x: 1.8 * (x - 273) + 32,
        }
    }
}


class UnitConverterPage:
    """
    This class  is the settings page of the application. It contains the following:
    - A title label that displays the name of the application   (Label)
    - A label that displays the info of the application         (Label)
    - A label that displays the guide of the application        (Label)
    """
    
    def __init__(self, master, tools):
        
        width = int(tools.screen_width*0.8)
        height = int(tools.screen_height*0.8)
        
        self.unit_converter_frame = Frame(master, width=width, height=height, bg=tools.pallete["gray"])
        master.add(self.unit_converter_frame)
        
        headline = """Converting units has never been easier!
        Select quantity and units, then enter a value and click \"Convert\""""
        
        self.title = Label(self.unit_converter_frame, text=headline, justify="center",
                           bg=tools.pallete["gray"], fg=tools.pallete["purple"],
                           font=("Berlin Sans FB", int(tools.screen_width*0.02)))
        self.title.pack(pady=int(tools.screen_height*0.02))
        
        self.container = Frame(self.unit_converter_frame, width=width, height=height, bg=tools.pallete["gray"])
        self.container.pack()
        

        self.quantity_label = Label(self.container, text="Select a quantity set:", font= ("Helvetica", 25),
                               bg=tools.pallete["gray"])
        
        self.quantity_variable = StringVar()

        self.quantity_box = ttk.Combobox(self.container, textvariable=self.quantity_variable, font= ("Helvetica", 15),
                                         state="readonly", values=tuple([x.capitalize() for x in UCdict.keys()]),
                                         width=int(tools.screen_width*0.02))
        self.quantity_box.bind("<<ComboboxSelected>>", self._AvailableUnits)

        self.convert_label = Label(self.container, text="Convert this value:", font= ("Helvetica", 25),
                               bg=tools.pallete["gray"])

        self.user_input = DoubleVar()
        self.user_input_entry = Entry(self.container, textvariable=self.user_input, 
                                      font= ("Helvetica", 15), width=int(tools.screen_width*0.02))

        clear_image_size = int(tools.screen_width*0.02)
        self.clear_icon = Image.open(r"../math_kit/assets/icons/clear.png")
        self.clear_icon = self.clear_icon.resize((clear_image_size, clear_image_size))
        self.clear_icon_img = ImageTk.PhotoImage(self.clear_icon)
        self.clear_img_button = Button(self.container, image=self.clear_icon_img, bg=tools.pallete["blue"], bd=1,
                               cursor="hand2", activebackground=tools.pallete["purple"], 
                               command=lambda: self.user_input.set(""))
        self.clear_img_button.image = self.clear_icon_img
        

        self.from_label = Label(self.container, text="from", font= ("Helvetica", 25),
                               bg=tools.pallete["gray"])
        
        self.from_variable = StringVar()
        self.unit_from_box = ttk.Combobox(self.container, textvariable=self.from_variable, state="readonly",
                                           font= ("Helvetica", 15))

        self.to_label = Label(self.container, text="to", font= ("Helvetica", 25),
                               bg=tools.pallete["gray"])

        self.to_variable = StringVar()
        self.unit_to_box = ttk.Combobox(self.container, textvariable=self.to_variable, state="readonly",
                                         font= ("Helvetica", 15))
        
        
        image_size = int(tools.screen_width*0.02)
        self.flip_icon = Image.open(r"../math_kit/assets/icons/flip.png")
        self.flip_icon = self.flip_icon.resize((image_size, image_size))
        self.flip_icon_img = ImageTk.PhotoImage(self.flip_icon)
        self.flip_img_button = Button(self.container, image=self.flip_icon_img, bg=tools.pallete["blue"], bd=1,
                               cursor="hand2", activebackground=tools.pallete["purple"], command=self._Flip)
        self.flip_img_button.image = self.flip_icon_img


        self.convert_button = Button(self.container, text="Convert", command=self._Convert, cursor="hand2",
                                     font= ("Helvetica", 25), bg=tools.pallete["blue"])

        self.result_variable = StringVar()
        self.result_text = Entry(self.container, textvariable=self.result_variable, 
                                 font= ("Helvetica", 15), width=int(tools.screen_width*0.04), 
                                 bg=tools.pallete["dark blue"], fg=tools.pallete["white"])
        
        clear_result_image_size = int(tools.screen_width*0.02)
        self.clear_result_icon = Image.open(r"../math_kit/assets/icons/clear.png")
        self.clear_result_icon = self.clear_result_icon.resize((clear_result_image_size, clear_result_image_size))
        self.clear_result_icon_img = ImageTk.PhotoImage(self.clear_result_icon)
        self.clear_result_img_button = Button(self.container, image=self.clear_result_icon_img, bg=tools.pallete["blue"], bd=1,
                               cursor="hand2", activebackground=tools.pallete["purple"], 
                               command=lambda: self.result_variable.set(""))
        self.clear_result_img_button.image = self.clear_result_icon_img



        self.quantity_label.grid(row=0, column=0, columnspan=2, sticky="w")
        self.quantity_box.grid(row=0, column=2, columnspan=2, sticky="e")
        self.convert_label.grid(row=1, column=0, columnspan=2, sticky="w")
        self.user_input_entry.grid(row=1, column=2, columnspan=2, sticky="e")
        self.clear_img_button.grid(row=1, column=4)
        
        self.from_label.grid(row=3, column=0)
        self.unit_from_box.grid(row=3, column=1)
        self.to_label.grid(row=3, column=2)
        self.unit_to_box.grid(row=3, column=3)
        self.flip_img_button.grid(row=3, column=4)
        
        self.convert_button.grid(row=4, column=0, columnspan=4)
        self.result_text.grid(row=5, column=0, columnspan=4)
        self.clear_result_img_button.grid(row=5, column=4)


        # * Highly important
        for child in self.container.winfo_children():
            child.grid_configure(padx=5, pady=15)       
        

    def _Flip(self):
        try: 
            unit_from = self.from_variable.get()
            unit_to = self.to_variable.get()
            
            self.unit_from_box.set(unit_to)
            self.unit_to_box.set(unit_from)
            
        except:
            messagebox.showerror("Invalid Selections !", "You have to fill both fields with valid selections.")



    def _Convert(self, *args):
        """Calculate the conversion."""
        try: 
            unit_from = self.from_variable.get()
            unit_to = self.to_variable.get()
            quantity = self.quantity_variable.get()
            input_num = self.user_input.get()
            
            result = UCdict[quantity.lower()][unit_from][unit_to](input_num)
            truncated_result = "{0:.4f}".format(result)    
            string_result = f"{input_num} {unit_from} = {truncated_result} {unit_to}"
        
            self.result_variable.set(string_result)

        except:
            self.result_variable.set("Invalid Selections !")
            messagebox.showerror("Invalid Selections !", "You have to fill all fields with valid selections.")

                        


    def _AvailableUnits(self, *args):
        """ Function to set the unit comboboxes to the selected unit. """
        
        quantity_lowered = self.quantity_variable.get().lower()
        
        self.from_variable.set(quantity_lowered)
        self.to_variable.set(quantity_lowered)
        
        self.unit_from_box['values'] = tuple(UCdict[quantity_lowered].keys())
        self.unit_to_box['values'] = tuple(UCdict[quantity_lowered].keys())
        
        self.unit_from_box.current(0)
        self.unit_to_box.current(1)





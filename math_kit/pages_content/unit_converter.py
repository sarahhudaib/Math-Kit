from tkinter import Label, Tk, StringVar, Entry, Button, Frame, ttk, DoubleVar
from pages_content.unit_convertor_dict import conversion_dict as UCdict


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
        
        self.container = Frame(self.unit_converter_frame, width=width, height=height, bg=tools.pallete["gray"])
        self.container.pack()
        

        self.quantity = Label(self.container, text="Select a quantity set", font= ("Helvetica", 25),
                               bg=tools.pallete["gray"])
        self.quantity.grid(row=0, column=0, columnspan=4, sticky="w")
        
        self.quantity_variable = StringVar()
        
        self.quantity_box = ttk.Combobox(self.container, textvariable=self.quantity_variable, font= ("Helvetica", 15),
                                         state="readonly", values=tuple([x.capitalize() for x in UCdict.keys()]))
        self.quantity_box.bind("<<ComboboxSelected>>", self._AvailableUnits)
        self.quantity_box.grid(row=0, column=4)

        self.convert = Label(self.container, text="Convert", font= ("Helvetica", 25),
                               bg=tools.pallete["gray"])
        self.convert.grid(row=1, column=0)

        self.user_input = DoubleVar()
        self.user_input_entry = Entry(self.container, textvariable=self.user_input, width=20,
                                      font= ("Helvetica", 15))
        self.user_input_entry.grid(row=1, column=1)

        self.from_variable = StringVar()
        self.unit_from_box = ttk.Combobox(self.container, textvariable=self.from_variable, state="readonly",
                                           font= ("Helvetica", 15))
        self.unit_from_box.grid(row=1, column=2)

        self.to = Label(self.container, text="to", font= ("Helvetica", 25),
                               bg=tools.pallete["gray"])
        self.to.grid(row=1, column=3)

        self.to_variable = StringVar()
        self.unit_to_box = ttk.Combobox(self.container, textvariable=self.to_variable, state="readonly",
                                         font= ("Helvetica", 15))
        self.unit_to_box.grid(row=1, column=4)

        self.convert_button = Button(self.container, text="Apply", command=self._Convert,
                                     font= ("Helvetica", 25), bg=tools.pallete["blue"])
        self.convert_button.grid(row=2, columnspan=5)

        self.result_variable = StringVar()
        self.result_entry = Entry(self.container, textvariable=self.result_variable, width=40,
                                   font= ("Helvetica", 15))
        self.result_entry.grid(row=3, column=0, columnspan=5, sticky="w")

        for child in self.container.winfo_children():
            child.grid_configure(padx=5, pady=5)

        self.container.mainloop()



    def _Convert(self, *args):
        """Calculate the conversion."""
        try: 
            result = UCdict[self.from_variable.get()][self.to_variable.get()](float(self.quantity_variable.get()))
            self.result_variable.set(result)
        except KeyError:
            self.result_variable.set("")
            pass
        
        result = "{0:.4f}".format(UCdict[self.quantity_variable.get().lower()][self.from_variable.get()][self.to_variable.get()](self.user_input.get()))
        result_string = self.user_input.get(), self.from_variable.get(), "=", result, self.to_variable.get()
        self.result_variable.set(result_string)


    def _AvailableUnits(self, *args):
        """ Function to set the unit comboboxes to the selected unit. """
        self.from_variable.set(self.quantity_variable.get().lower())
        self.to_variable.set(self.quantity_variable.get().lower())
        self.unit_from_box['values'] = tuple(UCdict[self.quantity_variable.get().lower()].keys())
        self.unit_to_box['values'] = tuple(UCdict[self.quantity_variable.get().lower()].keys())
        self.unit_from_box.current(0)





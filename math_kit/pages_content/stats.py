from tkinter import Frame, Label, LabelFrame, StringVar, messagebox, filedialog
from tkinter.ttk import Combobox
import csv
import statistics  
import customtkinter


class StatsPage:

       
    def __init__(self, master, tools):
    
        self.tools = tools
        self.csv_list = []
        self.columns_labels = []
        self.methods = ["Mean", "Median", "Mode", "STD", "Min", "Max"]
        
        width = int(tools.screen_width*0.8)
        height = int(tools.screen_height*0.8)
        
        self.stats_frame = customtkinter.CTkFrame(master, width=width, height=height)
        master.add(self.stats_frame)
        
        headline = """Get statistics about your data !"""
        
        self.title = customtkinter.CTkLabel(self.stats_frame, text=headline, justify="center", 
                           text_font=("Berlin Sans FB", int(tools.screen_width*0.02)))
        self.title.pack(pady=int(tools.screen_height*0.02))
        
        self.container = Frame(self.stats_frame, width=width, bg=tools.pallete["dark mode"])
        self.container.pack()
        
        self._PreparingDataLabelFrame()
        self._StatsLabelFrame()
        

    def _PreparingDataLabelFrame(self):
        
        self.preparing_data_frame = LabelFrame(self.container, bg=self.tools.pallete["dark mode"], 
                                               text="Preparing Data", fg="white")
        self.preparing_data_frame.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)
        
        self.import_button = customtkinter.CTkButton(self.preparing_data_frame, text="Import CSV", 
                        text_font=("Helvetica", 18, "bold"), cursor="hand2",  
                        command=lambda: self._ImportCSV(), hover_color=self.tools.pallete["purple"])
        
        self.select_label = customtkinter.CTkLabel(self.preparing_data_frame, text="Select the coluumn:", 
                                        text_font=("Helvetica", 18))

        self.list_variable = StringVar()
        self.list_box = Combobox(self.preparing_data_frame, textvariable=self.list_variable, state="readonly",
                                    font= ("Helvetica", 15))
        
        self.import_button.grid(row=0, column=0, columnspan=2, sticky="ew")
        
        self.select_label.grid(row=1, column=0, sticky="ew")
        self.list_box.grid(row=1, column=1, sticky="ew")        
        
        
        for child in self.preparing_data_frame.winfo_children():
            child.grid_configure(padx=15, pady=15) 
            

    def _StatsLabelFrame(self):
        
        self.stats_frame = LabelFrame(self.container, bg=self.tools.pallete["dark mode"], 
                                               text="Applying Statistics", fg="white")
        self.stats_frame.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)
        
        self.select_method_label = customtkinter.CTkLabel(self.stats_frame, text="Select the method:", 
                                        text_font=("Helvetica", 18))

        self.methods_list_variable = StringVar()
        self.methods_list_box = Combobox(self.stats_frame, textvariable=self.methods_list_variable, 
                                         state="readonly", font= ("Helvetica", 15), values=self.methods)
        self.methods_list_box.current(0)
        
        self.apply_stats_button = customtkinter.CTkButton(self.stats_frame, text="Apply", 
                        text_font=("Helvetica", 18, "bold"), cursor="hand2",  
                        command=lambda: self._ApplyStats(), hover_color=self.tools.pallete["purple"])
                
        self.result_variable = StringVar()
        self.result_entry = customtkinter.CTkEntry(self.stats_frame, text_font=("Helvetica", 18), 
                        textvariable=self.result_variable)
                
        self.select_method_label.grid(row=0, column=0, sticky="ew")
        self.methods_list_box.grid(row=0, column=1, sticky="ew")        
        self.apply_stats_button.grid(row=1, column=0, columnspan=2, sticky="ew")
        self.result_entry.grid(row=2, column=0, columnspan=2, sticky="ew")
        
        for child in self.stats_frame.winfo_children():
            child.grid_configure(padx=15, pady=15) 
             
            
    def _ImportCSV(self):
        
        filename = filedialog.askopenfilename(
            initialdir=r"C:", 
            title="Select a CSV file", 
            filetypes=(("CSV", "*.csv"), ("All", "*.*"))
        )
        
        with open(filename,"r") as csv_file:
            csv_reader = csv.DictReader(csv_file)
            
            self.columns_labels = list(next(csv_reader))
            self.list_box.config(values=self.columns_labels)
            
            self.list_box.current(0)
            
            self.csv_list = list(csv_reader)   


    def _ApplyStats(self):
        
        method = self.methods_list_box.get()
        
        x_list_items = list(self.list_box["values"])            
        if len(x_list_items) == 0:
            messagebox.showerror("Empty lists !", "The list is empty.")
            return
        
        x_list = []    
        for row in self.csv_list:
            x_list.append(row[self.list_box.get()])
    
            
        try:
            data = [float(i) for i in x_list]
        except:
            messagebox.showerror("Invalid input !", "List's elements are not numeric.")
            return
        
        
        if method == "Mean":
            result = statistics.mean(data)
            
        elif method == "Median":
            result = statistics.median(data)
            
        elif method == "Mode":
            result = statistics.mode(data)
            
        elif method == "STD":
            result = statistics.stdev(data)
            
        elif method == "Min":
            result = min(data)
            
        elif method == "Max":
            result = max(data)
            
        self.result_variable.set(result)
    
        
        
    
from tkinter import Frame, LabelFrame, Button, Label, messagebox, Entry, StringVar, filedialog
# import tkFileDialog
from tkinter.ttk import Combobox
from PIL import Image, ImageTk
import numpy as np
import matplotlib.pyplot as plt
import csv
from tkinter import Frame, Label
import threading
import os
import shutil
import customtkinter


class Plotter():
   
    def __init__(self, master, tools):        
        self.tools = tools
        
        self.columns_labels = []
        self.csv_list = []
        
        self.lower_limit = 0
        self.upper_limit = 0
        
        self.plotting = False
        
        width = int(tools.screen_width*0.8)
        height = int(tools.screen_height*0.8)
        
        self.box_background_color = tools.pallete["gray"]
        self.entries_color = tools.pallete["dark blue"]
        self.entry_text_color = tools.pallete["white"]
        self.text_color = "black"
        
        self.plotter_frame = customtkinter.CTkFrame(master, width=width, height=height)
        master.add(self.plotter_frame)
        
        headline = """Graph your data easily !"""
        
        self.title = customtkinter.CTkLabel(self.plotter_frame, text=headline, justify="center", 
                           text_font=("Berlin Sans FB", int(tools.screen_width*0.02)))
        self.title.pack(pady=int(tools.screen_height*0.02))
        
        self.container = Frame(self.plotter_frame, width=width, bg=tools.pallete["dark mode"])
        self.container.pack()
        
        self._GraphLabelFrame()
        self._PreparingDataLabelFrame()
        self._LineBarPlotLabelFrame()
        self._PolyPlotLabelFrame()
               
 
    def _ImportCSV(self):
        

        filename = filedialog.askopenfilename(
            initialdir=r"C:", 
            title="Select a CSV file", 
            filetypes=(("CSV", "*.csv"), ("All", "*.*"))
        )
        
        with open(filename,"r") as csv_file:
            csv_reader = csv.DictReader(csv_file)
            
            self.columns_labels = list(next(csv_reader))
            self.x_list_box.config(values=self.columns_labels)
            self.y_list_box.config(values=self.columns_labels)
            
            self.x_list_box.current(0)
            self.y_list_box.current(1)
            
            self.csv_list = list(csv_reader)  
              

   
    def _GraphLabelFrame(self):
        
        self.graph_frame = LabelFrame(self.container, bg=self.tools.pallete["dark mode"], 
                                      text="Graph", fg="white")
        self.graph_frame.grid(row=0, column=1, rowspan=4, sticky="nsew", padx=5, pady=5)
        
        self.graph_image_size = int(self.tools.screen_width*0.26)
        self.graph_icon = Image.open(r"../math_kit/assets/icons/splash.png")
        self.graph_icon = self.graph_icon.resize((self.graph_image_size, self.graph_image_size))
        self.graph_icon_img = ImageTk.PhotoImage(self.graph_icon)
        self.graph_img_label = customtkinter.CTkLabel(self.graph_frame, image=self.graph_icon_img)
        self.graph_img_label.image = self.graph_icon_img
        
        self.delete_graph_button = customtkinter.CTkButton(self.graph_frame, text="Clear", 
                    text_font=("Helvetica", 10, "bold"), cursor="hand2", command=lambda: self._DeleteGraph())
        
        self.save_graph_button = customtkinter.CTkButton(self.graph_frame, text="Save", 
                    text_font=("Helvetica", 10, "bold"), cursor="hand2", command=lambda: self._SaveGraph())
        
        
        self.graph_img_label.grid(row=0, column=0, columnspan=2, sticky="nsew", padx=10, pady=10)
        self.delete_graph_button.grid(row=1, column=0, sticky="ew", padx=10, pady=2)
        self.save_graph_button.grid(row=1, column=1, sticky="ew", padx=10, pady=2)
        

    def _PreparingDataLabelFrame(self):
        
        self.preparing_data_frame = LabelFrame(self.container, bg=self.tools.pallete["dark mode"], 
                                               text="Preparing Data", fg="white")
        self.preparing_data_frame.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)
        
        self.import_button = customtkinter.CTkButton(self.preparing_data_frame, text="Import CSV", 
                        text_font=("Helvetica", 18, "bold"), cursor="hand2",  
                        command=lambda: self._ImportCSV(), hover_color=self.tools.pallete["purple"])
        
        self.x_label_variable = StringVar()
        self.x_label =  customtkinter.CTkEntry(self.preparing_data_frame, text_font=("Helvetica", 18), 
                                        width=130, textvariable=self.x_label_variable)        
        self.x_label_variable.set("X-Label")
        
        self.y_label_variable = StringVar()
        self.y_label =  customtkinter.CTkEntry(self.preparing_data_frame, text_font=("Helvetica", 18), 
                                               width=130, textvariable=self.y_label_variable)        
        self.y_label_variable.set("Y-Label")
        
        self.title_label_variable = StringVar()
        self.title_label =  customtkinter.CTkEntry(self.preparing_data_frame, text_font=("Helvetica", 18),
                                            width=130, textvariable=self.title_label_variable)        
        self.title_label_variable.set("Title")
                
        self.line_label_variable = StringVar()
        self.line_label =  customtkinter.CTkEntry(self.preparing_data_frame, text_font=("Helvetica", 18), 
                                        width=130, textvariable=self.line_label_variable)        
        self.line_label_variable.set("Graph")
        
        
        self.lower_limit_label = customtkinter.CTkLabel(self.preparing_data_frame, text="Lower:", 
                                        text_font=("Helvetica", 18), bg=self.box_background_color, 
                                    fg=self.text_color)
                                    
        self.lower_limit_variable = StringVar()
        self.lower_limit_entry = customtkinter.CTkEntry(self.preparing_data_frame, text_font=("Helvetica", 18), 
                                        width=130, textvariable=self.lower_limit_variable)        
        self.lower_limit_variable.set("100")
        
        self.upper_limit_label = customtkinter.CTkLabel(self.preparing_data_frame, text="Upper:", 
                                    text_font=("Helvetica", 18), bg=self.box_background_color, 
                                    fg=self.text_color)
                
        self.upper_limit_variable = StringVar()
        self.upper_limit_entry = customtkinter.CTkEntry(self.preparing_data_frame, text_font=("Helvetica", 18), 
                                        width=130, textvariable=self.upper_limit_variable)        
        self.upper_limit_variable.set("150")

        
        self.import_button.grid(row=0, column=0, columnspan=4, sticky="ew")
        
        self.x_label.grid(row=1, column=0)
        self.y_label.grid(row=1, column=1)        
        self.title_label.grid(row=1, column=2)
        self.line_label.grid(row=1, column=3)
        
        self.lower_limit_label.grid(row=2, column=0)
        self.lower_limit_entry.grid(row=2, column=1)        
        self.upper_limit_label.grid(row=2, column=2)
        self.upper_limit_entry.grid(row=2, column=3)
        
        for child in self.preparing_data_frame.winfo_children():
            child.grid_configure(padx=5, pady=5) 
        
        
    def _LineBarPlotLabelFrame(self):
        
        self.line_plot_frame = LabelFrame(self.container, bg=self.tools.pallete["dark mode"], 
                                          text="Line Plot", fg="white")
        self.line_plot_frame.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)
        
        self.x_list_label = customtkinter.CTkLabel(self.line_plot_frame, text="X-List: ", 
                            text_font=("Helvetica", 18))
        
        self.y_list_label = customtkinter.CTkLabel(self.line_plot_frame, text="Y-List: ", 
                                                   text_font=("Helvetica", 18))
        
        self.line_bar_label = customtkinter.CTkLabel(self.line_plot_frame, text="Line/Bar: ", 
                                                text_font=("Helvetica", 18))
                
        self.x_list_variable = StringVar()
        self.x_list_box = Combobox(self.line_plot_frame, textvariable=self.x_list_variable, state="readonly",
                                    font= ("Helvetica", 15))
        
        self.y_list_variable = StringVar()
        self.y_list_box = Combobox(self.line_plot_frame, textvariable=self.y_list_variable, state="readonly",
                                    font= ("Helvetica", 15))
        
        self.line_bar_variable = StringVar()
        self.line_bar_box = Combobox(self.line_plot_frame, textvariable=self.line_bar_variable, state="readonly",
                                    font= ("Helvetica", 15), values=["Line Plot", "Bar Plot"])
        self.line_bar_box.set("Line Plot")
        
        self.line_plot_button = customtkinter.CTkButton(self.line_plot_frame, text="Plot", 
                                text_font=("Helvetica", 15, "bold"), cursor="hand2", 
                    command=lambda: self._LineBarPlotter(), hover_color=self.tools.pallete["purple"])
        
        
        self.x_list_label.grid(row=0, column=0)        
        self.x_list_box.grid(row=0, column=1)
        
        self.y_list_label.grid(row=1, column=0)
        self.y_list_box.grid(row=1, column=1)
        
        self.line_bar_label.grid(row=2, column=0)
        self.line_bar_box.grid(row=2, column=1)
                
        self.line_plot_button.grid(row=0, column=2, rowspan=3, sticky="w")
        
        for child in self.line_plot_frame.winfo_children():
            child.grid_configure(padx=5, pady=5) 

        self.line_plot_button.grid_configure(padx=35)

 
    def _PolyPlotLabelFrame(self):
        
        self.poly_plot_frame = LabelFrame(self.container, bg=self.tools.pallete["dark mode"], 
                                          text="Polynomial Plot", fg="white")
        self.poly_plot_frame.grid(row=2, column=0, sticky="nsew", padx=5, pady=5)
        
        self.poly_variable = StringVar()
        self.poly_entry =  customtkinter.CTkEntry(self.poly_plot_frame, text_font=("Helvetica", 18), 
                                        textvariable=self.poly_variable, width=110)        
        # self.poly_variable.set("Coeficients")
        self.poly_variable.set("2 5 20")
        
        info_image_size = int(self.tools.screen_width*0.02)
        self.info_icon = Image.open(r"../math_kit/assets/icons/info.png")
        self.info_icon = self.info_icon.resize((info_image_size, info_image_size))
        self.info_icon_img = ImageTk.PhotoImage(self.info_icon)
        self.info_img_button = customtkinter.CTkButton(self.poly_plot_frame, image=self.info_icon_img, 
                                cursor="hand2", command=lambda: self._InfoIcon(), text="",
                                hover_color=self.tools.pallete["purple"], width=info_image_size, 
                                height=info_image_size)
        self.info_img_button.image = self.info_icon_img
        
        
        self.x_start_variable = StringVar()
        self.x_start = customtkinter.CTkEntry(self.poly_plot_frame, text_font=("Helvetica", 18),
                                    width=110, textvariable=self.x_start_variable)        
        # self.x_start_variable.set("X-start")
        self.x_start_variable.set("-200")
        
        self.x_step_variable = StringVar()
        self.x_step = customtkinter.CTkEntry(self.poly_plot_frame, text_font=("Helvetica", 18), 
                                    width=110, textvariable=self.x_step_variable)        
        # self.x_step_variable.set("X-step")
        self.x_step_variable.set("1")
        
        self.x_end_variable = StringVar()
        self.x_end = customtkinter.CTkEntry(self.poly_plot_frame, text_font=("Helvetica", 18), 
                                    width=110, textvariable=self.x_end_variable)        
        # self.x_end_variable.set("X-end")
        self.x_end_variable.set("200")
        
        self.poly_plot_button = customtkinter.CTkButton(self.poly_plot_frame, text="Plot", 
                    text_font=("Helvetica", 15, "bold"), cursor="hand2", 
                    command=lambda: self._PolyPlotter(), hover_color=self.tools.pallete["purple"])


        self.poly_entry.grid(row=0, column=0, columnspan=3, sticky="ew")
        self.info_img_button.grid(row=0, column=3)
        self.poly_plot_button.grid(row=0, column=4, rowspan=2, sticky="w")

        self.x_start.grid(row=1, column=0)
        self.x_step.grid(row=1, column=1)        
        self.x_end.grid(row=1, column=2)        
                        
        for child in self.poly_plot_frame.winfo_children():
            child.grid_configure(padx=7, pady=5) 
    
    
    def _InfoIcon(self):
        self.explaination = """We have to enter coefficients of polynomial in the following form: \n4 3 -2 10
        that means:  4x^3 + 3x^2 - 2x + 10"""
        
        messagebox.showinfo("How to insert polynomial's coefficients", self.explaination)
 
        
    def _DeleteGraph(self):
        
        try: 
            os.remove("../math_kit/assets/plots/plot.png")
        except:
            pass
        
        self._ChangeGraphImage(name="icons/splash.png")
        
        
    def _SaveGraph(self):
        
        filename = filedialog.asksaveasfile(
            mode='w', 
            defaultextension=".png",
            initialdir=r"C:", 
            title="Select a directory and name the image")
            
        if filename is None:
            messagebox.showerror("Error", "Couldn't save the file !!")
            return
        
        try:
            shutil.copy(r"../math_kit/assets/plots/plot.png", filename.name) 
        except:
            messagebox.showerror("Error", "Couldn't save the file !!")
        
        
    def _ChangeGraphImage(self, name="plots/plot.png"):
        
        self.graph_icon = Image.open(r"../math_kit/assets/{name}".format(name=name))
        self.graph_icon = self.graph_icon.resize((self.graph_image_size, self.graph_image_size))
        self.graph_icon_img = ImageTk.PhotoImage(self.graph_icon)
        self.graph_img_label.config(image=self.graph_icon_img)
        self.graph_img_label.image = self.graph_icon_img
        
        
    def _LineBarPlotter(self):
        """
        will plot x set vs y set
        takes x list of integars, y list of integers , plat name as string , x axis lable as string , y axis lable as string, line_lable as string
        return plot
        """
        
        def thread():
            """
            a function that opens the url in the default browser

            Args:
                url (string): url to be opened
            """
            
            self.plotting = True
            
            try: 
                os.remove("../math_kit/assets/plots/plot.png")
            except:
                pass
            
            x_list_items, y_list_items = list(self.x_list_box["values"]), list(self.y_list_box["values"])
        
            
            if len(x_list_items) == 0 or len(y_list_items) == 0:
                messagebox.showerror("Empty lists !", "One or both of the lists are empty.")
                return

            lower_limit = self.lower_limit_variable.get()
            upper_limit = self.upper_limit_variable.get()
            
            if not lower_limit.isdigit() or not upper_limit.isdigit():
                messagebox.showerror("Invalid input !", "Upper and Lower limits must be integers.")
                return
            else: 
                lower_limit, upper_limit = int(lower_limit), int(upper_limit)
            
            x_list, y_list = [], []
            
            for row in self.csv_list:
                x_list.append(row[self.x_list_box.get()])
                y_list.append(row[self.y_list_box.get()])

            
            step = int((upper_limit-lower_limit)/15)
            tick_end = upper_limit+1
            
            plt.figure()
            
            plt.title(self.title_label.get())
            plt.xlabel(self.x_label.get())
            plt.ylabel(self.y_label.get())

            
            if (upper_limit-lower_limit)>len(x_list):
                
                messagebox.showerror("Out of range !", "Requested range larger then dataset size.")
                return

           

            

            try:
                # x_list, y_list = x_list[int(lower_limit):int(upper_limit)], y_list[int(lower_limit):int(upper_limit)]
                x_list, y_list = x_list[lower_limit:upper_limit:], y_list[lower_limit:upper_limit:]
            except:
                messagebox.showerror("Out of range !", "Upper or Lower limit is out of range.")
                return
            
            
            if self.line_bar_variable.get() == "Line Plot":
                plt.plot(x_list, y_list, label=self.line_label.get(), color="c")
            else:
                plt.bar(x_list, y_list, label=self.line_label.get(), color="c")

            plt.legend()
            plt.grid(True)
            if (upper_limit-lower_limit ) >20:
                try:
                    plt.xticks(x_list[0:int(tick_end):step],rotation=45)
                    plt.yticks(y_list[0:int(tick_end):step],rotation=0)
                except:
                    messagebox.showerror("Invalid input !!!", "Defference between the start and end must be relatively high.")
                    return 
            
                        
            plt.savefig("../math_kit/assets/plots/plot.png")

            plt.figure().clear()

            self._ChangeGraphImage()
            
            self.plotting = False


        if self.plotting:
            messagebox.showerror("Graph is being plotted !!!", "There is a plotting process currently, please wait until it is finished.")
            return 
        
        threading.Thread(target=thread, args=()).start()
        
    
    def _PolyPlotter(self):
        """
        will plot a polynomial function in the form of ax^5+bx^4+cx^3+dx^2+ex+f
        the function can auto generate the x list, in the form of x_start and x_end is the begging of and end of the list , with step between numbers
        takes a,b,c,d,e,f as integers , plot name as string , x axis lable as string , y axis lable as string,line_lable as string
        """
        
        def thread():
            """
            a function that opens the url in the default browser

            Args:
                url (string): url to be opened
            """
            
            self.plotting = True
            
            poly_list = list(self.poly_entry.get().strip().split(" "))
            
            try:
                poly_list = [int(i) for i in poly_list]
            except:
                messagebox.showerror("Invalid input !", "You have entered bad poly coefficients, click the info button to see how can you enter them correctly.")
                return
         
            
            lower_limit = self.lower_limit_variable.get()
            upper_limit = self.upper_limit_variable.get()
            
            if not lower_limit.isdigit() or not upper_limit.isdigit():
                messagebox.showerror("Invalid input !", "Upper and Lower limits must be integers.")
                return
            else: 
                lower_limit, upper_limit = int(lower_limit), int(upper_limit)
            
        
            x_start = self.x_start_variable.get()
            x_end = self.x_end_variable.get()
            x_step = self.x_step_variable.get()
            
            # if not x_start.isdigit() or not x_end.isdigit() or not x_step.isdigit():
            #     messagebox.showerror("Invalid input !", "Start, End, and Step points for X must be numbers.")
            #     return
            
            x_start, x_end, x_step = int(x_start), int(x_end), int(x_step)
            
            x_list = np.arange(x_start, x_end+x_step, x_step)
            
            poly = np.poly1d(poly_list)
            
            y_list = [poly(i) for i in x_list]
            
            
            plt.figure()
            
            plt.title(self.title_label.get())
            plt.xlabel(self.x_label.get())
            plt.ylabel(self.y_label.get())
            
            plt.plot(x_list, y_list, label=self.line_label.get(), color="c")
            plt.legend()
            plt.grid(True)
            plt.savefig("../math_kit/assets/plots/plot.png")
            
            plt.figure().clear()
            
            self._ChangeGraphImage()

            self.plotting = False


        if self.plotting:
            messagebox.showerror("Graph is being plotted !!!", "There is a plotting process currently, please wait until it is finished.")
            return 
        
        threading.Thread(target=thread, args=()).start()
        
    
from tkinter import Frame, LabelFrame, Button, Label, messagebox, Entry, StringVar
from tkinter.ttk import Combobox
from PIL import Image, ImageTk
import numpy as np
import matplotlib.pyplot as plt
import csv
from tkinter import Frame, Label


class Plotter():
   
    def __init__(self, master, tools):        
        self.tools = tools
        
        self.columns_labels = []
        
        width = int(tools.screen_width*0.8)
        height = int(tools.screen_height*0.8)
        
        self.box_background_color = tools.pallete["gray"]
        self.entries_color = tools.pallete["dark blue"]
        self.entry_text_color = tools.pallete["white"]
        self.text_color = "black"
        
        self.plotter_frame = Frame(master, width=width, height=height, bg=tools.pallete["gray"])
        master.add(self.plotter_frame)
        
        headline = """Graph your data easily !"""
        
        self.title = Label(self.plotter_frame, text=headline, justify="center", bg=tools.pallete["gray"], 
                           fg=tools.pallete["purple"], font=("Berlin Sans FB", int(tools.screen_width*0.02)))
        self.title.pack(pady=int(tools.screen_height*0.02))
        
        self.container = Frame(self.plotter_frame, width=width, bg=tools.pallete["gray"])
        self.container.pack()
        
        self._GraphLabelFrame()
        self._PreparingDataLabelFrame()
        self._LineBarPlotLabelFrame()
        self._PolyPlotLabelFrame()
               
        
        
    def _GraphLabelFrame(self):
        
        self.graph_frame = LabelFrame(self.container, bg=self.tools.pallete["gray"], text="Graph")
        self.graph_frame.grid(row=0, column=1, rowspan=4, sticky="nsew", padx=5, pady=5)
        
        self.graph_image_size = int(self.tools.screen_width*0.28)
        self.graph_icon = Image.open(r"../math_kit/assets/icons/splash.png")
        self.graph_icon = self.graph_icon.resize((self.graph_image_size, self.graph_image_size))
        self.graph_icon_img = ImageTk.PhotoImage(self.graph_icon)
        self.graph_img_label = Label(self.graph_frame, image=self.graph_icon_img, bg=self.tools.pallete["white"])
        self.graph_img_label.image = self.graph_icon_img
        
        self.graph_img_label.grid(row=0, column=0, sticky="nsew")
        
        
    def _PreparingDataLabelFrame(self):
        
        self.preparing_data_frame = LabelFrame(self.container, bg=self.tools.pallete["gray"], text="Preparing Data")
        self.preparing_data_frame.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)
        
        self.import_button = Button(self.preparing_data_frame, text="Import CSV", font=("Helvetica", 18, "bold"), 
                                      bg=self.tools.pallete["blue"], fg=self.tools.pallete["white"],
                                      activebackground=self.tools.pallete["purple"], cursor="hand2",
                                      command=lambda: self._ImportCSV())
        
        self.x_label_variable = StringVar()
        self.x_label =  Entry(self.preparing_data_frame, font=("Helvetica", 18), bg=self.entries_color,
                               fg=self.entry_text_color, width=7, textvariable=self.x_label_variable)        
        self.x_label_variable.set("X-Label")
        
        self.y_label_variable = StringVar()
        self.y_label =  Entry(self.preparing_data_frame, font=("Helvetica", 18), bg=self.entries_color,
                               fg=self.entry_text_color, width=7, textvariable=self.y_label_variable)        
        self.y_label_variable.set("Y-Label")
        
        self.title_label_variable = StringVar()
        self.title_label =  Entry(self.preparing_data_frame, font=("Helvetica", 18), bg=self.entries_color,
                               fg=self.entry_text_color, width=7, textvariable=self.title_label_variable)        
        self.title_label_variable.set("Title")
                
        self.line_label_variable = StringVar()
        self.line_label =  Entry(self.preparing_data_frame, font=("Helvetica", 18), bg=self.entries_color,
                               fg=self.entry_text_color, width=7, textvariable=self.line_label_variable)        
        self.line_label_variable.set("Graph")

        
        self.import_button.grid(row=0, column=0, columnspan=4, sticky="ew")
        
        self.x_label.grid(row=1, column=0)
        self.y_label.grid(row=1, column=1)        
        self.title_label.grid(row=1, column=2)
        self.line_label.grid(row=1, column=3)
        
        
        for child in self.preparing_data_frame.winfo_children():
            child.grid_configure(padx=5, pady=5) 
        
        
    def _LineBarPlotLabelFrame(self):
        
        self.line_plot_frame = LabelFrame(self.container, bg=self.tools.pallete["gray"], text="Line Plot")
        self.line_plot_frame.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)
        
        self.x_list_label = Label(self.line_plot_frame, text="X-List: ", font=("Helvetica", 18),
                                          bg=self.box_background_color, fg=self.text_color)
        
        self.y_list_label = Label(self.line_plot_frame, text="Y-List: ", font=("Helvetica", 18),
                                          bg=self.box_background_color, fg=self.text_color)
        
        self.line_bar_label = Label(self.line_plot_frame, text="Line/Bar: ", font=("Helvetica", 18),
                                          bg=self.box_background_color, fg=self.text_color)
                
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
        
        self.line_plot_button = Button(self.line_plot_frame, text="Plot", font=("Helvetica", 15, "bold"), 
                    bg=self.tools.pallete["blue"], fg=self.tools.pallete["white"],
                    activebackground=self.tools.pallete["purple"], cursor="hand2", 
                    command=lambda: self._LineBarPlotter())
        
        
        self.x_list_label.grid(row=0, column=0)        
        self.x_list_box.grid(row=0, column=1)
        
        self.y_list_label.grid(row=1, column=0)
        self.y_list_box.grid(row=1, column=1)
        
        self.line_bar_label.grid(row=2, column=0)
        self.line_bar_box.grid(row=2, column=1)
                
        self.line_plot_button.grid(row=0, column=2, rowspan=3, sticky="nsew")
        
        for child in self.line_plot_frame.winfo_children():
            child.grid_configure(padx=5, pady=5) 

        
    def _PolyPlotLabelFrame(self):
        
        self.poly_plot_frame = LabelFrame(self.container, bg=self.tools.pallete["gray"], text="Polynomial Plot")
        self.poly_plot_frame.grid(row=2, column=0, sticky="nsew", padx=5, pady=5)
        
        self.poly_variable = StringVar()
        self.poly_entry =  Entry(self.poly_plot_frame, font=("Helvetica", 18), bg=self.entries_color,
                               fg=self.entry_text_color, textvariable=self.poly_variable)        
        self.poly_variable.set("Coeficients")
        # self.poly_variable.set("2 5 2")
        
        info_image_size = int(self.tools.screen_width*0.02)
        self.info_icon = Image.open(r"../math_kit/assets/icons/info.png")
        self.info_icon = self.info_icon.resize((info_image_size, info_image_size))
        self.info_icon_img = ImageTk.PhotoImage(self.info_icon)
        self.info_img_button = Button(self.poly_plot_frame, image=self.info_icon_img, 
                                      bg=self.tools.pallete["blue"], bd=1, cursor="hand2", 
                               activebackground=self.tools.pallete["purple"], 
                               command=lambda: self._InfoIcon())
        self.info_img_button.image = self.info_icon_img
        
        
        self.x_start_variable = StringVar()
        self.x_start = Entry(self.poly_plot_frame, font=("Helvetica", 18), bg=self.entries_color,
                               fg=self.entry_text_color, width=7, textvariable=self.x_start_variable)        
        self.x_start_variable.set("X-start")
        # self.x_start_variable.set("0")
        
        self.x_step_variable = StringVar()
        self.x_step = Entry(self.poly_plot_frame, font=("Helvetica", 18), bg=self.entries_color,
                               fg=self.entry_text_color, width=7, textvariable=self.x_step_variable)        
        self.x_step_variable.set("X-step")
        # self.x_step_variable.set("1")
        
        self.x_end_variable = StringVar()
        self.x_end = Entry(self.poly_plot_frame, font=("Helvetica", 18), bg=self.entries_color,
                               fg=self.entry_text_color, width=7, textvariable=self.x_end_variable)        
        self.x_end_variable.set("X-end")
        # self.x_end_variable.set("200")
        
        self.poly_plot_button = Button(self.poly_plot_frame, text="Plot", font=("Helvetica", 15, "bold"), 
                    bg=self.tools.pallete["blue"], fg=self.tools.pallete["white"],
                    activebackground=self.tools.pallete["purple"], cursor="hand2", 
                    command=lambda: self._PolyPlotter())


        self.poly_entry.grid(row=0, column=0, columnspan=3, sticky="ew")
        self.info_img_button.grid(row=0, column=3)
        self.poly_plot_button.grid(row=0, column=4, rowspan=2, sticky="nsew")

        self.x_start.grid(row=1, column=0)
        self.x_step.grid(row=1, column=1)        
        self.x_end.grid(row=1, column=2)        
                        
        for child in self.poly_plot_frame.winfo_children():
            child.grid_configure(padx=7, pady=5) 
    
    
    
    def _InfoIcon(self):
        self.explaination = """We have to enter coefficients of polynomial in the following form: \n4, 3, -2, 10
        that means:  4x^3 + 3x^2 - 2x + 10"""
        
        messagebox.showinfo("How to insert polynomial's coefficients", self.explaination)
        
        
    def _ImportCSV(self):
        
        path = r"../math_kit/assets/csv/gold.csv"
        
        with open(path,"r") as csv_file:
            csv_reader = csv.DictReader(csv_file)
            
            self.columns_labels = list(next(csv_reader))
            self.x_list_box.config(values=self.columns_labels)
            self.y_list_box.config(values=self.columns_labels)
            
            csv_list = list(csv_reader)     
            
        
        # x_axis=[]
        # y_axis=[]
        
        # for row in csv_list:
        #    x_axis.append(row[x_axis_attr])
        #    y_axis.append(row[y_axis_attr])
        
        
    def _ChangeGraphImage(self):
        
        self.graph_icon = Image.open(r"../math_kit/assets/icons/plot.png")
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
        
        x_list, y_list = list(self.x_list_variable.get()), list(self.y_list_variable.get())
        
        if len(x_list) == 0 or len(y_list) == 0:
            messagebox.showerror("Empty lists !", "One or both of the lists are empty.")
            return
        
        plt.title(self.title_label.get())
        plt.xlabel(self.x_label.get())
        plt.ylabel(self.y_label.get())

        if self.line_bar_variable.get() == "Line Plot":
            plt.plot(x_list, y_list, label=self.line_label.get(), color="c")
        else:
            plt.bar(x_list, y_list, label=self.line_label.get(), color="c")

        plt.legend()
        plt.grid(True)
        plt.savefig("./math_kit/assets/plots/plot.png")

        self._ChangeGraphImage()
            
    
    def _PolyPlotter(self):
        """
        will plot a polynomial function in the form of ax^5+bx^4+cx^3+dx^2+ex+f
        the function can auto generate the x list, in the form of x_start and x_end is the begging of and end of the list , with step between numbers
        takes a,b,c,d,e,f as integers , plot name as string , x axis lable as string , y axis lable as string,line_lable as string
        """
        
        poly_list = list(self.poly_entry.get().strip().split(" "))
        
        try:
            poly_list = [int(i) for i in poly_list]
        except:
            messagebox.showerror("Invalid input !", ".")
            return
        
        
        x_start = self.x_start_variable.get()
        x_end = self.x_end_variable.get()
        x_step = self.x_step_variable.get()
        
        if not x_start.isdigit() or not x_end.isdigit() or not x_step.isdigit():
            messagebox.showerror("Invalid input !", "Start, End, and Step points for X must be numbers.")
            return
        
        # try:
        x_start, x_end, x_step = int(x_start), int(x_end), int(x_step)
        
        x_list = np.arange(x_start, x_end+x_step, x_step)
        
        poly = np.poly1d(poly_list)
        print(poly)
        
        y_list = [poly(i) for i in range(len(x_list))]
        
        plt.title(self.title_label.get())
        plt.xlabel(self.x_label.get())
        plt.ylabel(self.y_label.get())
        
        plt.plot(x_list, y_list, label=self.line_label.get(), color="c")
        plt.legend()
        plt.grid(True)
        plt.savefig("./math_kit/assets/plots/plot.png")
        
        self._ChangeGraphImage()

        # except:
        #     messagebox.showerror("Invalid input !", "You have entered bad poly coefficients, click the info button to see how can you enter them correctly.")
            
        
        
        
        
        
        # x_list= np.arange(x_start,x_end+step,step)
        # def _funx(x):
        #     return a*x**5+b*x**4+c*x**3+d*x**2+e*x+f
        # y_list=_funx(x_list)
        # plt.title(plt_name)
        # plt.xlabel(x_lable)
        # plt.ylabel(y_lable)
        # plt.plot(x_list,y_list, label=line_lable, color="c")
        # plt.legend()
        # plt.grid(True)
        # if save:
        #     plt.savefig("./math_kit/assets/plots/plot.png")

        # plt.show()




    # def bar_plotter(self, x_list, y_list, plt_name= None, x_lable= None ,y_lable= None, line_lable=None, save=False):
    #     plt.title(plt_name)
    #     plt.xlabel(x_lable)
    #     plt.ylabel(y_lable)

    #     plt.bar(x_list,y_list, label=line_lable, color="c")
    #     plt.legend()
    #     plt.grid(True)
    #     if save:
    #         plt.savefig("./math_kit/assets/plots/plot.png")
    #     plt.show()
        
    def plot_csv(self, path ,x_axis_attr,y_axis_attr,start=0,end=None, plt_name= None, x_lable= None ,y_lable= None, line_lable=None):
        """
        will read a csv file and plot one column in the x-axis vs another column in the y-axis,
        takes the path of the file , the name of the column to be used in the x-axis, the name of the colmun to be used in the y-axis, 
        a starting row and end row as numbers , plot name as string , x axis lable as string , y axis lable as string,line_lable as string
        """
        with open(path,"r") as csv_file:
            csv_reader = csv.DictReader(csv_file)
            row=next(csv_reader)
            csv_list=list(csv_reader)
        

        print(row)
        
        x_axis=[]
        y_axis=[]
        

        for row in csv_list:
           x_axis.append(row[x_axis_attr])
           y_axis.append(row[y_axis_attr])
        
        step=int((end-start)/15)
        tick_end=end+1
 
        plt.legend()
        plt.grid(True)

        plt.title(plt_name)
        plt.xlabel(x_lable)
        plt.ylabel(y_lable)
        plt.plot(x_axis[start:end:],y_axis[start:end:], label=line_lable)
        
        plt.xticks(x_axis[0:int(tick_end):step],rotation=90)
        plt.yticks(y_axis[0:int(tick_end):step],rotation=0)
        
        plt.show()
        


        




if __name__== "__main__": 

    """
    p3=Plotter()
    path=r"math_kit\assets\csv\gold.csv"
    x_axis_attr="Date"
    y_axis_attr="Close"
    p3.plot_csv(path,x_axis_attr,y_axis_attr,0,150,"xy","x","y")
    
    
    """


    """
    path=r"math_kit\assets\csv\gold.csv"
    x_axis_attr="Date"
    y_axis_attr="Close"
    
    with open(r"math_kit\assets\csv\gold.csv","r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        row=next(csv_reader)
        csvlist=list(csv_reader)
        

        print(row)
        
        x_axis=[]
        y_axis=[]
        for row in csvlist:
           x_axis.append(row["Date"])
           y_axis.append(row["Close"])
        

 
        plt.legend()


        plt.title("example")
        plt.xlabel("x lable")
        plt.ylabel("y lable")
        plt.plot(x_axis[0:150:],y_axis[0:150:], label="testing")
        plt.xticks(x_axis[0:151:10],rotation=90)
        plt.yticks(y_axis[0:151:10],rotation=0)
        plt.grid(True)
        plt.show()
"""
            

"""
        for row in csv_reader:
            language_count.update(row['LanguagesWorkedWith'].split(";"))
    languages =[]
    pop=[]
    for item in language_count.most_common(15):
        languages.append(item[0])
        pop.append(item[1])

    print(language_count.most_common(15))   
    print(languages)
    print(pop) 
    plt.legend()


    plt.title("example")
    plt.xlabel("x lable")
    plt.ylabel("y lable")
    plt.bar(languages,pop, label="testing")
    plt.show()

"""





""" p1=Plotter()
    x=[1,4,7,10]
    y=[13,25,100,33]
    p1.line_plotter(x,y,"test", "testing x", "testing y","testline")
"""
                                                                

  

  
    


"""    
    p2=Plotter()
    p2.function_plotter(0,0,3,1,5,0,"func test", "funx","funy","funlable",-100,100,1)
"""
    


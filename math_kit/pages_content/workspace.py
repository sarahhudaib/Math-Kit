from tkinter import Tk, Frame, Button, Label, messagebox
from PIL import Image, ImageDraw, ImageFilter, ImageTk

class WorkspacePage:
    """
    This class is the workspace page of the application. It contains the following:
    - A title label that displays the name of the application   (Label)
    - A label that displays the info of the application         (Label)
    - A label that displays the guide of the application        (Label)
    """
    
    def __init__(self, master, tools, mainWind):
        self.tools = tools
        self.notebook = master
        self.wind = mainWind
        
        self.width = int(tools.screen_width*0.8)
        self.height = int(tools.screen_height*0.8)
        
        self.workspace_frame = Frame(master, width=self.width, height=self.height, bg=tools.pallete["gray"])
        master.add(self.workspace_frame)
        
        self.padx, self.pady, self.ipadx, self.ipady = 20, 20, 10, 10
        self.avatar_side_lemgth, self.bd = int(self.width*0.14), 5
        self.bg, self.active_bg = tools.pallete["blue"], tools.pallete["purple"]
        
        self._Calc()
        self._Convertor()
        self._DiffAndInt()
        self._Numeric()
        self._Plot()
        self._Random()
        self._Stats()
        
    
    def _Calc(self):
        self.calc_frame = Frame(self.workspace_frame, bg=self.tools.pallete["gray"])
        self.calc_frame.grid(row=0, column=0, padx=self.padx, pady=self.pady, ipadx=self.ipadx, ipady=self.ipady)
        self.calc_frame.grid_columnconfigure(0, weight=1)
     
        self.calc_icon = Image.open(r"../math_kit/assets/icons/calc.png")
        self.calc_icon = self.calc_icon.resize((self.avatar_side_lemgth, self.avatar_side_lemgth))
        self.calc_icon_img = ImageTk.PhotoImage(self.calc_icon)
        self.calc_img = Button(self.calc_frame, image=self.calc_icon_img, bg=self.bg, bd=self.bd, cursor="hand2",
                               activebackground=self.active_bg, command=lambda: self._SwitchPage("calc"))
        self.calc_img.image = self.calc_icon_img
        self.calc_img.pack(pady=5)
        
        self.calc_label = Label(self.calc_frame, text="Calculator", bg=self.tools.pallete["gray"], 
                                font= ("Helvetica", 15, "bold"))
        self.calc_label.pack()
        
     
    def _Plot(self):
        self.plot_frame = Frame(self.workspace_frame, bg=self.tools.pallete["gray"])
        self.plot_frame.grid(row=0, column=1, padx=self.padx, pady=self.pady, ipadx=self.ipadx, ipady=self.ipady)
        self.plot_frame.grid_columnconfigure(0, weight=1)   

        self.plot_icon = Image.open(r"../math_kit/assets/icons/plot.png")
        self.plot_icon = self.plot_icon.resize((self.avatar_side_lemgth, self.avatar_side_lemgth))
        self.plot_icon_img = ImageTk.PhotoImage(self.plot_icon)
        self.plot_img = Button(self.plot_frame, image=self.plot_icon_img, bg=self.bg, bd=self.bd, cursor="hand2",
                               activebackground=self.active_bg, command=lambda: self._SwitchPage("plot"))
        self.plot_img.image = self.plot_icon_img
        self.plot_img.grid(row=0, column=1, padx=self.padx, pady=self.pady, ipadx=self.ipadx, ipady=self.ipady)
        self.plot_img.grid_columnconfigure(0, weight=1)
        self.plot_img.pack(pady=5)
        
        self.plot_label = Label(self.plot_frame, text="Plotter", bg=self.tools.pallete["gray"], 
                                font= ("Helvetica", 15, "bold"))
        self.plot_label.pack()  


    def _Convertor(self):
        self.convertor_frame = Frame(self.workspace_frame, bg=self.tools.pallete["gray"])
        self.convertor_frame.grid(row=0, column=2, padx=self.padx, pady=self.pady, ipadx=self.ipadx, ipady=self.ipady)
        self.convertor_frame.grid_columnconfigure(0, weight=1)
        
        self.convertor_icon = Image.open(r"../math_kit/assets/icons/convert.png")
        self.convertor_icon = self.convertor_icon.resize((self.avatar_side_lemgth, self.avatar_side_lemgth))
        self.convertor_icon_img = ImageTk.PhotoImage(self.convertor_icon)
        self.convertor_img = Button(self.convertor_frame, image=self.convertor_icon_img, bg=self.bg, bd=self.bd, 
                                    cursor="hand2", activebackground=self.active_bg, 
                                    command=lambda: self._SwitchPage("conv"))
        self.convertor_img.image = self.convertor_icon_img
        self.convertor_img.grid(row=0, column=2, padx=self.padx, pady=self.pady, ipadx=self.ipadx, ipady=self.ipady)
        self.convertor_img.grid_columnconfigure(0, weight=1)
        self.convertor_img.pack(pady=5)
        
        self.convertor_label = Label(self.convertor_frame, text="Convertor", bg=self.tools.pallete["gray"], 
                                font= ("Helvetica", 15, "bold"))
        self.convertor_label.pack()
        
    
    def _Random(self):
        self.random_frame = Frame(self.workspace_frame, bg=self.tools.pallete["gray"])
        self.random_frame.grid(row=0, column=3, padx=self.padx, pady=self.pady, ipadx=self.ipadx, ipady=self.ipady)
        self.random_frame.grid_columnconfigure(0, weight=1)
        
        self.random_icon = Image.open(r"../math_kit/assets/icons/random.png")
        self.random_icon = self.random_icon.resize((self.avatar_side_lemgth, self.avatar_side_lemgth))
        self.random_icon_img = ImageTk.PhotoImage(self.random_icon)
        self.random_img = Button(self.random_frame, image=self.random_icon_img, bg=self.bg, bd=self.bd, cursor="hand2",
                               activebackground=self.active_bg, command=lambda: self._SwitchPage("rand"))
        self.random_img.image = self.random_icon_img
        self.random_img.grid(row=0, column=3, padx=self.padx, pady=self.pady, ipadx=self.ipadx, ipady=self.ipady)
        self.random_img.grid_columnconfigure(0, weight=1)
        self.random_img.pack(pady=5)
        
        self.random_label = Label(self.random_frame, text="Randomizer", bg=self.tools.pallete["gray"], 
                                font= ("Helvetica", 15, "bold"))
        self.random_label.pack()
        
        
    def _Stats(self):
        self.stats_frame = Frame(self.workspace_frame, bg=self.tools.pallete["gray"])
        self.stats_frame.grid(row=1, column=0, padx=self.padx, pady=self.pady, ipadx=self.ipadx, ipady=self.ipady)
        self.stats_frame.grid_columnconfigure(0, weight=1)
        
        self.stats_icon = Image.open(r"../math_kit/assets/icons/stats.png")
        self.stats_icon = self.stats_icon.resize((self.avatar_side_lemgth, self.avatar_side_lemgth))
        self.stats_icon_img = ImageTk.PhotoImage(self.stats_icon)
        self.stats_img = Button(self.stats_frame, image=self.stats_icon_img, bg=self.bg, bd=self.bd, cursor="hand2",
                               activebackground=self.active_bg, command=lambda: self._SwitchPage("stat"))
        self.stats_img.image = self.stats_icon_img
        self.stats_img.pack(pady=5)
        
        self.stats_label = Label(self.stats_frame, text="Statistics", bg=self.tools.pallete["gray"], 
                                font= ("Helvetica", 15, "bold"))
        self.stats_label.pack()
        
        
    def _DiffAndInt(self):
        self.diff_and_int_frame = Frame(self.workspace_frame, bg=self.tools.pallete["gray"])
        self.diff_and_int_frame.grid(row=1, column=1, padx=self.padx, pady=self.pady, ipadx=self.ipadx, ipady=self.ipady)
        self.diff_and_int_frame.grid_columnconfigure(0, weight=1)
        
        self.diff_and_int_icon = Image.open(r"../math_kit/assets/icons/diff.png")
        self.diff_and_int_icon = self.diff_and_int_icon.resize((self.avatar_side_lemgth, self.avatar_side_lemgth))
        self.diff_and_int_icon_img = ImageTk.PhotoImage(self.diff_and_int_icon)
        self.diff_and_int_img = Button(self.diff_and_int_frame, image=self.diff_and_int_icon_img, bg=self.bg, 
                                       bd=self.bd, activebackground=self.active_bg, cursor="hand2", 
                                       command=lambda: self._SwitchPage("diff"))
        self.diff_and_int_img.image = self.diff_and_int_icon_img
        self.diff_and_int_img.grid(row=1, column=1, padx=self.padx, pady=self.pady, ipadx=self.ipadx, ipady=self.ipady)
        self.diff_and_int_img.grid_columnconfigure(0, weight=1)
        self.diff_and_int_img.pack(pady=5)
        
        self.diff_and_int_label = Label(self.diff_and_int_frame, text="Calculas", bg=self.tools.pallete["gray"], 
                                font= ("Helvetica", 15, "bold"))
        self.diff_and_int_label.pack()
        
        
    def _Numeric(self):
        self.numeric_frame = Frame(self.workspace_frame, bg=self.tools.pallete["gray"])
        self.numeric_frame.grid(row=1, column=2, padx=self.padx, pady=self.pady, ipadx=self.ipadx, ipady=self.ipady)
        self.numeric_frame.grid_columnconfigure(0, weight=1)

        self.numeric_icon = Image.open(r"../math_kit/assets/icons/numeric.png")
        self.numeric_icon = self.numeric_icon.resize((self.avatar_side_lemgth, self.avatar_side_lemgth))
        self.numeric_icon_img = ImageTk.PhotoImage(self.numeric_icon)
        self.numeric_img = Button(self.numeric_frame, image=self.numeric_icon_img, bg=self.bg, bd=self.bd, 
                                  cursor="hand2", activebackground=self.active_bg,
                                  command=lambda: self._SwitchPage("num"))
        self.numeric_img.image = self.numeric_icon_img
        self.numeric_img.grid(row=1, column=2, padx=self.padx, pady=self.pady, ipadx=self.ipadx, ipady=self.ipady)
        self.numeric_img.grid_columnconfigure(0, weight=1)
        self.numeric_img.pack(pady=5)
        
        self.numeric_label = Label(self.numeric_frame, text="Numerical", bg=self.tools.pallete["gray"], 
                                font= ("Helvetica", 15, "bold"))
        self.numeric_label.pack()


    def _SwitchPage(self, page_name):
        """
        """
        
        self.tools.PlayAudio("card_click.wav")
        
        if page_name == "calc": page_number = 4
        elif page_name == "plot": page_number = 5
        elif page_name == "conv": page_number = 10
        elif page_name == "rand": page_number = 9
        elif page_name == "stat": page_number = 8
        elif page_name == "diff": page_number = 7
        elif page_name == "num": page_number = 6
        
        
        tools = self.tools
        tools.Navigate(self.wind, self.notebook, page_number)
        
    
        
        
    
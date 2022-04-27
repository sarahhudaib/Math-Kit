from tkinter import Frame, StringVar
from math import *
import customtkinter


class ScientificCalculatorPage:
    """
    This class is used to create the scientific calculator workspace page.
    It has the following methods:
        - __init__(): This method is used to initialize the GUI of the workspace as a whole.
        - _UpperFrame(): This method is used to create the GUI for the upper frame of the workspace.
        - _LowerFrame(): This method is used to create the GUI for the lower frame of the workspace.
        - pressFunc(): This method is used to define the buttons pressed.
        - backsp(): This method is used to delete the last character.
        - equalFunc(): This method is used to evaluate the expression.
        - clearFunc(): This method is used to clear the expression.
    """
    
    def __init__(self, master, tools):
        """
        This method is used to initialize the GUI of the workspace as a whole.
        """
        self.master = master
        self.tools = tools
        
        self.expression = " "
        
        width = int(tools.screen_width*0.8)
        height = int(tools.screen_height*0.8)
        
        self.scy_calc_frame = customtkinter.CTkFrame(master, width=width, height=height,  bg=tools.pallete["dark mode"])
        master.add(self.scy_calc_frame)
        
        self.expression = ""
        
        headline = """Everybody needs a calculator at some point!"""
        
        self.title = customtkinter.CTkLabel(self.scy_calc_frame, text=headline, justify="center",
                           text_font=("Berlin Sans FB", int(tools.screen_width*0.02)))
        self.title.pack(pady=int(tools.screen_height*0.02))
        
        self.container = Frame(self.scy_calc_frame, bg=tools.pallete["dark mode"])
        self.container.pack(pady=20)
        
        self._UpperFrame()
        self._LowerFrame()


    def _UpperFrame(self):
        """
        This method is used to create the GUI for the upper frame of the workspace.
        """
        
        self.equation = StringVar()
        self.expression_field = customtkinter.CTkEntry(self.container, textvariable=self.equation, 
                                      justify='left', text_font=('courier', 20, 'bold'), 
                                      bg_color=self.tools.pallete["dark mode"], state="readonly",
                                      text_color=self.tools.pallete["dark mode"])
        self.expression_field.grid(row=0, column=0, columnspan=12, sticky='nsew')
        self.expression_field.columnconfigure(0, weight=1)
        
        self.expression_field.bind('<Return>', lambda event: self.equalFunc())
        
        


    def pressFunc(self, key):
        """Function to define the buttons pressed"""
        
        self.expression = self.expression + str(key)
        self.equation.set(self.expression)

        self.tools.PlayAudio("card_click.wav")


    def backsp(self):
        """Function to delete the last character"""
        
        text = self.expression[:-1]
        self.expression = text
        self.equation.set(text)

        self.tools.PlayAudio("card_click.wav")

        
    def equalFunc(self):
        """Function to evaluate the expression"""

        try:
            result = str(eval(self.expression))
            self.equation.set(result)
            self.expression = ""
            self.tools.PlayAudio("card_click.wav")
            
        except:
            self.equation.set("Math Error!!")
            
        

    def clearFunc(self):
        """Function to clear the expression"""
        
        self.expression = ""
        self.equation.set('0')
        
        self.tools.PlayAudio("card_click.wav")

        
    def _LowerFrame(self):
        """
        This method is used to create the GUI for the lower frame of the workspace.
        """
        
        side_length = 60
        font_size = 15
        background_color = self.tools.pallete["dark mode"]
        
        # First Row
        # button 1

        btn1 = customtkinter.CTkButton(
            self.container,
            text="1",
            bg_color=background_color,
            fg_color="white",
            text_color="black",
            text_font=("Berlin Sans FB", font_size),
            width=side_length,
            height=side_length,
            command=lambda: self.pressFunc(1),
            cursor="hand2"
        )

        # button 2
        btn2 = customtkinter.CTkButton(
            self.container,
            text="2",
            bg_color=background_color,
            fg_color="white",
            text_color="black",
            text_font=("Berlin Sans FB", font_size),
            width=side_length,
            height=side_length,
            command=lambda: self.pressFunc(2),
            cursor="hand2"
        )

        # button 3
        btn3 = customtkinter.CTkButton(
            self.container,
            text="3",
            bg_color=background_color,
            fg_color="white",
            text_color="black",
            text_font=("Berlin Sans FB", font_size),
            width=side_length,
            height=side_length,
            command=lambda: self.pressFunc(3),
            cursor="hand2"
        )
        # addition button
        addition = customtkinter.CTkButton(
            self.container,
            text="+",
            bg_color=background_color,
            fg_color="#3D4856",
            text_color="white",
            text_font=("Berlin Sans FB", font_size),
            width=side_length,
            height=side_length,
            command=lambda: self.pressFunc("+"),
            cursor="hand2"
        )

        # Second row
        # button 4
        btn4 = customtkinter.CTkButton(
            self.container,
            text="4",
            bg_color=background_color,
            fg_color="white",
            text_color="black",
            text_font=("Berlin Sans FB", font_size),
            width=side_length,
            height=side_length,
            command=lambda: self.pressFunc(4),
            cursor="hand2"
        )

        # button 5
        btn5 = customtkinter.CTkButton(
            self.container,
            text="5",
            bg_color=background_color,
            fg_color="white",
            text_color="black",
            text_font=("Berlin Sans FB", font_size),
            width=side_length,
            height=side_length,
            command=lambda: self.pressFunc(5),
            cursor="hand2"
        )

        # button 6
        btn6 = customtkinter.CTkButton(
            self.container,
            text="6",
            bg_color=background_color,
            fg_color="white",
            text_color="black",
            text_font=("Berlin Sans FB", font_size),
            width=side_length,
            height=side_length,
            command=lambda: self.pressFunc(6),
            cursor="hand2"
        )

        # subtract button
        subtract = customtkinter.CTkButton(
            self.container,
            text="-",
            bg_color=background_color,
            fg_color="#3D4856",
            text_color="white",
            text_font=("Berlin Sans FB", font_size),
            width=side_length,
            height=side_length,
            command=lambda: self.pressFunc("-"),
            cursor="hand2"
        )

        # Third row

        btn7 = customtkinter.CTkButton(
            self.container,
            text="7",
            bg_color=background_color,
            fg_color="white",
            text_color="black",
            text_font=("Berlin Sans FB", font_size),
            width=side_length,
            height=side_length,
            command=lambda: self.pressFunc(7),
            cursor="hand2"
        )

        # button 8
        btn8 = customtkinter.CTkButton(
            self.container,
            text="8",
            bg_color=background_color,
            fg_color="white",
            text_color="black",
            text_font=("Berlin Sans FB", font_size),
            width=side_length,
            height=side_length,
            command=lambda: self.pressFunc(8),
            cursor="hand2"
        )

        # button 9
        btn9 = customtkinter.CTkButton(
            self.container,
            text="9",
            bg_color=background_color,
            fg_color="white",
            text_color="black",
            text_font=("Berlin Sans FB", font_size),
            width=side_length,
            height=side_length,
            command=lambda: self.pressFunc(9),
            cursor="hand2"
        )

        # Multiply button
        multiply = customtkinter.CTkButton(
            self.container,
            text="*",
            bg_color=background_color,
            fg_color="#3D4856",
            text_color="white",
            text_font=("Berlin Sans FB", font_size),
            width=side_length,
            height=side_length,
            command=lambda: self.pressFunc("*"),
            cursor="hand2"
        )

        # zero button

        btn0 = customtkinter.CTkButton(
            self.container,
            text="0",
            bg_color=background_color,
            fg_color="white",
            text_color="black",
            text_font=("Berlin Sans FB", font_size),
            width=side_length,
            height=side_length,
            command=lambda: self.pressFunc(0),
            cursor="hand2"
        )
        # dot button
        dot = customtkinter.CTkButton(
            self.container,
            text=".",
            bg_color=background_color,
            fg_color="#3D4856",
            text_color="white",
            text_font=("Berlin Sans FB", font_size),
            width=side_length,
            height=side_length,
            command=lambda: self.pressFunc("."),
            cursor="hand2"
        )

        # clear button

        clear = customtkinter.CTkButton(
            self.container,
            text="Clear",
            bg_color=background_color,
            fg_color=self.tools.pallete["blue"],
            text_color="black",
            text_font=("Berlin Sans FB", font_size),
            width=side_length,
            height=side_length,
            command=lambda: self.clearFunc(),
            cursor="hand2",
            hover_color=self.tools.pallete["purple"]
        )
        

        # divide button
        divide = customtkinter.CTkButton(
            self.container,
            text="/",
            bg_color=background_color,
            fg_color="#3D4856",
            text_color="white",
            text_font=("Berlin Sans FB", font_size),
            width=side_length,
            height=side_length,
            command=lambda: self.pressFunc("/"),
            cursor="hand2"
        )

        # Equal Button
        equal = customtkinter.CTkButton(
            self.container,
            text="Enter",
            bg_color=background_color,
            fg_color=self.tools.pallete["blue"],
            text_color="black",
            text_font=("Berlin Sans FB", font_size),
            width=side_length,
            height=side_length,
            command=lambda: self.equalFunc(),
            cursor="hand2",
            hover_color=self.tools.pallete["purple"]
        )

        # sin Button
        sin_fun = customtkinter.CTkButton(
            self.container,
            text="sin()",
            bg_color=background_color,
            fg_color="#3D4856",
            text_color="white",
            text_font=("Berlin Sans FB", font_size),
            width=77,
            height=side_length,
            command=lambda: self.pressFunc("sin("),
            cursor="hand2"
        )

        # cos button
        cos_fun = customtkinter.CTkButton(
            self.container,
            text="cos()",
            bg_color=background_color,
            fg_color="#3D4856",
            text_color="white",
            text_font=("Berlin Sans FB", font_size),
            width=80,
            height=side_length,
            command=lambda: self.pressFunc("cos("),
            cursor="hand2"
        )

        # tan button
        tan = customtkinter.CTkButton(
            self.container,
            text="tan()",
            bg_color=background_color,
            fg_color="#3D4856",
            text_color="white",
            text_font=("Berlin Sans FB", font_size),
            width=84,
            height=side_length,
            command=lambda: self.pressFunc("tan("),
            cursor="hand2"
        )

        # pi button
        pibtn = customtkinter.CTkButton(
            self.container,
            text="\u03c0",
            bg_color=background_color,
            fg_color="#3D4856",
            text_color="white",
            text_font=("Berlin Sans FB", font_size),
            width=72,
            height=side_length,
            command=lambda: self.pressFunc("pi"),
            cursor="hand2"
        )

        # pi button
        sinh_btn =customtkinter.CTkButton(
            self.container,
            text="sinh()",
            bg_color=background_color,
            fg_color="#3D4856",
            text_color="white",
            text_font=("Berlin Sans FB", font_size),
            width=77,
            height=side_length,
            command=lambda: self.pressFunc("sinh("),
            cursor="hand2"
        )

        # cosh button
        cosh_btn = customtkinter.CTkButton(
            self.container,
            text="cosh()",
            bg_color=background_color,
            fg_color="#3D4856",
            text_color="white",
            text_font=("Berlin Sans FB", font_size),
            width=80,
            height=side_length,
            command=lambda: self.pressFunc("cosh("),
            cursor="hand2"
        )

        # tanh button
        tanh_btn = customtkinter.CTkButton(
            self.container,
            text="tanh()",
            bg_color=background_color,
            fg_color="#3D4856",
            text_color="white",
            text_font=("Berlin Sans FB", font_size),
            width=84,
            height=side_length,
            command=lambda: self.pressFunc("tanh("),
            cursor="hand2"
        )
        
        # modulus button
        mod = customtkinter.CTkButton(
            self.container,
            text="mod",
            bg_color=background_color,
            fg_color="#3D4856",
            text_color="white",
            text_font=("Berlin Sans FB", font_size),
            width=side_length,
            height=side_length,
            command=lambda: self.pressFunc("%("),
            cursor="hand2"
        )

        # sin inverse button
        asin_btn = customtkinter.CTkButton(
            self.container,
            text="sin\u207b" + "\u00b9",
            bg_color=background_color,
            fg_color="#3D4856",
            text_color="white",
            text_font=("Berlin Sans FB", font_size),
            width=77,
            height=side_length,
            command=lambda: self.equalFunc(),
            cursor="hand2"
        )
        
        # cos inverse button
        acos_btn = customtkinter.CTkButton(
            self.container,
            text="cos\u207b" + "\u00b9",
            bg_color=background_color,
            fg_color="#3D4856",
            text_color="white",
            text_font=("Berlin Sans FB", font_size),
            width=80,
            height=side_length,
            command=lambda: self.equalFunc(),
            cursor="hand2"
        )

        # tan inverse button
        atan_btn = customtkinter.CTkButton(
            self.container,
            text="tan\u207b" + "\u00b9",
            bg_color=background_color,
            fg_color="#3D4856",
            text_color="white",
            text_font=("Berlin Sans FB", font_size),
            width=84,
            height=side_length,
            command=lambda: self.equalFunc(),
            cursor="hand2"
        )

        # % button
        percent = customtkinter.CTkButton(
            self.container,
            text="%",
            bg_color=background_color,
            fg_color="#3D4856",
            text_color="white",
            text_font=("Berlin Sans FB", font_size),
            width=side_length,
            height=side_length,
            command=lambda: self.pressFunc("*0.01"),
            cursor="hand2"
        )

        # floor division button
        floor_div = customtkinter.CTkButton(
            self.container,
            text="//",
            bg_color=background_color,
            fg_color="#3D4856",
            text_color="white",
            text_font=("Berlin Sans FB", font_size),
            width=side_length,
            height=side_length,
            command=lambda: self.pressFunc("//"),
            cursor="hand2"
        )

        # Log to base ten button
        log_10 = customtkinter.CTkButton(
            self.container,
            text="log\u2081" + "\u2080",
            bg_color=background_color,
            fg_color="#3D4856",
            text_color="white",
            text_font=("Berlin Sans FB", font_size),
            width=side_length,
            height=side_length,
            command=lambda: self.pressFunc("log10("),
            cursor="hand2"
        )

        # log to base two button
        log_2 = customtkinter.CTkButton(
            self.container,
            text="log\u2082",
            bg_color=background_color,
            fg_color="#3D4856",
            text_color="white",
            text_font=("Berlin Sans FB", font_size),
            width=side_length,
            height=side_length,
            command=lambda: self.pressFunc("log2("),
            cursor="hand2"
        )

        # ln button
        natural_log = customtkinter.CTkButton(
            self.container,
            text="ln",
            bg_color=background_color,
            fg_color="#3D4856",
            text_color="white",
            text_font=("Berlin Sans FB", font_size),
            width=side_length,
            height=side_length,
            command=lambda: self.pressFunc("log("),
            cursor="hand2"
        )
        # expm1 button
        exp_onentm1 = customtkinter.CTkButton(
            self.container,
            text="Expm1",
            bg_color=background_color,
            fg_color="#3D4856",
            text_color="white",
            text_font=("Berlin Sans FB", font_size),
            width=side_length,
            height=side_length,
            command=lambda: self.pressFunc("expm1"),
            cursor="hand2"
        )

        # e log button
        e_x = customtkinter.CTkButton(
            self.container,
            text="e",
            bg_color=background_color,
            fg_color="#3D4856",
            text_color="white",
            text_font=("Berlin Sans FB", font_size),
            width=72,
            height=side_length,
            command=lambda: self.pressFunc("e**("),
            cursor="hand2"
        )

        # factorial ! button
        fact = customtkinter.CTkButton(
            self.container,
            text="!",
            bg_color=background_color,
            fg_color="#3D4856",
            text_color="white",
            text_font=("Berlin Sans FB", font_size),
            width=side_length,
            height=side_length,
            command=lambda: self.pressFunc("factorial("),
            cursor="hand2"
        )

        # inverse button
        inverse = customtkinter.CTkButton(
            self.container,
            text="x\u207b" + "\u00b9",
            bg_color=background_color,
            fg_color="#3D4856",
            text_color="white",
            text_font=("Berlin Sans FB", font_size),
            width=side_length,
            height=side_length,
            command=lambda: self.pressFunc("1/"),
            cursor="hand2"
        )
        
        # cube button
        cube = customtkinter.CTkButton(
            self.container,
            text="x\u00b3",
            bg_color=background_color,
            fg_color="#3D4856",
            text_color="white",
            text_font=("Berlin Sans FB", font_size),
            width=side_length,
            height=side_length,
            command=lambda: self.pressFunc("**3"),
            cursor="hand2"
        )

        # square button
        square = customtkinter.CTkButton(
            self.container,
            text="x\u00b2",
            bg_color=background_color,
            fg_color="#3D4856",
            text_color="white",
            text_font=("Berlin Sans FB", font_size),
            width=side_length,
            height=side_length,
            command=lambda: self.pressFunc("**2"),
            cursor="hand2"
        )

        # Square root button
        square_Root = customtkinter.CTkButton(
            self.container,
            text="\u00b2\u221Ax",
            bg_color=background_color,
            fg_color="#3D4856",
            text_color="white",
            text_font=("Berlin Sans FB", font_size),
            width=side_length,
            height=side_length,
            command=lambda: self.pressFunc("isqrt("),
            cursor="hand2"
        )
        
        # back_space button
        back_space = customtkinter.CTkButton(
            self.container,
            text="\u2190",
            bg_color=background_color,
            fg_color="#3D4856",
            text_color="white",
            text_font=("Berlin Sans FB", font_size),
            width=side_length,
            height=side_length,
            command=lambda: self.backsp(),
            cursor="hand2"
        )

        # power_fun button
        pow_fun = customtkinter.CTkButton(
            self.container,
            text="pow",
            bg_color=background_color,
            fg_color="#3D4856",
            text_color="white",
            text_font=("Berlin Sans FB", font_size),
            width=72,
            height=side_length,
            command=lambda: self.pressFunc("**"),
            cursor="hand2"
        )
        
        # root button
        root = customtkinter.CTkButton(
            self.container,
            text="\u207f\u221Ax",
            bg_color=background_color,
            fg_color="#3D4856",
            text_color="white",
            text_font=("Berlin Sans FB", font_size),
            width=side_length,
            height=side_length,
            command=lambda: self.pressFunc("**(1/"),
            cursor="hand2"
        )

        # ( button
        l_bracket = customtkinter.CTkButton(
            self.container,
            text="\u2772",
            bg_color=background_color,
            fg_color="#3D4856",
            text_color="white",
            text_font=("Berlin Sans FB", font_size),
            width=side_length,
            height=side_length,
            command=lambda: self.pressFunc("("),
            cursor="hand2"
        )

        # ) button
        r_bracket = customtkinter.CTkButton(
            self.container,
            text="\u2773",
            bg_color=background_color,
            fg_color="#3D4856",
            text_color="white",
            text_font=("Berlin Sans FB", font_size),
            width=side_length,
            height=side_length,
            command=lambda: self.pressFunc(")"),
            cursor="hand2"
        )

        # asinh button
        a_sinh = customtkinter.CTkButton(
            self.container,
            text="asinh()",
            bg_color=background_color,
            fg_color="#3D4856",
            text_color="white",
            text_font=("Berlin Sans FB", font_size),
            width=side_length,
            height=side_length,
            command=lambda: self.pressFunc("asinh("),
            cursor="hand2"
        )

        # acosh button
        a_cosh = customtkinter.CTkButton(
            self.container,
            text="acosh()",
            bg_color=background_color,
            fg_color="#3D4856",
            text_color="white",
            text_font=("Berlin Sans FB", font_size),
            width=side_length,
            height=side_length,
            command=lambda: self.pressFunc("acosh("),
            cursor="hand2"
        )

        # atanh button
        a_tanh = customtkinter.CTkButton(
            self.container,
            text="atanh()",
            bg_color=background_color,
            fg_color="#3D4856",
            text_color="white",
            text_font=("Berlin Sans FB", font_size),
            width=side_length,
            height=side_length,
            command=lambda: self.pressFunc("atanh("),
            cursor="hand2"
        )

        # packing the expression field
        self.expression_field.grid(row=0, column=0, columnspan=12, pady=5, padx=3, ipady=5, ipadx=18)  
        # ipadx changes the frame width

        # Positioning the button in rows
        # Row one
        btn1.grid(row=1, column=0)
        btn2.grid(row=1, column=1)
        btn3.grid(row=1, column=2)
        addition.grid(row=1, column=3)
        multiply.grid(row=1, column=4)
        floor_div.grid(row=1, column=5)
        sin_fun.grid(row=1, column=6)
        cos_fun.grid(row=1, column=7)
        tan.grid(row=1, column=8)
        square.grid(row=1, column=9)

        natural_log.grid(row=1, column=10)
        exp_onentm1.grid(row=1, column=11)

        # row two
        btn4.grid(row=2, column=0)
        btn5.grid(row=2, column=1)
        btn6.grid(row=2, column=2)
        subtract.grid(row=2, column=3)

        divide.grid(row=2, column=4)
        fact.grid(row=2, column=5)
        sinh_btn.grid(row=2, column=6)
        cosh_btn.grid(row=2, column=7)
        tanh_btn.grid(row=2, column=8)
        cube.grid(row=2, column=9)

        e_x.grid(row=2, column=11)
        log_10.grid(row=2, column=10)

        # row three
        btn7.grid(row=3, column=0)
        btn8.grid(row=3, column=1)
        btn9.grid(row=3, column=2)
        l_bracket.grid(row=3, column=3)
        r_bracket.grid(row=3, column=4)
        mod.grid(row=3, column=5)
        asin_btn.grid(row=3, column=6)
        acos_btn.grid(row=3, column=7)
        atan_btn.grid(row=3, column=8)
        inverse.grid(row=3, column=9)
        log_2.grid(row=3, column=10)
        pow_fun.grid(row=3, column=11)

        # Row Four
        equal.grid(row=4, column=0)
        btn0.grid(row=4, column=1)
        clear.grid(row=4, column=2)
        dot.grid(row=4, column=3)
        percent.grid(row=4, column=4)
        back_space.grid(row=4, column=5)
        a_sinh.grid(row=4, column=6)
        a_cosh.grid(row=4, column=7)
        a_tanh.grid(row=4, column=8)
        root.grid(row=4, column=9)
        square_Root.grid(row=4, column=10)
        pibtn.grid(row=4, column=11)

        for child in self.container.winfo_children():
            child.grid_configure(padx=2, pady=2)

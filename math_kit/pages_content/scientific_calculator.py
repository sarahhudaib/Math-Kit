from tkinter import Tk, Frame, Button, Entry, StringVar, Label
from math import tan, sin, cos, exp, log, sqrt, atan2, asin, acos, atan, degrees, radians, floor, ceil, trunc, pow, fabs

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
        
        width = int(tools.screen_width*0.8)
        height = int(tools.screen_height*0.8)
        
        self.scy_calc_frame = Frame(master, width=width, height=height, bg=tools.pallete["gray"])
        master.add(self.scy_calc_frame)
        
        self.expression = " "
        self.equation = StringVar()
        
        headline = """Everybody needs a calculator at some point!"""
        
        self.title = Label(self.scy_calc_frame, text=headline, justify="center",
                           bg=tools.pallete["gray"], fg=tools.pallete["purple"],
                           font=("Berlin Sans FB", int(tools.screen_width*0.02)))
        self.title.pack(pady=int(tools.screen_height*0.02))
        
        self.container = Frame(self.scy_calc_frame, bg=self.tools.pallete["gray"])
        self.container.pack(pady=20)
        
        self._UpperFrame()
        self._LowerFrame()


    def _UpperFrame(self):
        """
        This method is used to create the GUI for the upper frame of the workspace.
        """
        self.expression_field = Entry(self.container, textvariable=self.equation, 
                                      width=int(self.tools.screen_width*0.042),
                                justify='left', font=('courier', 20, 'bold'), bg='#D3D8DE', bd=5)
        self.expression_field.grid(row=0, column=0, columnspan=12)
        self.expression_field.columnconfigure(0, weight=1)
        
        


    def pressFunc(self, key):
        """Function to define the buttons pressed"""
        self.expression
        self.expression = self.expression + str(key)

        # to set the expression
        self.equation.set(self.expression)

    def backsp(self):
        """Function to delete the last character"""
        self.expression
        text = self.expression[:-1]
        self.expression = text
        self.equation.set(text)

        
    def equalFunc(self):
        """Function to evaluate the expression"""
        self.expression

        try:
            result = str(eval(self.expression))
            self.equation.set(result)
            # to reset
            self.expression = ""

        except:
            self.equation.set("Math Error!!")


    def clearFunc(self):
        """Function to clear the expression"""
        self.expression
        self.expression = ""
        self.equation.set("0")

        
    def _LowerFrame(self):
        """
        This method is used to create the GUI for the lower frame of the workspace.
        """
        # First Row
        # button 1

        btn1 = Button(
            self.container,
            text="1",
            bg="white",
            font=("Berlin Sans FB", 12),
            relief="raised",
            bd=1,
            width=8,
            height=3,
            command=lambda: self.pressFunc(1),
        )

        # button 2
        btn2 = Button(
            self.container,
            text="2",
            bg="white",
            font=("Berlin Sans FB", 12),
            relief="raised",
            bd=1,
            width=8,
            height=3,
            command=lambda: self.pressFunc(2),
        )

        # button 3
        btn3 = Button(
            self.container,
            text="3",
            bg="white",
            font=("Berlin Sans FB", 12),
            relief="raised",
            bd=1,
            width=8,
            height=3,
            command=lambda: self.pressFunc(3),
        )
        # addition button
        addition = Button(
            self.container,
            text="+",
            bg="#3D4856",
            font=("Berlin Sans FB", 12),
            relief="raised",
            bd=1,
            width=8,
            height=3,
            fg="white",
            command=lambda: self.pressFunc("+"),
        )

        # Second row
        # button 4
        btn4 = Button(
            self.container,
            text="4",
            bg="white",
            font=("Berlin Sans FB", 12),
            relief="raised",
            bd=1,
            width=8,
            height=3,
            command=lambda: self.pressFunc(4),
        )

        # button 5
        btn5 = Button(
            self.container,
            text="5",
            bg="white",
            font=("Berlin Sans FB", 12),
            relief="raised",
            bd=1,
            width=8,
            height=3,
            command=lambda: self.pressFunc(5),
        )

        # button 6
        btn6 = Button(
            self.container,
            text="6",
            bg="white",
            font=("Berlin Sans FB", 12),
            relief="raised",
            bd=1,
            width=8,
            height=3,
            command=lambda: self.pressFunc(6),
        )

        # subtract button
        subtract = Button(
            self.container,
            text="-",
            bg="#3D4856",
            font=("Berlin Sans FB", 12),
            relief="raised",
            bd=1,
            width=8,
            height=3,
            fg="white",
            command=lambda: self.pressFunc("-"),
        )

        # Third row

        btn7 = Button(
            self.container,
            text="7",
            bg="white",
            font=("Berlin Sans FB", 12),
            relief="raised",
            bd=1,
            width=8,
            height=3,
            command=lambda: self.pressFunc(7),
        )

        # button 8
        btn8 = Button(
            self.container,
            text="8",
            bg="white",
            font=("Berlin Sans FB", 12),
            relief="raised",
            bd=1,
            width=8,
            height=3,
            command=lambda: self.pressFunc(8),
        )

        # button 9
        btn9 = Button(
            self.container,
            text="9",
            bg="white",
            font=("Berlin Sans FB", 12),
            relief="raised",
            bd=1,
            width=8,
            height=3,
            command=lambda: self.pressFunc(9),
        )

        # Multiply button
        multiply = Button(
            self.container,
            text="*",
            bg="#3D4856",
            font=("arial", 12),
            relief="raised",
            bd=1,
            width=8,
            height=3,
            fg="white",
            command=lambda: self.pressFunc("*"),
        )

        # zero button

        btn0 = Button(
            self.container,
            text="0",
            bg="white",
            font=("Berlin Sans FB", 12),
            relief="raised",
            bd=1,
            width=8,
            height=3,
            command=lambda: self.pressFunc(0),
        )
        # dot button
        dot = Button(
            self.container,
            text=".",
            bg="#3D4856",
            font=("Berlin Sans FB", 12),
            relief="raised",
            bd=1,
            width=8,
            height=3,
            fg="white",
            command=lambda: self.pressFunc("."),
        )

        # clear button

        clear = Button(
            self.container,
            text="Clear",
            bg="#0693E3",
            fg="white",
            font=("Berlin Sans FB", 12),
            relief="raised",
            bd=1,
            width=8,
            height=3,
            command=lambda: self.clearFunc(),
        )

        # divide button
        divide = Button(
            self.container,
            text="/",
            bg="#3D4856",
            font=("arial", 12),
            relief="raised",
            bd=1,
            width=8,
            height=3,
            fg="white",
            command=lambda: self.pressFunc("/"),
        )

        # Equal Button
        equal = Button(
            self.container,
            text="Enter",
            bg="#0693E3",
            font=("arial", 12),
            relief="raised",
            bd=1,
            width=8,
            height=3,
            fg="white",
            command=lambda: self.equalFunc(),
        )

        # sin Button
        sin_fun = Button(
            self.container,
            text="sin()",
            bg="#3D4856",
            font=("arial", 12),
            relief="raised",
            bd=1,
            width=8,
            height=3,
            fg="white",
            command=lambda: self.pressFunc("sin("),
        )

        # cos button
        cos_fun = Button(
            self.container,
            text="cos()",
            bg="#3D4856",
            font=("arial", 12),
            relief="raised",
            bd=1,
            width=8,
            height=3,
            fg="white",
            command=lambda: self.pressFunc("cos("),
        )

        # tan button
        tan = Button(
            self.container,
            text="tan()",
            bg="#3D4856",
            font=("arial", 12),
            relief="raised",
            bd=1,
            width=8,
            height=3,
            fg="white",
            command=lambda: self.pressFunc("tan("),
        )

        # pi button
        pibtn = Button(
            self.container,
            text="\u03c0",
            bg="#3D4856",
            font=("arial", 12),
            relief="raised",
            bd=1,
            width=8,
            height=3,
            fg="white",
            command=lambda: self.pressFunc("pi"),
        )

        # pi button
        sinh_btn = Button(
            self.container,
            text="sinh()",
            bg="#3D4856",
            font=("arial", 12),
            relief="raised",
            bd=1,
            width=8,
            height=3,
            fg="white",
            command=lambda: self.pressFunc("sinh("),
        )

        # cosh button
        cosh_btn = Button(
            self.container,
            text="cosh()",
            bg="#3D4856",
            font=("arial", 12),
            relief="raised",
            bd=1,
            width=8,
            height=3,
            fg="white",
            command=lambda: self.pressFunc("cosh("),
        )

        # tanh button
        tanh_btn = Button(
            self.container,
            text="tanh()",
            bg="#3D4856",
            font=("arial", 12),
            relief="raised",
            bd=1,
            width=8,
            height=3,
            fg="white",
            command=lambda: self.equalFunc(),
        )

        # modulus button
        mod = Button(
            self.container,
            text="mod",
            bg="#3D4856",
            font=("arial", 12),
            relief="raised",
            bd=1,
            width=8,
            height=3,
            fg="white",
            command=lambda: self.pressFunc("%("),
        )

        # sin inverse button
        asin_btn = Button(
            self.container,
            text="sin\u207b" + "\u00b9",
            bg="#3D4856",
            font=("arial", 12),
            relief="raised",
            bd=1,
            width=8,
            height=3,
            fg="white",
            command=lambda: self.equalFunc(),
        )

        # cos inverse button
        acos_btn = Button(
            self.container,
            text="cos\u207b" + "\u00b9",
            bg="#3D4856",
            font=("arial", 12),
            relief="raised",
            bd=1,
            width=8,
            height=3,
            fg="white",
            command=lambda: self.equalFunc(),
        )

        # tan inverse button
        atan_btn = Button(
            self.container,
            text="tan\u207b" + "\u00b9",
            bg="#3D4856",
            font=("arial", 12),
            relief="raised",
            bd=1,
            width=8,
            height=3,
            fg="white",
            command=lambda: self.equalFunc(),
        )

        # % button
        percent = Button(
            self.container,
            text="%",
            bg="#3D4856",
            font=("arial", 12),
            relief="raised",
            bd=1,
            width=8,
            height=3,
            fg="white",
            command=lambda: self.pressFunc("*0.01"),
        )

        # floor division button
        floor_div = Button(
            self.container,
            text="//",
            bg="#3D4856",
            font=("arial", 12),
            relief="raised",
            bd=1,
            width=8,
            height=3,
            fg="white",
            command=lambda: self.pressFunc("//"),
        )

        # Log to base ten button
        log_10 = Button(
            self.container,
            text="log\u2081" + "\u2080",
            bg="#3D4856",
            font=("arial", 12),
            relief="raised",
            bd=1,
            width=8,
            height=3,
            fg="white",
            command=lambda: self.pressFunc("log10("),
        )

        # log to base two button
        log_2 = Button(
            self.container,
            text="log\u2082",
            bg="#3D4856",
            font=("arial", 12),
            relief="raised",
            bd=1,
            width=8,
            height=3,
            fg="white",
            command=lambda: self.pressFunc("log2("),
        )

        # ln button
        natural_log = Button(
            self.container,
            text="ln",
            bg="#3D4856",
            font=("arial", 12),
            relief="raised",
            bd=1,
            width=8,
            height=3,
            fg="white",
            command=lambda: self.pressFunc("log("),
        )
        # expm1 button
        exp_onentm1 = Button(
            self.container,
            text="Expm1",
            bg="#3D4856",
            font=("arial", 12),
            relief="raised",
            bd=1,
            width=8,
            height=3,
            fg="white",
            command=lambda: self.pressFunc("expm1("),
        )

        # e log button
        e_x = Button(
            self.container,
            text="e",
            bg="#3D4856",
            font=("arial", 12),
            relief="raised",
            bd=1,
            width=8,
            height=3,
            fg="white",
            command=lambda: self.pressFunc("e**("),
        )

        # factorial ! button
        fact = Button(
            self.container,
            text="!",
            bg="#3D4856",
            font=("arial", 12),
            relief="raised",
            bd=1,
            width=8,
            height=3,
            fg="white",
            command=lambda: self.pressFunc("factorial("),
        )

        # inverse button
        inverse = Button(
            self.container,
            text="x\u207b" + "\u00b9",
            bg="#3D4856",
            font=("arial", 12),
            relief="raised",
            bd=1,
            width=8,
            height=3,
            fg="white",
            command=lambda: self.pressFunc("1/"),
        )

        # cube button
        cube = Button(
            self.container,
            text="x\u00b3",
            bg="#3D4856",
            font=("arial", 12),
            relief="raised",
            bd=1,
            width=8,
            height=3,
            fg="white",
            command=lambda: self.pressFunc("**3"),
        )

        # square button
        square = Button(
            self.container,
            text="x\u00b2",
            bg="#3D4856",
            font=("arial", 12),
            relief="raised",
            bd=1,
            width=8,
            height=3,
            fg="white",
            command=lambda: self.pressFunc("**2"),
        )

        # Square root button
        square_Root = Button(
            self.container,
            text="\u00b2\u221Ax",
            bg="#3D4856",
            font=("arial", 12),
            relief="raised",
            bd=1,
            width=8,
            height=3,
            fg="white",
            command=lambda: self.pressFunc("isqrt("),
        )

        # back_space button
        back_space = Button(
            self.container,
            text="\u2190 Back",
            bg="#3D4856",
            font=("arial", 12),
            relief="raised",
            bd=1,
            width=8,
            height=3,
            fg="white",
            command=lambda: self.backsp(),
        )

        # power_fun button
        pow_fun = Button(
            self.container,
            text="pow",
            bg="#3D4856",
            font=("arial", 12),
            relief="raised",
            bd=1,
            width=8,
            height=3,
            fg="white",
            command=lambda: self.pressFunc("**"),
        )

        # root button
        root = Button(
            self.container,
            text="\u207f\u221Ax",
            bg="#3D4856",
            font=("arial", 12),
            relief="raised",
            bd=1,
            width=8,
            height=3,
            fg="white",
            command=lambda: self.pressFunc("**(1/"),
        )

        # ( button
        l_bracket = Button(
            self.container,
            text="\u2772",
            bg="#3D4856",
            font=("arial", 12),
            relief="raised",
            bd=1,
            width=8,
            height=3,
            fg="white",
            command=lambda: self.pressFunc("("),
        )

        # ) button
        r_bracket = Button(
            self.container,
            text="\u2773",
            bg="#3D4856",
            font=("arial", 12),
            relief="raised",
            bd=1,
            width=8,
            height=3,
            fg="white",
            command=lambda: self.pressFunc(")"),
        )

        # asinh button
        a_sinh = Button(
            self.container,
            text="asinh()",
            bg="#3D4856",
            font=("arial", 12),
            relief="raised",
            bd=1,
            width=8,
            height=3,
            fg="white",
            command=lambda: self.pressFunc("asinh("),
        )

        # acosh button
        a_cosh = Button(
            self.container,
            text="acosh()",
            bg="#3D4856",
            font=("arial", 12),
            relief="raised",
            bd=1,
            width=8,
            height=3,
            fg="white",
            command=lambda: self.pressFunc("acosh("),
        )

        # atanh button
        a_tanh = Button(
            self.container,
            text="atanh()",
            bg="#3D4856",
            font=("arial", 12),
            relief="raised",
            bd=1,
            width=8,
            height=3,
            fg="white",
            command=lambda: self.pressFunc("atanh("),
        )

        # packing the expression field
        self.expression_field.grid(
            row=0, column=0, columnspan=12, pady=5, padx=3, ipady=5, ipadx=18
        )  # ipadx changes the frame width

        # Positioning the button in rows
        # Row one
        btn1.grid(row=1, column=0)
        btn2.grid(row=1, column=1)
        btn3.grid(row=1, column=2)
        addition.grid(row=1, column=3)
        multiply.grid(row=1, column=4)
        floor_div.grid(row=1, column=5)
        sin_fun.grid(row=1, column=6)
        sinh_btn.grid(row=1, column=7)
        asin_btn.grid(row=1, column=8)
        a_sinh.grid(row=1, column=9)

        natural_log.grid(row=1, column=10)
        exp_onentm1.grid(row=1, column=11)

        # row two
        btn4.grid(row=2, column=0)
        btn5.grid(row=2, column=1)
        btn6.grid(row=2, column=2)
        subtract.grid(row=2, column=3)

        divide.grid(row=2, column=4)
        fact.grid(row=2, column=5)
        cos_fun.grid(row=2, column=6)
        cosh_btn.grid(row=2, column=7)
        acos_btn.grid(row=2, column=8)
        a_cosh.grid(row=2, column=9)

        e_x.grid(row=2, column=11)
        log_10.grid(row=2, column=10)

        # row three
        btn7.grid(row=3, column=0)
        btn8.grid(row=3, column=1)
        btn9.grid(row=3, column=2)
        l_bracket.grid(row=3, column=3)
        r_bracket.grid(row=3, column=4)
        mod.grid(row=3, column=5)
        tan.grid(row=3, column=6)
        tanh_btn.grid(row=3, column=7)
        atan_btn.grid(row=3, column=8)
        a_tanh.grid(row=3, column=9)
        log_2.grid(row=3, column=10)
        pow_fun.grid(row=3, column=11)

        # Row Four
        equal.grid(row=4, column=0)
        btn0.grid(row=4, column=1)
        clear.grid(row=4, column=2)
        dot.grid(row=4, column=3)
        percent.grid(row=4, column=4)
        back_space.grid(row=4, column=5)
        square.grid(row=4, column=6)
        cube.grid(row=4, column=7)
        inverse.grid(row=4, column=8)
        root.grid(row=4, column=9)
        square_Root.grid(row=4, column=10)
        pibtn.grid(row=4, column=11)



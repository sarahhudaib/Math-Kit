
from tkinter import Tk, Frame, Button, Entry, StringVar

from math import tan, sin, cos, exp, log, sqrt, atan2, asin, acos, atan, degrees, radians, floor, ceil, trunc, pow, fabs

expression = " "

window = Tk()

window.title("Scientific Calculator")  # set window title

window.geometry("960x325")  # set window dimensions

window.configure(bg="#D3D8DE")  # set background color

# container
frm_container = Frame(window, bg="#0693E3")
frm_container.pack()

# Entry field where we indicate expressions
equation = StringVar() 
expression_field = Entry(frm_container, textvariable=equation, width=75,
                         justify='right', font=('courier', 15, 'bold', 'italic'), bg='#D3D8DE', bd=5)


# expression_field.pack()


def pressFunc(key):
    """ Function to define the buttons pressed """
    global expression
    expression = expression + str(key)

    # to set the expression
    equation.set(expression)


def backsp():
    """ Function to delete the last character """
    global expression
    text = expression[:-1]
    expression = text
    equation.set(text)


def equalFunc():
    """ Function to evaluate the expression """
    global expression

    try:

        result = str(eval(expression))

        equation.set(result)
        # to reset
        expression = ""

    except:
        equation.set("Math Error!!")


def clearFunc():
    """ Function to clear the expression """
    global expression
    expression = ""

    equation.set('0')


# First Row
# button 1
btn1 = Button(frm_container, text="1", bg='white', font=("Berlin Sans FB", 12), relief='raised', bd=1,
              width=8, height=3, command=lambda: pressFunc(1))

# button 2
btn2 = Button(frm_container, text="2", bg='white', font=("Berlin Sans FB", 12), relief='raised', bd=1,
              width=8, height=3, command=lambda: pressFunc(2))

# button 3
btn3 = Button(frm_container, text="3", bg='white', font=("Berlin Sans FB", 12), relief='raised', bd=1,
              width=8, height=3, command=lambda: pressFunc(3))
# addition button
addition = Button(frm_container, text="+", bg='#3D4856', font=("Berlin Sans FB", 12), relief='raised', bd=1,
                  width=8, height=3, fg='white', command=lambda: pressFunc("+"))

# Second row
# button 4
btn4 = Button(frm_container, text="4", bg='white', font=("Berlin Sans FB", 12), relief='raised', bd=1,
              width=8, height=3, command=lambda: pressFunc(4))

# button 5
btn5 = Button(frm_container, text="5", bg='white', font=("Berlin Sans FB", 12), relief='raised', bd=1,
              width=8, height=3, command=lambda: pressFunc(5))

# button 6
btn6 = Button(frm_container, text="6", bg='white', font=("Berlin Sans FB", 12), relief='raised', bd=1,
              width=8, height=3, command=lambda: pressFunc(6))

# subtract button
subtract = Button(frm_container, text="-", bg='#3D4856', font=("Berlin Sans FB", 12), relief='raised', bd=1,
                  width=8, height=3, fg='white', command=lambda: pressFunc("-"))

# Third row

btn7 = Button(frm_container, text="7", bg='white', font=("Berlin Sans FB", 12), relief='raised', bd=1,
              width=8, height=3, command=lambda: pressFunc(7))

# button 8
btn8 = Button(frm_container, text="8", bg='white', font=("Berlin Sans FB", 12), relief='raised', bd=1,
              width=8, height=3, command=lambda: pressFunc(8))

# button 9
btn9 = Button(frm_container, text="9", bg='white', font=("Berlin Sans FB", 12), relief='raised', bd=1,
              width=8, height=3, command=lambda: pressFunc(9))

# Multiply button
multiply = Button(frm_container, text="*", bg='#3D4856', font=("arial", 12), relief='raised', bd=1,
                  width=8, height=3, fg='white', command=lambda: pressFunc("*"))

# zero button

btn0 = Button(frm_container, text="0", bg='white', font=("Berlin Sans FB", 12), relief='raised', bd=1,
              width=8, height=3, command=lambda: pressFunc(0))
# dot button
dot = Button(frm_container, text=".", bg='white', font=("Berlin Sans FB", 12), relief='raised', bd=1,
             width=8, height=3, command=lambda: pressFunc("."))

# clear button

clear = Button(frm_container, text="Clear", bg='white', fg='red', font=("Berlin Sans FB", 12), relief='raised', bd=1,
               width=8, height=3, command=clearFunc)

# divide button
divide = Button(frm_container, text="/", bg='#3D4856', font=("arial", 12), relief='raised', bd=1,
                width=8, height=3, fg='white', command=lambda: pressFunc("/"))

# Equal Button
equal = Button(frm_container, text="=", bg='#3D4856', font=("arial", 12), relief='raised', bd=1,
               width=8, height=3, fg='white', command=equalFunc)

# sin Button
sin_fun = Button(frm_container, text="sin", bg='#3D4856', font=("arial", 12), relief='raised', bd=1,
                 width=8, height=3, fg='white', command=lambda: pressFunc('sin('))

# cos button
cos_fun = Button(frm_container, text="cos", bg='#3D4856', font=("arial", 12), relief='raised', bd=1,
                 width=8, height=3, fg='white', command=lambda: pressFunc('cos('))

# tan button
tan = Button(frm_container, text="tan", bg='#3D4856', font=("arial", 12), relief='raised', bd=1,
             width=8, height=3, fg='white', command=lambda: pressFunc('tan('))

# pi button
pibtn = Button(frm_container, text="\u03c0", bg='#3D4856', font=("arial", 12), relief='raised', bd=1,
               width=8, height=3, fg='white', command=lambda: pressFunc("pi"))

# pi button
sinh_btn = Button(frm_container, text="sinh", bg='#3D4856', font=("arial", 12), relief='raised', bd=1,
                  width=8, height=3, fg='white', command=lambda: pressFunc('sinh('))

# cosh button
cosh_btn = Button(frm_container, text="cosh", bg='#3D4856', font=("arial", 12), relief='raised', bd=1,
                  width=8, height=3, fg='white', command=lambda: pressFunc('cosh('))

# tanh button
tanh_btn = Button(frm_container, text="tanh", bg='#3D4856', font=("arial", 12), relief='raised', bd=1,
                  width=8, height=3, fg='white', command=equalFunc)

# modulus button
mod = Button(frm_container, text="mod", bg='#3D4856', font=("arial", 12), relief='raised', bd=1,
             width=8, height=3, fg='white', command=lambda: pressFunc('%('))

# sin inverse button
asin_btn = Button(frm_container, text="sin\u207b" + "\u00b9", bg='#3D4856', font=("arial", 12), relief='raised', bd=1,
                  width=8, height=3, fg='white', command=equalFunc)

# cos inverse button
acos_btn = Button(frm_container, text="cos\u207b" + "\u00b9", bg='#3D4856', font=("arial", 12), relief='raised', bd=1,
                  width=8, height=3, fg='white', command=equalFunc)

# tan inverse button
atan_btn = Button(frm_container, text="tan\u207b" + "\u00b9", bg='#3D4856', font=("arial", 12), relief='raised', bd=1,
                  width=8, height=3, fg='white', command=equalFunc)

# % button
percent = Button(frm_container, text="%", bg='#3D4856', font=("arial", 12), relief='raised', bd=1,
                 width=8, height=3, fg='white', command=lambda: pressFunc('*0.01'))

# floor division button
floor_div = Button(frm_container, text="//", bg='#3D4856', font=("arial", 12), relief='raised', bd=1,
                   width=8, height=3, fg='white', command=lambda: pressFunc('//'))

# Log to base ten button
log_10 = Button(frm_container, text="log\u2081" + "\u2080", bg='#3D4856', font=("arial", 12), relief='raised', bd=1,
                width=8, height=3, fg='white', command=lambda: pressFunc('log10('))

# log to base two button
log_2 = Button(frm_container, text="log\u2082", bg='#3D4856', font=("arial", 12), relief='raised', bd=1,
               width=8, height=3, fg='white', command=lambda: pressFunc('log2('))

# ln button
natural_log = Button(frm_container, text="ln", bg='#3D4856', font=("arial", 12), relief='raised', bd=1,
                     width=8, height=3, fg='white', command=lambda: pressFunc('log('))
# expm1 button
exp_onentm1 = Button(frm_container, text="Expm1", bg='#3D4856', font=("arial", 12), relief='raised', bd=1,
                     width=8, height=3, fg='white', command=lambda: pressFunc('expm1('))

# e log button
e_x = Button(frm_container, text="e", bg='#3D4856', font=("arial", 12), relief='raised', bd=1,
             width=8, height=3, fg='white', command=lambda: pressFunc('e**('))

# factorial ! button
fact = Button(frm_container, text="!", bg='#3D4856', font=("arial", 12), relief='raised', bd=1,
              width=8, height=3, fg='white', command=lambda: pressFunc('factorial('))

# inverse button
inverse = Button(frm_container, text="x\u207b" + "\u00b9", bg='#3D4856', font=("arial", 12), relief='raised', bd=1,
                 width=8, height=3, fg='white', command=lambda: pressFunc('1/'))

# cube button
cube = Button(frm_container, text="x\u00b3", bg='#3D4856', font=("arial", 12), relief='raised', bd=1,
              width=8, height=3, fg='white', command=lambda: pressFunc('**3'))

# square button
square = Button(frm_container, text="x\u00b2", bg='#3D4856', font=("arial", 12), relief='raised', bd=1,
                width=8, height=3, fg='white', command=lambda: pressFunc('**2'))

# Square root button
square_Root = Button(frm_container, text="\u00b2\u221Ax", bg='#3D4856', font=("arial", 12), relief='raised', bd=1,
                     width=8, height=3, fg='white', command=lambda: pressFunc('isqrt('))

# back_space button
back_space = Button(frm_container, text="\u2190 Back", bg='#3D4856', font=("arial", 12), relief='raised', bd=1,
                    width=8, height=3, fg='white', command=lambda: backsp())

# power_fun button
pow_fun = Button(frm_container, text="pow", bg='#3D4856', font=("arial", 12), relief='raised', bd=1,
                 width=8, height=3, fg='white', command=lambda: pressFunc('**'))

# root button
root = Button(frm_container, text="\u207f\u221Ax", bg='#3D4856', font=("arial", 12), relief='raised', bd=1,
              width=8, height=3, fg='white', command=lambda: pressFunc('**(1/'))

# ( button
l_bracket = Button(frm_container, text="\u2772", bg='#3D4856', font=("arial", 12), relief='raised', bd=1,
                   width=8, height=3, fg='white', command=lambda: pressFunc("("))

# ) button
r_bracket = Button(frm_container, text="\u2773", bg='#3D4856', font=("arial", 12), relief='raised', bd=1,
                   width=8, height=3, fg='white', command=lambda: pressFunc(")"))

# asinh button
a_sinh = Button(frm_container, text="asinh", bg='#3D4856', font=("arial", 12), relief='raised', bd=1,
                width=8, height=3, fg='white', command=lambda: pressFunc('asinh('))

# acosh button
a_cosh = Button(frm_container, text="acosh", bg='#3D4856', font=("arial", 12), relief='raised', bd=1,
                width=8, height=3, fg='white', command=lambda: pressFunc('acosh('))

# atanh button
a_tanh = Button(frm_container, text="atanh", bg='#3D4856', font=("arial", 12), relief='raised', bd=1,
                width=8, height=3, fg='white', command=lambda: pressFunc('atanh('))

# packing the expression field
expression_field.grid(row=0, column=0, columnspan=12,
                      pady=5, padx=3, ipady=5, ipadx=18)  # ipadx changes the frame width

# Positioning the button in rows
# Row one
btn1.grid(row=1, column=0)
btn2.grid(row=1, column=1)
btn3.grid(row=1, column=2)
addition.grid(row=1, column=3)
sin_fun.grid(row=1, column=4)
sinh_btn.grid(row=1, column=5)
asin_btn.grid(row=1, column=6)
pow_fun.grid(row=1, column=7)
exp_onentm1.grid(row=1, column=8)
cube.grid(row=1, column=9)
floor_div.grid(row=1, column=10)
a_sinh.grid(row=1, column=11)


# row two
btn4.grid(row=2, column=0)
btn5.grid(row=2, column=1)
btn6.grid(row=2, column=2)
subtract.grid(row=2, column=3)
cos_fun.grid(row=2, column=4)
cosh_btn.grid(row=2, column=5)
acos_btn.grid(row=2, column=6)
log_10.grid(row=2, column=7)
e_x.grid(row=2, column=8)
square.grid(row=2, column=9)
root.grid(row=2, column=10)
a_cosh.grid(row=2, column=11)

# row three
btn7.grid(row=3, column=0)
btn8.grid(row=3, column=1)
btn9.grid(row=3, column=2)
multiply.grid(row=3, column=3)
tan.grid(row=3, column=4)
tanh_btn.grid(row=3, column=5)
atan_btn.grid(row=3, column=6)
log_2.grid(row=3, column=7)
fact.grid(row=3, column=8)
square_Root.grid(row=3, column=9)
l_bracket.grid(row=3, column=10)
a_tanh.grid(row=3, column=11)


# Row Four
btn0.grid(row=4, column=0)
dot.grid(row=4, column=1)
clear.grid(row=4, column=2)
divide.grid(row=4, column=3)
mod.grid(row=4, column=5)
percent.grid(row=4, column=6)
natural_log.grid(row=4, column=7)
inverse.grid(row=4, column=8)
back_space.grid(row=4, column=9)
r_bracket.grid(row=4, column=10)
pibtn.grid(row=4, column=11)

equal.grid(row=4, column=4)

window.resizable(False, False)

window.mainloop()

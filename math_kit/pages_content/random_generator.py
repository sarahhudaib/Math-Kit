from tkinter import Frame, Label
from math import *  # we import all the math functions


class RandomGeneratorPage:
    
    def __init__(self, master, tools):
        self.tools = tools
        
        width = int(tools.screen_width*0.8)
        height = int(tools.screen_height*0.8)
        
        self.randomizer_frame = Frame(master, width=width, height=height, bg=tools.pallete["gray"])
        master.add(self.randomizer_frame)
        
        Label(self.randomizer_frame, text="Random Generator").pack()
        
        
        

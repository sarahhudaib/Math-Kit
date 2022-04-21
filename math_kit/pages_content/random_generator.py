from tkinter import *
from math import *  # we import all the math functions


class RandomGeneratorPage:
    
    def __init__(self, master, tools):
        self.master = master
        self.tools = tools
        
        width = int(tools.screen_width*0.8)
        height = int(tools.screen_height*0.8)
        
        self.randomizer_frame = Frame(master, width=width, height=height, bg=tools.pallete["gray"])
        self.master.add(self.randomizer_frame)
        
        
        

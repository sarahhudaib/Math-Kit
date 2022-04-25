from tkinter import Frame, Label


class NumericalOperationsPage:
    
    def __init__(self, master, tools):
        self.tools = tools
        
        width = int(tools.screen_width*0.8)
        height = int(tools.screen_height*0.8)
        
        self.numerical_frame = Frame(master, width=width, height=height, bg=tools.pallete["gray"])
        master.add(self.numerical_frame)
        
        Label(self.numerical_frame, text="numerical_frame").pack()

from tkinter import Tk, Frame, Button, Label



class WorkspacePage:
    """
    """
    
    def __init__(self, master, tools):
        
        width = int(tools.screen_width*0.8)
        height = int(tools.screen_height*0.8)
        
        self.workspace_frame = Frame(master, width=width, height=height, bg=tools.pallete["gray"])
        master.add(self.workspace_frame)
        




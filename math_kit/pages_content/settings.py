from tkinter import Tk, Frame, Button, Label



class SettingsPage:
    """
    """
    
    def __init__(self, master, tools):
        
        width = int(tools.screen_width*0.8)
        height = int(tools.screen_height*0.8)
        
        self.settings_frame = Frame(master, width=width, height=height, bg=tools.pallete["gray"])
        master.add(self.settings_frame)
        




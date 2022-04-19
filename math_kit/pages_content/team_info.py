from tkinter import Tk, Frame, Button, Label



class TeamInfoPage:
    """
    """
    
    def __init__(self, master, tools):
        
        width = int(tools.screen_width*0.8)
        height = int(tools.screen_height*0.8)
        
        self.team_info_frame = Frame(master, width=width, height=height, bg=tools.pallete["gray"])
        master.add(self.team_info_frame)
        
        




from tkinter import Frame, Label


class StatsPage:
    
    def __init__(self, master, tools):
        self.tools = tools
        
        width = int(tools.screen_width*0.8)
        height = int(tools.screen_height*0.8)
        
        self.stats_frame = Frame(master, width=width, height=height, bg=tools.pallete["gray"])
        master.add(self.stats_frame)
        
        Label(self.stats_frame, text="stats").pack()

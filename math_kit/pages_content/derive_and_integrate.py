from tkinter import Frame, Label


class DeriveAndIntegratePage:
    
    def __init__(self, master, tools):
        self.tools = tools
        
        width = int(tools.screen_width*0.8)
        height = int(tools.screen_height*0.8)
        
        self.derive_frame = Frame(master, width=width, height=height, bg=tools.pallete["gray"])
        master.add(self.derive_frame)
        
        Label(self.derive_frame, text="derive_frame").pack()

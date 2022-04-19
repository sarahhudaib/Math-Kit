from tkinter import Tk, Frame, Button, Label



class HomePage:
    """
    """
    
    def __init__(self, master, tools):
        
        width = int(tools.screen_width*0.8)
        height = int(tools.screen_height*0.8)
        
        self.home_frame = Frame(master, width=width, height=height, bg=tools.pallete["gray"])
        master.add(self.home_frame)
        
        
        page_title = Label(self.home_frame, text="Home Page", font=("Helvetica", 30), bg=tools.pallete["gray"])
        page_title.pack()
        
        info = """
        write the info here
        """

        guide = """
        write the guide here
        """
        
        self.info = Label(self.home_frame, text=info, font=("Berlin Sans FB", 20), bg=tools.pallete["gray"])
        self.info.pack()
        
        self.guide = Label(self.home_frame, text=guide, font=("Berlin Sans FB", 20), bg=tools.pallete["gray"])
        self.guide.pack()

from tkinter import Tk, Frame, Button, Label



class HomePage:
    """
    This class is the home page of the application. It contains the following: 
    - A title label that displays the name of the application   (Label) 
    - A label that displays the info of the application         (Label)
    - A label that displays the guide of the application        (Label)          
    """
    
    def __init__(self, master, tools):
        """
        This method is the constructor of the class. It creates the following:
        - The title label that displays the name of the application   (Label)
        - The label that displays the info of the application         (Label)
        - The label that displays the guide of the application        (Label)
        """
        
        width = int(tools.screen_width*0.8)
        height = int(tools.screen_height*0.8)
        
        self.home_frame = Frame(master, width=width, height=height, bg=tools.pallete["gray"])
        master.add(self.home_frame)
        
        
        page_title = Label(self.home_frame, text="Home Page", font=("Helvetica", 30), bg=tools.pallete["gray"])
        page_title.pack()
        
        info = """
        Welcome To the Home Page of our project 'Math-Kit'

        This project is a GUI tool, built using Python and a few of its libraries; specifically:
        1. tkinter
        2. NumPy
        all for the purpose of performing basic and advanced mathematical operations easily and directly.\n
        """

        guide = """
        A starting guide on how to navigate 'Math-Kit':

        The navigation bar at the top of this window shows four different buttons, 
        that you can use to walk through this project simply by clicking on any them.
        And to further explain the content of each window, here's the following:
        1. Home Page: this window is for briefing you about our project.
        2. Workspace: this window is for performing the basic and advanced mathematical operations.
        3. Team Info: this window is for introducing the developers behind "Math-Kit".
        4. settings: this window is for changing a few characteristics of the GUI window of the project.
        """
        
        self.info = Label(self.home_frame, text=info, font=("Berlin Sans FB", 15), bg=tools.pallete["gray"], 
                          justify="left")
        self.info.pack()
        
        self.guide = Label(self.home_frame, text=guide, font=("Berlin Sans FB", 15), bg=tools.pallete["gray"]
                           , justify="left")
        self.guide.pack()

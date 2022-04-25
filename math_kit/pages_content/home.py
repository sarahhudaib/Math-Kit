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

        welcoming_message = "Welcome to Math Kit!\n"
        
        info = """
        This project is a GUI desktop app that uses a few Python libraries, such as: tkinter to build the GUI 
        and solve various mathematical problems, which will be found in the "workspace" window.

        """

        guide_starting_message =  "A starting guide on how to navigate 'Math-Kit':"


        guide = """
        The navigation bar at the top of this window shows four different buttons, 
        that you can use to walk through this project simply by clicking on any them.
        And to further explain the content of each window, here's the following:\n
        1. Home Page: this window is for briefing you about our project.
        2. Workspace: this window is for performing the basic and advanced mathematical operations.
        3. Team Info: this window is for introducing the developers behind "Math-Kit".
        4. settings: this window is for changing a few characteristics of the GUI window of the project.

        
        """
        
        self.welcoming_message = Label(self.home_frame, text=welcoming_message, font=("Berlin Sans FB", 18), 
        bg=tools.pallete["gray"], justify="center")

        self.welcoming_message.pack()

        self.info = Label(self.home_frame, text=info, font=("Berlin Sans FB", 15), bg=tools.pallete["gray"], 
                          justify="left")
        self.info.pack()

        self.guide_starting_message = Label(self.home_frame, text=guide_starting_message, font=("Berlin Sans FB", 18),
                                            bg=tools.pallete["gray"], justify="center")  

        self.guide_starting_message.pack()
        
        self.guide = Label(self.home_frame, text=guide, font=("Berlin Sans FB", 15), bg=tools.pallete["gray"]
                           , justify="left")
        self.guide.pack()

        





from tkinter import Tk, Frame, Button, Label
import customtkinter


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
        
        self.home_frame = customtkinter.CTkFrame(master, width=width, height=height)
        master.add(self.home_frame)
        
        
        page_title = customtkinter.CTkLabel(self.home_frame, text="Home Page", text_font=("Helvetica", 30))
        page_title.pack(pady=15)

        welcoming_message = "Welcome to Math Kit!\n"
        
        info = """
        This project is a GUI tool that uses a few Python libraries, such as: tkinter and NumPy to 
        help build the GUI and solve various mathematical problems, which will be found in the "workspace" window.

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
        
        self.welcoming_message = customtkinter.CTkLabel(self.home_frame, text=welcoming_message, 
                                                        text_font=("Berlin Sans FB", 18), justify="center")

        self.welcoming_message.pack()

        self.info = customtkinter.CTkLabel(self.home_frame, text=info, text_font=("Berlin Sans FB", 15),
                                           justify="left")
        self.info.pack()

        self.guide_starting_message = customtkinter.CTkLabel(self.home_frame, text=guide_starting_message, 
                                    text_font=("Berlin Sans FB", 18), justify="center")  

        self.guide_starting_message.pack()
        
        self.guide = customtkinter.CTkLabel(self.home_frame, text=guide, text_font=("Berlin Sans FB", 15), 
                                            justify="left")
        self.guide.pack()

        





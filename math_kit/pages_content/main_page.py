from tkinter import Tk, Frame, Button, Label
from tkinter.ttk import Notebook, Style

from pages_content.home import HomePage
from pages_content.workspace import WorkspacePage
from pages_content.team_info import TeamInfoPage
from pages_content.settings import SettingsPage

from pages_content.scientific_calculator import ScientificCalculatorPage

from pages_content.random_generator import RandomGeneratorPage


class MainPage:
    """
    This class represents the background of the pages.  It is used to change the background color of the page  
    when the user clicks on a button.   The background color is changed to the color of the button.
    """
    
    def __init__(self, wind, tools):

        self.wind = wind
        self.tools = tools
        
        self.width = int(tools.screen_width*0.8)
        self.height = int(tools.screen_height*0.8)
        offsetX = int(tools.screen_width*0.1)
        offsetY = int(tools.screen_height*0.1)

        self.wind.geometry(f"{self.width}x{self.height}+{offsetX}+{offsetY}")   
        
        self.NavigationBar()
        
        
        
    def NavigationBar(self):
        """
        This method creates the navigation bar of the application.  It contains the following:
        - A button that displays the home page  (Button) 
        - A button that displays the workspace page  (Button)
        - A button that displays the team info page  (Button)
        - A button that displays the settings page  (Button)
        """
        tools = self.tools
        wind = self.wind 

        self.upper_frame = Frame(self.wind, bg=tools.pallete["dark blue"])
        self.upper_frame.pack(fill="x", expand=True, side="top", anchor="n")

        self.home_button = Button(self.upper_frame, text="Home", bg=tools.pallete["purple"], fg=tools.pallete["white"],
                            font= ("Berlin Sans FB", int(tools.screen_width*0.012)), cursor="hand2")
        self.home_button.grid(row=0, column=0, sticky="n", padx=int(tools.screen_width*0.015), pady=15,
                         ipadx=int(tools.screen_width*0.050), ipady=5)

        self.workspace_button = Button(self.upper_frame, text="Workspace", bg=tools.pallete["blue"], fg=tools.pallete["white"],
                            font= ("Berlin Sans FB", int(tools.screen_width*0.012)), cursor="hand2")
        self.workspace_button.grid(row=0, column=1, sticky="n", padx=int(tools.screen_width*0.015), pady=15,
                              ipadx=int(tools.screen_width*0.050), ipady=5)

        self.team_info_button = Button(self.upper_frame, text="Team Info", bg=tools.pallete["blue"], fg=tools.pallete["white"],
                        font= ("Berlin Sans FB", int(tools.screen_width*0.012)), cursor="hand2")
        self.team_info_button.grid(row=0, column=2, sticky="n", padx=int(tools.screen_width*0.015), pady=15,
                              ipadx=int(tools.screen_width*0.050), ipady=5)

        self.settings_button = Button(self.upper_frame, text="Settings", bg=tools.pallete["blue"], fg=tools.pallete["white"],
                        font= ("Berlin Sans FB", int(tools.screen_width*0.012)), cursor="hand2")
        self.settings_button.grid(row=0, column=3, sticky="n", padx=int(tools.screen_width*0.015), pady=15, 
                             ipadx=int(tools.screen_width*0.050), ipady=5)


        self.pages_display_notebook = Notebook(self.wind)
        self.pages_display_notebook.pack(fill="x", expand=True, side="top", anchor="n")
        style = Style()
        style.layout('TNotebook.Tab', [])

        self.home_button.config(command=lambda: self._SwitchPageBackground(0))
        self.workspace_button.config(command=lambda: self._SwitchPageBackground(1))
        self.team_info_button.config(command=lambda: self._SwitchPageBackground(2))
        self.settings_button.config(command=lambda: self._SwitchPageBackground(3))

        HomePage(self.pages_display_notebook, self.tools)
        WorkspacePage(self.pages_display_notebook, self.tools, self.wind)
        TeamInfoPage(self.pages_display_notebook, self.tools)
        SettingsPage(self.pages_display_notebook, self.tools)
        
        ScientificCalculatorPage(self.pages_display_notebook, self.tools)
        RandomGeneratorPage(self.pages_display_notebook, self.tools)



    def _SwitchPageBackground(self, page_number):
        """
        This method is called when the user clicks on a button.  
        It changes the background color of the page to the color of the button. 
        """
        tools = self.tools
        
        if page_number == 0:
            tools.Navigate(self.wind, self.pages_display_notebook, 0)
            self.home_button.config(bg=tools.pallete["purple"])
            self.workspace_button.config(bg=tools.pallete["blue"])
            self.team_info_button.config(bg=tools.pallete["blue"])
            self.settings_button.config(bg=tools.pallete["blue"])
            
        elif page_number == 1:
            tools.Navigate(self.wind, self.pages_display_notebook, 1)
            self.home_button.config(bg=tools.pallete["blue"])
            self.workspace_button.config(bg=tools.pallete["purple"])
            self.team_info_button.config(bg=tools.pallete["blue"])
            self.settings_button.config(bg=tools.pallete["blue"])
            
        elif page_number == 2:
            tools.Navigate(self.wind, self.pages_display_notebook, 2)
            self.home_button.config(bg=tools.pallete["blue"])
            self.workspace_button.config(bg=tools.pallete["blue"])
            self.team_info_button.config(bg=tools.pallete["purple"])
            self.settings_button.config(bg=tools.pallete["blue"])
            
        elif page_number == 3:
            tools.Navigate(self.wind, self.pages_display_notebook, 3)
            self.home_button.config(bg=tools.pallete["blue"])
            self.workspace_button.config(bg=tools.pallete["blue"])
            self.team_info_button.config(bg=tools.pallete["blue"])
            self.settings_button.config(bg=tools.pallete["purple"])
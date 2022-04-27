from tkinter import Tk, Frame, Button, Label
from tkinter.ttk import Notebook, Style
import customtkinter

from pages_content.home import HomePage
from pages_content.workspace import WorkspacePage
from pages_content.team_info import TeamInfoPage
from pages_content.settings import SettingsPage

from pages_content.scientific_calculator import ScientificCalculatorPage
from pages_content.plotting import Plotter
from pages_content.unit_converter import UnitConverterPage
from pages_content.random_generator import RandomGeneratorPage
from pages_content.stats import StatsPage
from pages_content.derive_and_integrate import DeriveAndIntegratePage


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
        offsetY = int(tools.screen_height*0.05)

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
        
        ipadx_nav_button = int(tools.screen_width*0.040)


        self.upper_frame = customtkinter.CTkFrame(self.wind, bg=tools.pallete["dark blue"])
        self.upper_frame.pack(fill="x", expand=True, side="top", anchor="n")

        self.home_button = customtkinter.CTkButton(self.upper_frame, text="Home", hover_color=tools.pallete["purple"], 
                            text_font= ("Berlin Sans FB", int(tools.screen_width*0.012)), cursor="hand2",
                            fg_color=tools.pallete["purple"])
        self.home_button.grid(row=0, column=0, sticky="n", padx=int(tools.screen_width*0.015), pady=15,
                         ipadx=ipadx_nav_button, ipady=5)

        self.workspace_button = customtkinter.CTkButton(self.upper_frame, text="Workspace", hover_color=tools.pallete["purple"],
                            text_font= ("Berlin Sans FB", int(tools.screen_width*0.012)), cursor="hand2",
                            fg_color=tools.pallete["blue"])
        self.workspace_button.grid(row=0, column=1, sticky="n", padx=int(tools.screen_width*0.015), pady=15,
                              ipadx=ipadx_nav_button, ipady=5)

        self.team_info_button = customtkinter.CTkButton(self.upper_frame, text="Team Info", hover_color=tools.pallete["purple"],
                        text_font= ("Berlin Sans FB", int(tools.screen_width*0.012)), cursor="hand2",
                        fg_color=tools.pallete["blue"])
        self.team_info_button.grid(row=0, column=2, sticky="n", padx=int(tools.screen_width*0.015), pady=15,
                              ipadx=ipadx_nav_button, ipady=5)

        self.settings_button = customtkinter.CTkButton(self.upper_frame, text="Settings", hover_color=tools.pallete["purple"],
                        text_font= ("Berlin Sans FB", int(tools.screen_width*0.012)), cursor="hand2", 
                        fg_color=tools.pallete["blue"])
        self.settings_button.grid(row=0, column=3, sticky="n", padx=int(tools.screen_width*0.015), pady=15, 
                             ipadx=ipadx_nav_button, ipady=5)


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
        Plotter(self.pages_display_notebook, self.tools)
        # NumericalOperationsPage(self.pages_display_notebook, self.tools)
        DeriveAndIntegratePage(self.pages_display_notebook, self.tools)
        StatsPage(self.pages_display_notebook, self.tools)
        RandomGeneratorPage(self.pages_display_notebook, self.tools)
        UnitConverterPage(self.pages_display_notebook, self.tools)



    def _SwitchPageBackground(self, page_number):
        """
        This method is called when the user clicks on a button.  
        It changes the background color of the page to the color of the button. 
        """
        
        tools = self.tools
        tools.PlayAudio("navigate_click.wav")
        
        if page_number == 0:
            tools.Navigate(self.wind, self.pages_display_notebook, 0)
            self.home_button.config(fg_color=tools.pallete["purple"])
            self.workspace_button.config(fg_color=tools.pallete["blue"])
            self.team_info_button.config(fg_color=tools.pallete["blue"])
            self.settings_button.config(fg_color=tools.pallete["blue"])
            
        elif page_number == 1:
            tools.Navigate(self.wind, self.pages_display_notebook, 1)
            self.home_button.config(fg_color=tools.pallete["blue"])
            self.workspace_button.config(fg_color=tools.pallete["purple"])
            self.team_info_button.config(fg_color=tools.pallete["blue"])
            self.settings_button.config(fg_color=tools.pallete["blue"])
            
        elif page_number == 2:
            tools.Navigate(self.wind, self.pages_display_notebook, 2)
            self.home_button.config(fg_color=tools.pallete["blue"])
            self.workspace_button.config(fg_color=tools.pallete["blue"])
            self.team_info_button.config(fg_color=tools.pallete["purple"])
            self.settings_button.config(fg_color=tools.pallete["blue"])
            
        elif page_number == 3:
            tools.Navigate(self.wind, self.pages_display_notebook, 3)
            self.home_button.config(fg_color=tools.pallete["blue"])
            self.workspace_button.config(fg_color=tools.pallete["blue"])
            self.team_info_button.config(fg_color=tools.pallete["blue"])
            self.settings_button.config(fg_color=tools.pallete["purple"])
            
            
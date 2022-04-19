from tkinter import Tk, Frame, Button, Label
from tkinter.ttk import Notebook, Style

from pages_content.main_page import MainPage


class Tools:
    """
    """
    
    def __init__(self):
        
        self.pallete = {
            "blue":  "#0693E3",
            "dark blue": "#3D4856",
            "gray": "#D3D8DE",
            "pink": "#D96794",
            "purple": "#9E3161",
            "white": "#FFFFFF"}
        
        self.screen_width = 0
        self.screen_height = 0
        
        
    @staticmethod
    def Navigate(wind, pages_display_notebook, page):
        pages_display_notebook.select(page)
        
        if page == 0:
            wind.title("Math Kit - Home Page")
        elif page == 1:
            wind.title("Math Kit - Workspace")
        elif page == 2:
            wind.title("Math Kit - Team Info")
        elif page == 3:
            wind.title("Math Kit - Settings")
        

if __name__ == "__main__":
    wind = Tk()
    wind.title("Math Kit - Home Page")
    wind.resizable(0, 0)

    tools = Tools()

    tools.screen_width = wind.winfo_screenwidth()
    tools.screen_height = wind.winfo_screenheight() 

    app = MainPage(wind, tools)
        
    app.wind.mainloop()


from tkinter import Tk, Frame, Button, Label
from tkinter.ttk import Notebook, Style
from PIL import Image, ImageDraw, ImageFilter
from pages_content.main_page import MainPage
from playsound import playsound
import threading
import customtkinter


class Tools:
    """
    This class represents the main window of the application.  It contain the following:
    - A title label that displays the name of the application   (Label)
    - A label that displays the info of the application         (Label)
    - A label that displays the guide of the application        (Label)
    """
    
    def __init__(self):
        
        self.pallete = {
            "blue":  "#0693E3",
            "dark blue": "#3D4856",
            "gray": "#D3D8DE",
            "pink": "#D96794",
            "purple": "#9E3161",
            "white": "#FFFFFF",
            "dark mode": "#2e2e2e"}
        
        self.screen_width = 0
        self.screen_height = 0
        
        
    @staticmethod
    def Navigate(wind, pages_display_notebook, page):
        """
        This method is called when the user clicks on a button. 
        It navigates to the page that the user clicked on.  
        It also changes the color of the button that the user clicked on.      
        """
        pages_display_notebook.select(page)
        
        if page == 0:
            wind.title("Math Kit - Home Page")
        elif page == 1:
            wind.title("Math Kit - Workspace")
        elif page == 2:
            wind.title("Math Kit - Team Info")
        elif page == 3:
            wind.title("Math Kit - Settings")
        
        elif page == 4:
            wind.title("Math Kit - Workspace - Scientific Calculator")
        elif page == 5:
            wind.title("Math Kit - Workspace - Plotter")
        elif page == 9:
            wind.title("Math Kit - Workspace - Convertor")
        elif page == 8:
            wind.title("Math Kit - Workspace - Randomizer")
        elif page == 7:
            wind.title("Math Kit - Workspace - Statistics")
        elif page == 6:
            wind.title("Math Kit - Workspace - Calculas")

            
            
    @staticmethod
    def PlayAudio(name):
        
        def thread(name):
            playsound(r"assets\sounds\{name}".format(name=name))

        threading.Thread(target=thread, args=(name,)).start()
    
    
    def mask_circle_transparent(self, pil_img, blur_radius, offset=0):
        """
        this method cut a PIL image as a circle and make the background transparent

        Args:
            pil_img (PIL image): the image that will be cut as a circle
            blur_radius (_type_): the radius of the blur that will be applied to the image
            offset (int, optional): the offset of the circle from the center of the image, defaults to 0

        Returns:
            PIL image: the image that has been cut as a circle and made transparent
        """
        
        offset = blur_radius * 2 + offset 
        mask = Image.new("L", pil_img.size, 0) 
        draw = ImageDraw.Draw(mask)   
        draw.ellipse((offset, offset, pil_img.size[0] - offset, pil_img.size[1] - offset), fill=255) 
        mask = mask.filter(ImageFilter.GaussianBlur(blur_radius)) 
        result = pil_img.copy() 
        result.putalpha(mask) 
        
        return result
        

if __name__ == "__main__":


    customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
    customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

    wind = customtkinter.CTk()
    wind.title("Math Kit - Home Page")
    wind.resizable(0, 0) 

    tools = Tools()

    tools.screen_width = wind.winfo_screenwidth()
    tools.screen_height = wind.winfo_screenheight() 

    app = MainPage(wind, tools)
        
    app.wind.mainloop()


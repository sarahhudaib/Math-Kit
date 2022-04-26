from tkinter import Tk, Frame, Button, Label, messagebox
from PIL import Image, ImageTk
import webbrowser
import threading


class TeamInfoPage:
    """
    This class is the team info page of the application. It contains the following:
    - A title label that displays the name of the application   (Label)
    - A label that displays the info of the application         (Label)
    - A label that displays the guide of the application        (Label)
    """
    
    def __init__(self, master, tools):
        self.tools = tools
        self.requesting = False 
        
        self.width = int(tools.screen_width*0.8)
        self.height = int(tools.screen_height*0.8)
        
        self.team_info_frame = customtkinter.CTkFrame(master, width=self.width, height=self.height)
        master.add(self.team_info_frame)
        
        self.padx, self.pady, self.ipadx, self.ipady = 20, 30, 10, 10
        self.card_width, self.card_height = int(self.width*0.20), int(self.height*0.5)
        self.avatar_side_lemgth = int(self.width*0.15)
        self.bg, self.bd, self.bd_thickness = "#E3E9C8", self.tools.pallete["blue"], 5
        
        self._SaraCard()
        self._MustafaCard()
        self._BatoolCard()
        self._SalimCard()


    def _SaraCard(self):
        self.sara = customtkinter.CTkFrame(self.team_info_frame, height=self.card_height, bg=self.bg,
                         highlightthickness= self.bd_thickness)
        self.sara.config(highlightbackground = self.bd, highlightcolor= self.bd)
        self.sara.grid(row=0, column=0, padx=self.padx, pady=self.pady, ipadx=self.ipadx, ipady=self.ipady)
        self.sara.grid_columnconfigure(0, weight=1)
        

        self.sara_img = Image.open(r"../math_kit/assets/avatars/sara.png")
        self.sara_img = self.sara_img.resize((self.avatar_side_lemgth, self.avatar_side_lemgth))
        self.sara_img = self.tools.mask_circle_transparent(self.sara_img, 1.5)
        self.sara_avatar_img = ImageTk.PhotoImage(self.sara_img)
        self.sara_avatar = customtkinter.CTkLabel(self.sara, image=self.sara_avatar_img, bg=self.bg)
        self.sara_avatar.image = self.sara_avatar_img
        self.sara_avatar.pack(ipadx=self.ipadx, ipady=self.ipady)
        
        self.name = customtkinter.CTkLabel(self.sara, text="Sarah \nHudaib", bg=self.bg, text_font=("Berlin Sans FB", 20))
        self.name.pack(ipadx=self.ipadx, ipady=self.ipady)
        
        self.sara_github = "https://github.com/sarahhudaib"
        self.sara_linkedin = "https://www.linkedin.com/in/sarah-hudaib-2298a5184/"
        self.sara_github_button = customtkinter.CTkButton(self.sara, text="Github", bg=self.tools.pallete["blue"], 
                                         text_font=("Berlin Sans FB", 18),
                                  command=lambda: self.url_button_handler(self.sara_github))
        self.sara_linkedin_button = customtkinter.CTkButton(self.sara, text="LinkedIn", bg=self.tools.pallete["blue"], 
                                         text_font=("Berlin Sans FB", 18),
                                    command=lambda: self.url_button_handler(self.sara_linkedin))
        self.sara_github_button.pack(padx=10, fill="x", expand=True)
        self.sara_linkedin_button.pack(padx=10, fill="x", expand=True)
    
    
    def _MustafaCard(self):
        self.mustafa = customtkinter.CTkFrame(self.team_info_frame,height=self.card_height,
                                bg=self.bg, highlightthickness= self.bd_thickness)
        self.mustafa.grid(row=0, column=1, padx=self.padx, pady=self.pady, ipadx=self.ipadx, ipady=self.ipady)
        self.mustafa.config(highlightbackground = self.bd, highlightcolor= self.bd)
        self.mustafa.grid_columnconfigure(0, weight=1)
        

        self.mustafa_img = Image.open(r"../math_kit/assets/avatars/mustafa.jpg")
        self.mustafa_img = self.mustafa_img.resize((self.avatar_side_lemgth, self.avatar_side_lemgth))
        self.mustafa_img = self.tools.mask_circle_transparent(self.mustafa_img, 1.5)
        self.mustafa_avatar_img = ImageTk.PhotoImage(self.mustafa_img)
        self.mustafa_avatar = customtkinter.CTkLabel(self.mustafa, image=self.mustafa_avatar_img, bg=self.bg)
        self.mustafa_avatar.image = self.mustafa_avatar_img
        self.mustafa_avatar.pack(ipadx=self.ipadx, ipady=self.ipady)
        
        self.name = customtkinter.CTkLabel(self.mustafa, text="Mustafa \nAlhasanat", bg=self.bg, 
                                           text_font=("Berlin Sans FB", 20))
        self.name.pack(ipadx=self.ipadx, ipady=self.ipady)
        
        self.mustafa_github = "https://github.com/Mustfa1999"
        self.mustafa_linkedin = "https://www.linkedin.com/in/mustafa-alhasanat/"
        self.mustafa_github_button = customtkinter.CTkButton(self.mustafa, text="Github", bg=self.tools.pallete["blue"], 
                                         text_font=("Berlin Sans FB", 18),
                                  command=lambda: self.url_button_handler(self.mustafa_github))
        self.mustafa_linkedin_button = customtkinter.CTkButton(self.mustafa, text="LinkedIn", bg=self.tools.pallete["blue"], 
                                         text_font=("Berlin Sans FB", 18),
                                    command=lambda: self.url_button_handler(self.mustafa_linkedin))
        self.mustafa_github_button.pack(padx=10, fill="x", expand=True)
        self.mustafa_linkedin_button.pack(padx=10, fill="x", expand=True)
        
        
    def _BatoolCard(self):
        self.batool = customtkinter.CTkFrame(self.team_info_frame,height=self.card_height,
                                bg=self.bg, highlightthickness= self.bd_thickness)
        self.batool.grid(row=0, column=2, padx=self.padx, pady=self.pady, ipadx=self.ipadx, ipady=self.ipady)
        self.batool.config(highlightbackground = self.bd, highlightcolor= self.bd)
        self.batool.grid_columnconfigure(0, weight=1)
        

        self.batool_img = Image.open(r"../math_kit/assets/avatars/batool.png")
        self.batool_img = self.batool_img.resize((self.avatar_side_lemgth, self.avatar_side_lemgth))
        self.batool_img = self.tools.mask_circle_transparent(self.batool_img, 1.5)
        self.batool_avatar_img = ImageTk.PhotoImage(self.batool_img)
        self.batool_avatar = customtkinter.CTkLabel(self.batool, image=self.batool_avatar_img, bg=self.bg)
        self.batool_avatar.image = self.batool_avatar_img
        self.batool_avatar.pack(ipadx=self.ipadx, ipady=self.ipady)

        self.name = customtkinter.CTkLabel(self.batool, text="Batool \nRagayah", bg=self.bg, text_font=("Berlin Sans FB", 20))
        self.name.pack(ipadx=self.ipadx, ipady=self.ipady)
        
        self.batool_github = "https://github.com/BatoolBtoush"
        self.batool_linkedin = "https://www.linkedin.com/in/batool-ragayah/"
        self.batool_github_button = customtkinter.CTkButton(self.batool, text="Github", bg=self.tools.pallete["blue"], 
                                         text_font=("Berlin Sans FB", 18),
                                  command=lambda: self.url_button_handler(self.batool_github))
        self.batool_linkedin_button = customtkinter.CTkButton(self.batool, text="LinkedIn", bg=self.tools.pallete["blue"], 
                                         text_font=("Berlin Sans FB", 18),
                                    command=lambda: self.url_button_handler(self.batool_linkedin))
        self.batool_github_button.pack(padx=10, fill="x", expand=True)
        self.batool_linkedin_button.pack(padx=10, fill="x", expand=True)
        
        
    def _SalimCard(self):
        self.salim =  customtkinter.CTkFrame(self.team_info_frame,  height=self.card_height,
                                bg=self.bg, highlightthickness= self.bd_thickness)
        self.salim.grid(row=0, column=3, padx=self.padx, pady=self.pady, ipadx=self.ipadx, ipady=self.ipady)
        self.salim.config(highlightbackground = self.bd, highlightcolor= self.bd)
        self.salim.grid_columnconfigure(0, weight=1)
        

        self.salim_img = Image.open(r"../math_kit/assets/avatars/salim.png")
        self.salim_img = self.salim_img.resize((self.avatar_side_lemgth, self.avatar_side_lemgth))
        self.salim_img = self.tools.mask_circle_transparent(self.salim_img, 1.5)
        self.salim_avatar_img = ImageTk.PhotoImage(self.salim_img)
        self.salim_avatar = customtkinter.CTkLabel(self.salim, image=self.salim_avatar_img, bg=self.bg)
        self.salim_avatar.image = self.salim_avatar_img
        self.salim_avatar.pack(ipadx=self.ipadx, ipady=self.ipady)

        self.name = customtkinter.CTkLabel(self.salim, text="Salim \nHassouneh", bg=self.bg, text_font=("Berlin Sans FB", 20))
        self.name.pack(ipadx=self.ipadx, ipady=self.ipady)
        
        self.salim_github = "https://github.com/SalimHass"
        self.salim_linkedin = "https://www.linkedin.com/in/salim-hassouneh/"
        self.salim_github_button = customtkinter.CTkButton(self.salim, text="Github", bg=self.tools.pallete["blue"], 
                                       text_font=("Berlin Sans FB", 18),
                                  command=lambda: self.url_button_handler(self.salim_github))
        self.salim_linkedin_button = customtkinter.CTkButton(self.salim, text="LinkedIn", bg=self.tools.pallete["blue"], 
                                       text_font=("Berlin Sans FB", 18),
                                    command=lambda: self.url_button_handler(self.salim_linkedin))
        self.salim_github_button.pack(padx=10, fill="x", expand=True)
        self.salim_linkedin_button.pack(padx=10, fill="x", expand=True)
        
        
    def url_button_handler(self, url):
        """
        opens the url in the default browser

        Args:
            url (string): url to be opened
        """
        
        def thread(url):
            """
            a function that opens the url in the default browser

            Args:
                url (string): url to be opened
            """
            
            self.requesting = True
            webbrowser.open_new(url)
            self.requesting = False
        
        
        # if there is a web page is openning now, raise an error message box
        if self.requesting:
            messagebox.showerror("Page is openning !!!", "There is a page opening currently, please wait until it is finished.")
            return
        # open the web page in a new thread only if there is no web page is openning now
        threading.Thread(target=thread, args=(url,)).start()
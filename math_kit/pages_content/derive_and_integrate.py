from tkinter import Frame, Label, LabelFrame, StringVar, messagebox
from PIL import Image, ImageTk
import numpy as np
import customtkinter


class DeriveAndIntegratePage:
    
    def __init__(self, master, tools):
        
        self.tools = tools
        self.current_poly = None
        
        width = int(tools.screen_width*0.8)
        height = int(tools.screen_height*0.8)
        
        self.derive_frame = customtkinter.CTkFrame(master, width=width, height=height)
        master.add(self.derive_frame)
        
        headline = """Derivate, Integrate, and Evaluate your polynomials !"""
        
        self.title = customtkinter.CTkLabel(self.derive_frame, text=headline, justify="center", 
                           text_font=("Berlin Sans FB", int(tools.screen_width*0.02)))
        self.title.pack(pady=int(tools.screen_height*0.02))
        
        self.container = Frame(self.derive_frame, width=width, bg=tools.pallete["dark mode"])
        self.container.pack()
    
    
        self._PolyPrepareFrame()
        self._PolyDeriveIntFrame()
        

    def _PolyPrepareFrame(self):
        
        self.poly_prepare_frame = LabelFrame(self.container, bg=self.tools.pallete["dark mode"], 
                                          text="Prepare the Polynomial", fg="white")
        self.poly_prepare_frame.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)
        
        self.poly_variable = StringVar()
        self.poly_entry =  customtkinter.CTkEntry(self.poly_prepare_frame, text_font=("Helvetica", 18), 
                                        textvariable=self.poly_variable, width=250)        
        # self.poly_variable.set("Coeficients")
        self.poly_variable.set("2 5 20")
        
        info_image_size = int(self.tools.screen_width*0.02)
        self.info_icon = Image.open(r"../math_kit/assets/icons/info.png")
        self.info_icon = self.info_icon.resize((info_image_size, info_image_size))
        self.info_icon_img = ImageTk.PhotoImage(self.info_icon)
        self.info_img_button = customtkinter.CTkButton(self.poly_prepare_frame, image=self.info_icon_img, 
                                cursor="hand2", command=lambda: self._InfoIcon(), text="",
                                hover_color=self.tools.pallete["purple"], width=info_image_size, 
                                height=info_image_size)
        self.info_img_button.image = self.info_icon_img
        
        
        self.poly_enter_button = customtkinter.CTkButton(self.poly_prepare_frame, text="Enter Polynomial", 
                    text_font=("Helvetica", 15, "bold"), cursor="hand2", 
                    command=lambda: self._EnterPoly(), hover_color=self.tools.pallete["purple"])


        self.poly_entry.grid(row=0, column=0, columnspan=3, sticky="ew")
        self.info_img_button.grid(row=0, column=3)
                
        self.poly_enter_button.grid(row=1, column=0, columnspan=4, sticky="nsew")
        
        for child in self.poly_prepare_frame.winfo_children():
            child.grid_configure(padx=40, pady=10) 
            
            
    def _PolyDeriveIntFrame(self):
        
        self.poly_derive_int_frame = LabelFrame(self.container, bg=self.tools.pallete["dark mode"], 
                                          text="Derive/Integrate the Polynomial", fg="white")
        self.poly_derive_int_frame.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)
        
        self.poly_derive_button = customtkinter.CTkButton(self.poly_derive_int_frame, 
                    text="Derive the current Polynomial", 
                    text_font=("Helvetica", 15, "bold"), cursor="hand2", 
                    command=lambda: self._DerIntEval("der"), hover_color=self.tools.pallete["purple"])

        self.poly_int_button = customtkinter.CTkButton(self.poly_derive_int_frame, 
                    text="Integrate the current Polynomial", 
                    text_font=("Helvetica", 15, "bold"), cursor="hand2", 
                    command=lambda: self._DerIntEval("int"), hover_color=self.tools.pallete["purple"])


        self.eval_label = customtkinter.CTkLabel(self.poly_derive_int_frame, text="Evaluate at:", 
                                                text_font=("Helvetica", 18))

        self.eval_variable = StringVar()
        self.eval_entry =  customtkinter.CTkEntry(self.poly_derive_int_frame, text_font=("Helvetica", 18), 
                                        textvariable=self.eval_variable, width=100) 

        self.poly_eval_button = customtkinter.CTkButton(self.poly_derive_int_frame, 
                    text="Evaluate the current Polynomial", 
                    text_font=("Helvetica", 15, "bold"), cursor="hand2", 
                    command=lambda: self._DerIntEval("eval"), hover_color=self.tools.pallete["purple"])

        self.eval_result_variable = StringVar()
        self.eval_result_entry =  customtkinter.CTkEntry(self.poly_derive_int_frame, text_font=("Helvetica", 18), 
                                        textvariable=self.eval_result_variable) 


        self.poly_derive_button.grid(row=0, column=0, columnspan=2, sticky="nsew")
        self.poly_int_button.grid(row=1, column=0, columnspan=2, sticky="nsew")
        
        self.eval_label.grid(row=2, column=0)
        self.eval_entry.grid(row=2, column=1)
        self.poly_eval_button.grid(row=3, column=0, columnspan=2, sticky="nsew")
        
        self.eval_result_entry.grid(row=4, column=0, columnspan=2, sticky="nsew")
        
        
        
        for child in self.poly_derive_int_frame.winfo_children():
            child.grid_configure(padx=30, pady=10, ipadx=20) 
    
    
    def _EnterPoly(self):
            
        array = list(self.poly_entry.get().strip().split(" "))
        
        try:
            array = [float(i) for i in array]
        except:
            messagebox.showerror("Invalid Input", "List's elements must be integers or floats seperated by spaces.")
            return
        
        self.current_poly = np.poly1d(array)
    
        messagebox.showinfo("Poly is ready", "The polynomial has been entered correctly!.")
    
    
    def _DerIntEval(self, process):
        
        if not self.current_poly:
            messagebox.showerror("Invalid Input", "You have to ENTER the polynomial.")
            return
            
        if process == "der":
            self.current_poly = np.polyder(self.current_poly)
            poly_list = " ".join([str(i) for i in list(self.current_poly.c)])
            self.poly_variable.set(poly_list)
            
        elif process == "int":
            self.current_poly = np.polyint(self.current_poly)
            poly_list = " ".join([str(i) for i in list(self.current_poly.c)])
            self.poly_variable.set(poly_list)
            
        elif process == "eval":
            
            value = self.eval_variable.get().strip()
            if not value.isdigit():
                self.eval_result_variable.set("Invalid input value!")
                messagebox.showerror("Invalid Input", "The point must be an integer.")
                return
            
            value = float(value)            
            try:
                self.eval_result_variable.set(self.current_poly(value))
            except:
                self.eval_result_variable.set("Invalid input")
                messagebox.showerror("Invalid Input", "You have to ENTER the polynomial correctly.")
                return
    
        
    def _InfoIcon(self):
        self.explaination = """We have to enter coefficients of polynomial in the following form: \n4 3 -2 10
        that means:  4x^3 + 3x^2 - 2x + 10"""
        
        messagebox.showinfo("How to insert polynomial's coefficients", self.explaination)
 
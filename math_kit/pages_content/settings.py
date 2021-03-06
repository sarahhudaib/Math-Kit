from tkinter import Tk, Frame, Button, Label
import tkinter
import tkinter.messagebox
import customtkinter
import sys


class SettingsPage:
    """
    This class  is the settings page of the application. It contains the following:
    - A title label that displays the name of the application   (Label)
    - A label that displays the info of the application         (Label)
    - A label that displays the guide of the application        (Label)
    """

    def __init__(self, master, tools):

        width = int(tools.screen_width * 0.8)
        height = int(tools.screen_height * 0.8)

        self.settings_frame = customtkinter.CTkFrame(master, width=width, height=height, bg=tools.pallete["gray"])
        master.add(self.settings_frame)
        
        self.theme_switch = customtkinter.CTkSwitch(self.settings_frame, text="Dark Mode", command=self.change_mode)
        self.theme_switch.pack(pady=40)
        
    
    def change_mode(self):
        if self.theme_switch.get() == 1:
            customtkinter.set_appearance_mode("dark")
        else:
            customtkinter.set_appearance_mode("light")


# customtkinter.set_appearance_mode(
#     "System"
# )  # Modes: "System" (standard), "Dark", "Light"
# customtkinter.set_default_color_theme(
#     "blue"
# )  # Themes: "blue" (standard), "green", "dark-blue"


# class App(customtkinter.CTk):

#     WIDTH = 780
#     HEIGHT = 520

#     def __init__(self):
#         super().__init__()

#         self.title("Settings")
#         self.geometry(f"{App.WIDTH}x{App.HEIGHT}")
#         # self.minsize(App.WIDTH, App.HEIGHT)

#         self.protocol(
#             "WM_DELETE_WINDOW", self.on_closing
#         )  # call .on_closing() when app gets closed

#         # ============ create two frames ============

#         # configure grid layout (2x1)
#         self.grid_columnconfigure(1, weight=1)
#         self.grid_rowconfigure(0, weight=1)

#         self.frame_left = customtkinter.CTkFrame(
#             master=self, width=180, corner_radius=0
#         )
#         self.frame_left.grid(row=0, column=0, sticky="nswe")

#         self.frame_right = customtkinter.CTkFrame(master=self)
#         self.frame_right.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)

#         # ============ frame_left ============

#         # configure grid layout (1x11)
#         self.frame_left.grid_rowconfigure(
#             0, minsize=10
#         )  # empty row with minsize as spacing
#         self.frame_left.grid_rowconfigure(5, weight=1)  # empty row as spacing
#         self.frame_left.grid_rowconfigure(
#             8, minsize=20
#         )  # empty row with minsize as spacing
#         self.frame_left.grid_rowconfigure(
#             11, minsize=10
#         )  # empty row with minsize as spacing

#         self.label_1 = customtkinter.CTkLabel(
#             master=self.frame_left,
#             text="CustomTkinter",
#             text_font=("Roboto Medium", -16),
#         )  # font name and size in px
#         self.label_1.grid(row=1, column=0, pady=10, padx=10)

#         self.button_1 = customtkinter.CTkButton(
#             master=self.frame_left,
#             text="Get Started",
#             fg_color=("gray75", "gray30"),  # <- custom tuple-color
#             command=self.button_event,
#         )
#         self.button_1.grid(row=2, column=0, pady=10, padx=20)

#         self.button_2 = customtkinter.CTkButton(
#             master=self.frame_left,
#             text="Appearance",
#             fg_color=("gray75", "gray30"),  # <- custom tuple-color
#             command=self.button_event,
#         )
#         self.button_2.grid(row=3, column=0, pady=10, padx=20)

#         self.button_3 = customtkinter.CTkButton(
#             master=self.frame_left,
#             text="Privacy and security",
#             fg_color=("gray75", "gray30"),  # <- custom tuple-color
#             command=self.button_event,
#         )
#         self.button_3.grid(row=4, column=0, pady=10, padx=20)

#         self.switch_1 = customtkinter.CTkSwitch(master=self.frame_left, text="Show tab search button")
#         self.switch_1.grid(row=9, column=0, pady=10, padx=20, sticky="w")

#         self.switch_2 = customtkinter.CTkSwitch(
#             master=self.frame_left, text="Theme", command=self.change_mode
#         )
#         self.switch_2.grid(row=10, column=0, pady=10, padx=20, sticky="w")

#         # ============ frame_right ============

#         # configure grid layout (3x7)
#         self.frame_right.rowconfigure((0, 1, 2, 3), weight=1)
#         self.frame_right.rowconfigure(7, weight=10)
#         self.frame_right.columnconfigure((0, 1), weight=1)
#         self.frame_right.columnconfigure(2, weight=0)

#         self.frame_info = customtkinter.CTkFrame(master=self.frame_right)
#         self.frame_info.grid(
#             row=0, column=0, columnspan=2, rowspan=4, pady=20, padx=20, sticky="nsew"
#         )

#         # ============ frame_info ============

#         # configure grid layout (1x1)
#         self.frame_info.rowconfigure(0, weight=1)
#         self.frame_info.columnconfigure(0, weight=1)

#         self.label_info_1 = customtkinter.CTkLabel(
#             master=self.frame_info,
#             text="We coded and developed each calculator \n" 
#             + "individually and put each one through strict, \n"
#             + "comprehensive testing.\n"
#             + " However, please inform us if you notice even\n"
#             + "the slightest error \n"
#             + "your input is extremely valuable to us.",
#             height=100,
#             fg_color=("white", "gray38"),  # <- custom tuple-color
#             justify=tkinter.LEFT,
#         )
#         self.label_info_1.grid(column=0, row=0, sticky="nwe", padx=15, pady=15)

#         self.progressbar = customtkinter.CTkProgressBar(master=self.frame_info)
#         self.progressbar.grid(row=1, column=0, sticky="ew", padx=15, pady=15)

#         # ============ frame_right ============

#         self.radio_var = tkinter.IntVar(value=0)

#         self.label_radio_group = customtkinter.CTkLabel(
#             master=self.frame_right, text="CTkRadioButton Group:"
#         )
#         self.label_radio_group.grid(
#             row=0, column=2, columnspan=1, pady=20, padx=10, sticky=""
#         )

#         self.radio_button_1 = customtkinter.CTkRadioButton(
#             master=self.frame_right, variable=self.radio_var, value=0
#         )
#         self.radio_button_1.grid(row=1, column=2, pady=10, padx=20, sticky="n")

#         self.radio_button_2 = customtkinter.CTkRadioButton(
#             master=self.frame_right, variable=self.radio_var, value=1
#         )
#         self.radio_button_2.grid(row=2, column=2, pady=10, padx=20, sticky="n")

#         self.radio_button_3 = customtkinter.CTkRadioButton(
#             master=self.frame_right, variable=self.radio_var, value=2
#         )
#         self.radio_button_3.grid(row=3, column=2, pady=10, padx=20, sticky="n")

#         self.slider_1 = customtkinter.CTkSlider(
#             master=self.frame_right,
#             from_=0,
#             to=1,
#             number_of_steps=3,
#             command=self.progressbar.set,
#         )
#         self.slider_1.grid(row=4, column=0, columnspan=2, pady=10, padx=20, sticky="we")

#         self.slider_2 = customtkinter.CTkSlider(
#             master=self.frame_right, command=self.progressbar.set
#         )
#         self.slider_2.grid(row=5, column=0, columnspan=2, pady=10, padx=20, sticky="we")

#         self.slider_button_1 = customtkinter.CTkButton(
#             master=self.frame_right,
#             height=25,
#             text="CTkButton",
#             command=self.button_event,
#         )
#         self.slider_button_1.grid(
#             row=4, column=2, columnspan=1, pady=10, padx=20, sticky="we"
#         )

#         self.slider_button_2 = customtkinter.CTkButton(
#             master=self.frame_right,
#             height=25,
#             text="CTkButton",
#             command=self.button_event,
#         )
#         self.slider_button_2.grid(
#             row=5, column=2, columnspan=1, pady=10, padx=20, sticky="we"
#         )

#         self.checkbox_button_1 = customtkinter.CTkButton(
#             master=self.frame_right,
#             height=25,
#             text="CTkButton",
#             border_width=3,  # <- custom border_width
#             fg_color=None,  # <- no fg_color
#             command=self.button_event,
#         )
#         self.checkbox_button_1.grid(
#             row=6, column=2, columnspan=1, pady=10, padx=20, sticky="we"
#         )

#         self.check_box_1 = customtkinter.CTkCheckBox(
#             master=self.frame_right, text="Font size"
#         )
#         self.check_box_1.grid(row=6, column=0, pady=10, padx=20, sticky="w")

#         self.check_box_2 = customtkinter.CTkCheckBox(
#             master=self.frame_right, text="Fixed-width font"
#         )
#         self.check_box_2.grid(row=6, column=1, pady=10, padx=20, sticky="w")

#         self.entry = customtkinter.CTkEntry(
#             master=self.frame_right, width=120, placeholder_text="CTkEntry"
#         )
#         self.entry.grid(row=8, column=0, columnspan=2, pady=20, padx=20, sticky="we")

#         self.button_5 = customtkinter.CTkButton(
#             master=self.frame_right, text="CTkButton", command=self.button_event
#         )
#         self.button_5.grid(row=8, column=2, columnspan=1, pady=20, padx=20, sticky="we")

#         # set default values
#         self.radio_button_1.select()
#         self.switch_2.select()
#         self.slider_1.set(0.2)
#         self.slider_2.set(0.7)
#         self.progressbar.set(0.5)
#         self.slider_button_1.configure(state=tkinter.DISABLED, text="Customize fonts")
#         self.radio_button_3.configure(state=tkinter.DISABLED)
#         self.check_box_1.configure(state=tkinter.DISABLED, text="Always show full URLs")
#         self.check_box_2.select()

#     def button_event(self):
#         print("Button pressed")

    

#     def on_closing(self, event=0):
#         self.destroy()

#     def start(self):
#         self.mainloop()


# if __name__ == "__main__":
#     app = App()
#     app.start()

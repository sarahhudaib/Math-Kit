from tkinter import *

# Conversion factors
unit_dict = {
    "cm": 0.01,
    "m": 1.0,
    "km": 1000.0,
    "feet": 0.3048,
    "miles": 1609.344,
    "inches": 0.0254,
    "grams": 1.0,
    "kg": 1000.0,
    "quintals": 100000.0,
    "tonnes": 1000000.0,
    "pounds": 453.592,
    "sq. m": 1.0,
    "sq. km": 1000000.0,
    "are": 100.0,
    "hectare": 10000.0,
    "acre": 4046.856,
    "sq. mile": 2590000.0,
    "sq. foot": 0.0929,
    "cu. cm": 0.001,
    "Litre": 1.0,
    "ml": 0.001,
    "gallon": 3.785,
}

lengths = [
    "cm",
    "m",
    "km",
    "feet",
    "miles",
    "inches",
]
weights = [
    "kg",
    "grams",
    "quintals",
    "tonnes",
    "pounds",
]
temps = ["Celsius", "Fahrenheit"]
areas = ["sq. m", "sq. km", "are", "hectare", "acre", "sq. mile", "sq. foot"]
volumes = ["cu. cm", "Litre", "ml", "gallon"]

# Options for drop-down menu
OPTIONS = [
    "select units",
    "cm",
    "m",
    "km",
    "feet",
    "miles",
    "inches",
    "kg",
    "grams",
    "quintals",
    "tonnes",
    "pounds",
    "Celsius",
    "Fahrenheit",
    "sq. m",
    "sq. km",
    "are",
    "hectare",
    "acre",
    "sq. mile",
    "sq. foot",
    "cu. cm",
    "Litre",
    "ml",
    "gallon",
]

OPTIONS_length: [
    "select units",
    "cm",
    "m",
    "km",
    "feet",
    "miles",
    "inches",
]

OPTIONS_weight = [
    "select units",
    "kg",
    "grams",
    "quintals",
    "tonnes",
    "pounds",
]


OPTIONS_temps = [
    "select units",
    "Celsius",
    "Fahrenheit",
]

OPTIONS_areas = [
    "select units",
    "sq. m",    
    "sq. km",
    "are",
    "hectare",
    "acre",
    "sq. mile",
    "sq. foot",
]

OPTIONS_volumes = [
    "select units",
    "cu. cm",
    "Litre",
    "ml",
    "gallon",
]


# Main window
wind = Tk()
wind.geometry("400x350")
wind.title("Unit Converter")
wind["bg"] = "#3D4856"


def convert():
    """ function to Convert units"""
    user_input = float(input_entry.get())
    input_unit = input_opt.get()
    output_unit = output_opt.get()

    cons = [
        input_unit in lengths and output_unit in lengths,
        input_unit in weights and output_unit in weights,
        input_unit in temps and output_unit in temps,
        input_unit in areas and output_unit in areas,
        input_unit in volumes and output_unit in volumes,
    ]

    if any(cons):  # If both the units are of same type, do the conversion
        if input_unit == "Celsius" and output_unit == "Fahrenheit":
            output_entry.delete(0, END)
            output_entry.insert(0, (user_input * 1.8) + 32)
        elif input_unit == "Fahrenheit" and output_unit == "Celsius":
            output_entry.delete(0, END)
            output_entry.insert(0, (user_input - 32) * (5 / 9))
        else:
            output_entry.delete(0, END)
            output_entry.insert(
                0, round(user_input * unit_dict[input_unit] / unit_dict[output_unit], 5)
            )

    else:  # Display error if units are of different types
        output_entry.delete(0, END)
        output_entry.insert(0, "Invalid conversion")


input_opt = StringVar()
input_opt.set(OPTIONS[0])

output_opt = StringVar()
output_opt.set(OPTIONS[0])
 

# Widgets
input_label = Label(wind, text="Input")
input_label.grid(row=0, column=0, pady=20)

input_entry = Entry(wind, justify="center", font="bold")
input_entry.grid(row=1, column=0, padx=35, ipady=5)

input_menu = OptionMenu(wind, input_opt, *OPTIONS)
input_menu.grid(row=1, column=1)
input_menu.config(font="Arial 10")

output_label = Label(wind, text="Output")
output_label.grid(row=2, column=0, pady=20)

output_entry = Entry(wind, justify="center", font="bold")
output_entry.grid(row=3, column=0, padx=35, ipady=5)

output_menu = OptionMenu(wind, output_opt, *OPTIONS)
output_menu.grid(row=3, column=1)
output_menu.config(font="Arial 10")

convert_button = Button(wind, text="Convert", command=convert, padx=80, pady=2)
convert_button.grid(row=4, column=0, columnspan=2, pady=50)

wind.mainloop()

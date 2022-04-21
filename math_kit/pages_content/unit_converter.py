from tkinter import Label, Tk, StringVar, Entry, Button, Frame, OptionMenu, Checkbutton, Listbox, Scrollbar, IntVar, ttk, DoubleVar, W
from unit_convertor_dict import conversion_dict as UCdict


window = Tk()
Label(window, text="Quantity").grid(row=0, column=0, columnspan=4, sticky=W)


def Converter(*args):
    """Calculate the conversion."""
    try:  # Try to convert the quantity to the to unit.  If it fails, return the error message.
        # Convert the quantity to the to unit.  If it fails, return the error message.
        result = UCdict[fromVariable.get()][toVariable.get()](
            float(quantVariable.get()))
        resultVar.set(result)
    except KeyError:
        resultVar.set("")
        pass
    result = "{0:.4f}".format(UCdict[quantVariable.get().lower(
    )][fromVariable.get()][toVariable.get()](val.get()))
    result_string = val.get(), fromVariable.get(), "=", result, toVariable.get()
    resultVar.set(result_string)


def MakeUnit(*args):
    """ Function to set the unit comboboxes to the selected unit. """
    fromVariable.set(quantVariable.get().lower()
                     )  # Set the from unit to the selected unit.
    # Set the to unit to the selected unit.
    toVariable.set(quantVariable.get().lower())
    cbUnitFrom['values'] = tuple(UCdict[quantVariable.get().lower()].keys())
    cbUnitTo['values'] = tuple(UCdict[quantVariable.get().lower()].keys())
    cbUnitFrom.current(0)


quantVariable = StringVar()
cbQuantity = ttk.Combobox(window, textvariable=quantVariable, state="readonly",
                          values=tuple([x.capitalize() for x in UCdict.keys()]))
cbQuantity.bind("<<ComboboxSelected>>", MakeUnit)
cbQuantity.grid(row=0, column=4)

Label(window, text="Convert").grid(row=1, column=0)

val = DoubleVar()
Entry(window, textvariable=val, width=7).grid(row=1, column=1)

fromVariable = StringVar()
cbUnitFrom = ttk.Combobox(window, textvariable=fromVariable, state="readonly")
cbUnitFrom.grid(row=1, column=2)

Label(window, text="to").grid(row=1, column=3)

# This is the variable to store the unit to be converted to.
toVariable = StringVar()
cbUnitTo = ttk.Combobox(window, textvariable=toVariable, state="readonly")
cbUnitTo.grid(row=1, column=4)

Button(window, text="Convert", command=Converter).grid(row=2, columnspan=5)

resultVar = StringVar()  # This is the variable to store the result.
resultLabel = Label(window, textvariable=resultVar).grid(row=3, column=0, columnspan=5, sticky=W)

for child in window.winfo_children():
    child.grid_configure(padx=5, pady=5)

window.mainloop()

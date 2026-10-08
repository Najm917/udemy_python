from tkinter import *


def mile_to_km():
    try:
        mile = float(mile_input.get())
        km = round(mile * 1.609, 2)
        KM_result_lable.config(text=km)
    except ValueError:  # Specific exception use karna safer hota hai
        KM_result_lable.config(text="Invalid")


window = Tk()
window.title("Mile To KM")
window.geometry("500x300")
window.config(padx=30, pady=25)

FONT = ("Arial", 14)
BOLD_FONT = ("Arial", 16, "bold")

# Row 0
mile_input = Entry(width=8, font=FONT)
mile_input.insert(0, "0")
mile_input.grid(column=1, row=0, padx=10, pady=10)

mile_lable = Label(text="Miles", font=FONT)
mile_lable.grid(column=2, row=0, padx=10, pady=10)

# Row 1
is_equal = Label(text="is equal to", font=FONT)
is_equal.grid(column=0, row=1, padx=10, pady=10)

KM_result_lable = Label(text="0", font=BOLD_FONT)
KM_result_lable.grid(column=1, row=1, padx=10, pady=10)

KM_lable = Label(text="KM", font=FONT)
KM_lable.grid(column=2, row=1, padx=10, pady=10)

# Row 2
calculate_button = Button(
    text="Calculate",
    command=mile_to_km,
    font=BOLD_FONT,
    padx=10,
    pady=3,
)
calculate_button.grid(column=1, row=2, padx=10, pady=15)

window.mainloop()
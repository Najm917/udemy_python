import tkinter


def km_to_mile():
    try:
        km = float(km_input.get())
        miles = round(km / 1.609, 2)
        miles_result_label.config(text=f"{miles}")
    except ValueError:
        miles_result_label.config(text="Error")


window = tkinter.Tk()
window.title("KM to Mile Converter")
window.geometry("500x300")
window.config(padx=40, pady=40)

# Fonts bada kar diya display ke liye
FONT = ("Arial", 16)
BOLD_FONT = ("Arial", 18, "bold")

# Row 0: Input aur unit label
km_input = tkinter.Entry(width=8, font=FONT)
km_input.insert(0, "0")
km_input.grid(column=1, row=0, padx=10, pady=10)

km_label = tkinter.Label(text="KM", font=FONT)
km_label.grid(column=2, row=0, padx=10, pady=10)

# Row 1: Result
is_equal = tkinter.Label(text="is equal to", font=FONT)
is_equal.grid(column=0, row=1, padx=10, pady=10)

miles_result_label = tkinter.Label(text="0", font=BOLD_FONT)
miles_result_label.grid(column=1, row=1, padx=10, pady=10)

miles_label = tkinter.Label(text="Miles", font=FONT)
miles_label.grid(column=2, row=1, padx=10, pady=10)

# Row 2: Calculate Button
calculate_button = tkinter.Button(
    text="Calculate",
    command=km_to_mile,
    font=BOLD_FONT,
    padx=15,
    pady=5,  # Button ka size bada karne ke liye
)
calculate_button.grid(column=1, row=2, pady=20)

window.mainloop()
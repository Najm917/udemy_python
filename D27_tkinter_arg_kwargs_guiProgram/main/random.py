import tkinter

window = tkinter.Tk()
window.title("Title")
window.minsize(300, 200)

# Bina kisi padding ke grid
my_label = tkinter.Label(text="Name:")
my_label.grid(row=4, column=3,padx=10)

button = tkinter.Button(text="Submit")
button.grid(row=1, column=3)

window.mainloop()
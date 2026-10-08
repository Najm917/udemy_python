import tkinter

window=tkinter.Tk()

window.title("My First GUI Program")
window.minsize(500,300)

my_lable=tkinter.Label(text="i am lable", font=("Arial",24,"bold"))
# my_lable.pack(side="left")

my_lable.grid(column=1,row=1)
# -------------------------------------
# Entry
user_input=tkinter.Entry(width=10)

# show position 

# user_input.pack()
#           OR

# _____________________________________
# create button and function

def button_click():
  print("hey i am button")
  # my_lable["text"]="clicked"
  # my_lable['font']=("Arial",30,"bold")
  # my_lable.config(font=("Arial",24,"bold"),text="Clicked")
  my_lable.config(text=user_input.get(),font=("Arial",30,"bold"))
  
  
button=tkinter.Button(text="Click me",command=button_click)
button.pack()


# _____________________________
# update component
# my_lable["text"]="New Textssss"
my_lable.config(text="New text")

window.mainloop()
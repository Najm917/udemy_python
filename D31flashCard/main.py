from tkinter import *
import pandas,random

BACKGROUND_COLOR = "#B1DDC6" 
current_card={}
to_lern={}
try:
  data=pandas.read_csv("data/learn_new_word.csv")
except FileNotFoundError:
  orginal_data=pandas.read_csv("data/hindi_english_words_only.csv")
  to_lern=orginal_data.to_dict(orient="records")
else:
  to_lern=data.to_dict(orient="records")

def next_card():
  global current_card,flip_time
  window.after_cancel(flip_time)
  current_card=random.choice(to_lern)

  canvas.itemconfig(card_title,text="English",fill="black")
  canvas.itemconfig(card_word,text=current_card["English"],fill="black")
  canvas.itemconfig(card_bgc,image=front_image)
  flip_time=window.after(3000,func=show_hindi)
  

def show_hindi():
  canvas.itemconfig(card_title,text="Hindi",fill="white")
  canvas.itemconfig(card_word,text=current_card["Hindi"],fill="white")
  canvas.itemconfig(card_bgc,image=back_image)
  
  
def is_known():
  to_lern.remove(current_card)
  print(len(to_lern))
  data=pandas.DataFrame(to_lern)
  data.to_csv("data/learn_new_word.csv",index=False)
# _________________________________
window=Tk()
window.title("FLASH CARD ")
window.config(bg=BACKGROUND_COLOR,padx=50,pady=50)
flip_time=window.after(5000,func=show_hindi)

# ____________________________________
canvas=Canvas(width=800,height=526)
front_image=PhotoImage(file="images/card_front.png")
back_image=PhotoImage(file="images/card_back.png")
card_bgc=canvas.create_image(400,263,image=front_image)
canvas.grid(row=0,column=0,columnspan=2)
card_title=canvas.create_text(400,150,text="Title",font=("Arial",40))
card_word=canvas.create_text(400,263,text="word",font=("Arial",40,"bold"))
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
# _________________________________
cross_image=PhotoImage(file="images/wrong.png")
cross_btn=Button(image=cross_image,command=next_card)
cross_btn.grid(row=1,column=0)
# __________________________________
check_image=PhotoImage(file="images/right.png")
right_btn=Button(image=check_image,command=is_known)
right_btn.grid(row=1,column=1)







window.mainloop()
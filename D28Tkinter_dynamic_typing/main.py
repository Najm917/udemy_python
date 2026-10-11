from tkinter import *
import time,math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps=0
timer=None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    global reps, timer
    if timer is not None:
        window.after_cancel(timer)
        timer = None
    canvas.itemconfig(timer_text, text="00:00")
    title_lable.config(text="Timer", fg=GREEN)
    check_mark_label.config(text="")
    reps = 0
    start_button.config(state="normal")  # Wapas click karne ke laayak banayein

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def stsrt_timer():
  start_button.config(state="disabled")
  global reps
  reps+=1
  work_sec=WORK_MIN*60
  short_brack=SHORT_BREAK_MIN*60
  long_brack=LONG_BREAK_MIN*60
  
  if reps%8==0: 
    count_down(long_brack)
    title_lable.config(fg=PINK ,text="Brack",bg=YELLOW)
  elif reps%2==0:
    count_down(short_brack)
    title_lable.config(fg=RED,bg=YELLOW,text="Brack")
    
  else:
    count_down(work_sec)
    title_lable.config(fg=GREEN,bg=YELLOW,text="Work")
    
  
# def reset_timer():
#   count_down(SHORT_BREAK_MIN*60)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(counter):
  count_min=math.floor(counter/60)
  count_sec=counter%60
  
  # jab countdown 1 se 9 ke bich me hogo 01,02.. ye show hoga 
  
  if count_sec<10:
    count_sec=f"0{count_sec}"
  if count_min < 10:
    count_min = f"0{count_min}"
  
  canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
  if counter>0:
    global timer
    
    timer=window.after(1000,count_down,counter-1)
    
  else:
    stsrt_timer()
    mark=""
    work_section=math.floor(reps/2)
    for _ in range(work_section):
      mark+="✔️"
    check_mark_label.config(text=mark,)
# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("POMODORO")
window.config(padx=100,pady=40,bg=YELLOW)




title_lable=Label(text="Timer",background=YELLOW,fg=GREEN,font=(FONT_NAME,26))
title_lable.grid(column=1,row=0)

canvas = Canvas(width=200, background=YELLOW,height=223,highlightthickness=0)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(100, 110, image=tomato)
timer_text=canvas.create_text(103,125,text="00:00",font=(FONT_NAME,25,"bold"),fill="white")
canvas.grid(column=1,row=1)


start_button=Button(text="Start",highlightthickness=0,command=stsrt_timer)
start_button.grid(column=0,row=2,)

reset_button=Button(text="Reset",highlightthickness=0,command=reset_timer)
reset_button.grid(column=2,row=2)

check_mark_label=Label(fg=GREEN,bg=YELLOW,font=(0))

check_mark_label.grid(column=1,row=3)



window.mainloop()
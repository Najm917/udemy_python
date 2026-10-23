from tkinter import *
import time
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"
class QuizInterFace():
  def __init__(self,quiz_brain:QuizBrain):
    
    self.quiz=quiz_brain
    
    self.window=Tk()
    self.window.title("QUIZ GAME")
    self.window.config(bg=THEME_COLOR,padx=20,pady=20)
    self.score_lable=Label(text="Score: 0",fg="white",bg=THEME_COLOR)
    self.score_lable.grid(row=0,column=0)

    self.canvas=Canvas(width=300,height=250,bg="white")
    self.question_text=self.canvas.create_text(150,125,text="Some Question Text",fill=THEME_COLOR,font=("Arial",20),width=290)
    self.canvas.grid(row=1,column=0,columnspan=2,pady=50)
    
    true_btn_img=PhotoImage(file="images/true.png")
    self.true_btn=Button(image=true_btn_img,width=70,height=70,command=self.true_press)
    self.true_btn.grid(row=2,column=0)
    
    
    false_btn_img=PhotoImage(file="images/false.png")
    self.false_btn=Button(image=false_btn_img,height=70,width=70,command=self.false_press)
    self.false_btn.grid(row=2,column=1)
    
    self.get_next_question()
    
    self.window.mainloop()
    
  
  def get_next_question(self):
    if self.quiz.still_has_questions():
      self.canvas.config(bg="white")
      self.score_lable.config(text=f"Score: {self.quiz.score}")
      q_text=self.quiz.next_question()
      self.canvas.itemconfig(self.question_text,text=q_text)
    else:
      self.canvas.itemconfig(self.question_text,text="You've reached the end of the question")
      self.true_btn.config(state="disabled")
      self.false_btn.config(state="disabled")
    
  def true_press(self):
    self.give_feedback(self.quiz.check_answer("True"))
  
  def false_press(self):
    is_right=self.quiz.check_answer("False")
    self.give_feedback(is_right)
    
  def give_feedback(self,is_right):
    if is_right:
      self.canvas.config(bg="green")
    else:
      self.canvas.config(bg="red")
    self.window.after(1000,self.get_next_question)


class QuestionBrain:
  def __init__(self,q_list):
    self.score=0
    self.question_number=0
    self.question_list=q_list
    
  def still_has_quetion(self):
    return self.question_number<len(self.question_list)
    
  def next_question(self):
    current_question=self.question_list[self.question_number]
    self.question_number += 1
    ask_user=input(f"Q.{self.question_number}:{current_question.text} (True/False)? ")
    self.check_answer(ask_user,current_question.answer)
    
  def check_answer(self,ask_user,correct_answer):
    if ask_user.lower()==correct_answer.lower():
      print("You got it right:")
      self.score+=1
    else:
      print("thas's wrong.")
    print(f"the correct answer was: {correct_answer}.")
    print(f"Your cirrent score is: {self.score}/{self.question_number}")
      
    

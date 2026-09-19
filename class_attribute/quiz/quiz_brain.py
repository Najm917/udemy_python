
class QuizBrain:
  def __init__(self,q_list):
    self.question_number=0
    self.score=0
    self.question_list=q_list
    
  def continue_quiz(self):
    return self.question_number < len(self.question_list)
     

  def new_question(self):
    current_question=self.question_list[self.question_number]
    self.question_number+=1
    user_answer=input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
    self.check_answer(user_answer,current_question.answer)
    
  def check_answer(self,user_answer,correctt_answer):
    if user_answer.lower()==correctt_answer.lower():
      self.score+=1
      print("you got it right")
      
    else:
      print("that's wrong")
    print(f"correct answer was : {correctt_answer}")
    print(f"your current score is:{self.score}/{self.question_number}")
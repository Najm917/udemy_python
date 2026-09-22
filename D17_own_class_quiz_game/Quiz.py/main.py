from data import question_data
from question_model import Question
from quiz_brain import QuestionBrain

question_bank=[]
for question in question_data:
  question_text=question["text"]
  question_answer=question["answer"]
  new_question=Question(q_text=question_text,q_answer=question_answer)
  question_bank.append(new_question)

quiz=QuestionBrain(question_bank)
while quiz.still_has_quetion():
  quiz.next_question()
  
print(f"you've complete the quiz")
print(f"Your final score is {quiz.score}/{quiz.question_number}")
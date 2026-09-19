from question_and_ans import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)
    
    
quiz=QuizBrain(question_bank)
while quiz.continue_quiz():
    quiz.new_question() 
    
print("you have completed the quiz")
print(f"your final score was : {quiz.score}/{quiz.question_number}")

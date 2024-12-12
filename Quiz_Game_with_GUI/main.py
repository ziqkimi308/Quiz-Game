"""
********************************************************************************
* Project Name:  Quiz Game with GUI
* Description:   It is a fun and interactive quiz application built with Python and Tkinter. It allows you to test your knowledge on various topics by answering True/False questions. 
* Author:        ziqkimi308
* Created:       2024-12-12
* Updated:       2024-12-12
* Version:       1.0
********************************************************************************
"""

from data import question_data
from quiz_logic import QuizLogic, QuestionPrototype
from quiz_interface import QuizInterface

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = QuestionPrototype(question_text, question_answer)
    question_bank.append(new_question)


quiz = QuizLogic(question_bank)
quiz_ui = QuizInterface(quiz)


# while quiz.still_has_questions():
#     quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")

"""
********************************************************************************
* Project Name:  Quiz Game
* Description:   This project is a True/False Quiz Game built with Python. It challenges users with a series of questions, evaluates their answers, and keeps track of the score throughout the game.
* Author:        ziqkimi308
* Created:       2024-12-05
* Updated:       2024-12-05
* Version:       1.0
********************************************************************************
"""

from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for item in question_data:
    question = Question(item["text"],item["answer"])
    question_bank.append(question)

quiz = QuizBrain(question_bank)
quiz.next_question()

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz.")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
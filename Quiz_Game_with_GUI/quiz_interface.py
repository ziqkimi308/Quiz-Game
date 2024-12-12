from tkinter import *
from quiz_logic import QuizLogic

# -------------------------------- CONSTANT ----------------------------------- #
THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")

# -------------------------------- INTERFACE ------------------------------------- #
class QuizInterface:

	# 
	def __init__(self, quiz_brain: 	QuizLogic):
		self.quiz = quiz_brain
		self.window = Tk()
		self.window.title("Quizz Game")
		self.window.config(padx=20, pady=20, bg=THEME_COLOR)
		# Canvas
		self.canvas = Canvas(width=300, height=250, bg="white")
		self.canvas.grid(row=1, column=0, columnspan=2, padx=20, pady=20)
		# x and y in create_text() are positional arg and does not accept keyword arg
		self.question_text = self.canvas.create_text(150, 125, width=280, text="TESTING", font=FONT, fill=THEME_COLOR)

		# Label
		self.label_score = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
		self.label_score.grid(row=0, column=1, sticky="nsew")

		# Button
		true_image = PhotoImage(file="./images/true.png")
		false_image = PhotoImage(file="./images/false.png")

		self.button_true = Button(image=true_image, highlightthickness=0, command=self.clicked_true)
		self.button_true.grid(row=2, column=0)
		self.button_false = Button(image=false_image, highlightthickness=0, command=self.clicked_false)
		self.button_false.grid(row=2, column=1)

		# Call next question function
		self.get_next_question()

		self.window.mainloop()

	def get_next_question(self):
		self.canvas.config(bg="white")
		self.button_true.config(state=NORMAL)
		self.button_false.config(state=NORMAL)
		if self.quiz.still_has_questions():
			self.label_score.config(text=f"Score: {self.quiz.score}")
			q_text = self.quiz.next_question()
			self.canvas.itemconfig(self.question_text, text=q_text)
		else:
			self.canvas.itemconfig(self.question_text, text="The Quiz ends here.")
			self.button_true.config(state=DISABLED)
			self.button_false.config(state=DISABLED)

	# Create two functions for button right and wrong
	def clicked_true(self):
		self.button_false.config(state=DISABLED)
		self.button_true.config(state=DISABLED)
		is_right = self.quiz.check_answer("True")
		self.give_feedback(is_right)

	def clicked_false(self):
		self.button_false.config(state=DISABLED)
		self.button_true.config(state=DISABLED)
		is_right = self.quiz.check_answer("False")
		self.give_feedback(is_right)

	def give_feedback(self, is_right):
		if is_right:
			self.canvas.config(bg="green")
		else:
			self.canvas.config(bg="red")
		self.window.after(1000, self.get_next_question)
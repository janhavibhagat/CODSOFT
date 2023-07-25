import tkinter as tk
from tkinter import messagebox

class QuizGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Game")
        self.question_number = 0
        self.score = 0

        self.questions = [
            {
                "question": "What is the capital of France?",
                "options": ["Paris", "London", "Berlin", "Madrid"],
                "correct_option": 0
            },
            {
                "question": "Who painted the Mona Lisa?",
                "options": ["Leonardo da Vinci", "Pablo Picasso", "Vincent van Gogh", "Michelangelo"],
                "correct_option": 0
            },
            {
                "question": "Which planet is known as the Red Planet?",
                "options": ["Mars", "Jupiter", "Venus", "Mercury"],
                "correct_option": 0
            },
            {
                "question": "What is the largest ocean in the world?",
                "options": ["Pacific Ocean", "Atlantic Ocean", "Indian Ocean", "Arctic Ocean"],
                "correct_option": 0
            }
        ]

        self.question_label = tk.Label(root, text="")
        self.question_label.pack()

        self.option_buttons = []
        for i in range(4):
            button = tk.Button(root, text="", width=30, command=lambda i=i: self.check_answer(i))
            button.pack()
            self.option_buttons.append(button)

        self.score_label = tk.Label(root, text="Score: 0")
        self.score_label.pack()

        self.next_question()

    def next_question(self):
        if self.question_number < len(self.questions):
            self.question_label.config(text=self.questions[self.question_number]["question"])
            options = self.questions[self.question_number]["options"]
            for i in range(4):
                self.option_buttons[i].config(text=options[i])
            self.score_label.config(text="Score: " + str(self.score))
        else:
            messagebox.showinfo("Quiz Game", f"Quiz completed!\nYour score: {self.score}/{len(self.questions)}")
            self.root.quit()

    def check_answer(self, selected_option):
        correct_option = self.questions[self.question_number]["correct_option"]
        if selected_option == correct_option:
            self.score += 1
        self.question_number += 1
        self.next_question()

root = tk.Tk()
quiz_game = QuizGame(root)
root.mainloop()

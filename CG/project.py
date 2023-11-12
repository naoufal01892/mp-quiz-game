import tkinter as tk
from tkinter import IntVar
import threading
import csv
import random
import os
import sys

# Add sound module path
additional_paths = ["./sound"]
sys.path.extend(os.path.abspath(path) for path in additional_paths)

# Custom sound module (replace this with your actual sound module)
import sound

script_dir = os.path.dirname(__file__)
csv_file_path = os.path.join(script_dir, 'Book1.csv')

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz App")
        self.root.geometry("800x400")

        self.question_label = tk.Label(self.root, text="", font=("Arial", 12))
        self.question_label.grid(row=0, column=0, pady=10, sticky=tk.W)

        self.options_frame = tk.Frame(self.root)
        self.options_frame.grid(row=1, column=0, pady=10, padx=20, sticky=tk.W)

        self.checkbox_vars = [IntVar() for _ in range(4)]
        self.checkboxes = [tk.Checkbutton(self.options_frame, variable=var, text="", anchor=tk.W) for var in self.checkbox_vars]
        [checkbox.grid(row=i, column=0, pady=5, sticky=tk.W) for i, checkbox in enumerate(self.checkboxes)]

        self.option_labels = [tk.Label(self.options_frame, text="", font=("Arial", 10), anchor=tk.W) for _ in range(4)]
        [label.grid(row=i, column=1, pady=5, sticky=tk.W) for i, label in enumerate(self.option_labels)]

        self.validate_button = tk.Button(self.root, text="Validate", command=self.validate_answers)
        self.validate_button.grid(row=2, column=0, pady=10, padx=20, sticky=tk.W)

        self.ignore_button = tk.Button(self.root, text="Ignore", command=self.next_question)
        self.ignore_button.grid(row=2, column=1, pady=10, padx=20, sticky=tk.W)

        self.feedback_label = tk.Label(self.root, text="", font=("Arial", 10))
        self.feedback_label.grid(row=2, column=0, columnspan=2, pady=10, padx=20, sticky=tk.W)

        self.score = 0
        self.question_number = 0
        self.correct_option_index = 0
        self.correct_answer = ""

    def start_quiz(self):
        self.next_question()

    def display_options(self, options_list):
        [var.set(0) for var in self.checkbox_vars]
        [checkbox.config(text=options_list[i]) for i, checkbox in enumerate(self.checkboxes)]
        [label.config(text=options_list[i]) for i, label in enumerate(self.option_labels)]

        # Print the options to the terminal for verification
        print("Options displayed in GUI:")
        for i, option in enumerate(options_list):
            print(f"{i + 1}. {option}")

    def next_question(self):
        random_rows = get_random_rows(csv_file_path, num_rows=5)
        self.correct_option_index, self.correct_answer = display_question_and_options(random_rows)

        self.question_label.config(text=random_rows[0][0])

        options_list = random_rows[0][2:]
        random.shuffle(options_list)

        self.display_options(options_list)

    def validate_answers(self):
        user_choices = [var.get() for var in self.checkbox_vars]
        if 1 in user_choices:
            user_choice = user_choices.index(1) + 1
            validation_player = sound.ValidationPlayer() if user_choice == self.correct_option_index else sound.ErrorPlayer()
            validation_player.play()
            message = "Your answer is correct!" if user_choice == self.correct_option_index else f"The correct answer is option {self.correct_option_index}: {self.correct_answer}."
            self.feedback_label.config(text=message)

            if user_choice == self.correct_option_index:
                self.score += 1

        self.question_number += 1
        if self.question_number < 20:
            self.next_question()
        else:
            self.show_final_score()

    def show_final_score(self):
        self.feedback_label.config(text=f"Quiz Completed! Your total score is {self.score}.")

def get_random_rows(file_path, num_rows):
    with open(file_path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        csv_data = list(csv_reader)
        random_line_index = random.randint(0, len(csv_data) - 1)
        start_index = max(0, random_line_index - num_rows + 1)
        random_rows = csv_data[start_index:random_line_index + 1]
        return random_rows

def display_question_and_options(options):
    print("Question:")
    question = options[0][0]
    print(question)

    answer = options[0][1]
    options_list = options[0][2:]
    all_options = random.sample(options_list, k=3)
    all_options.append(answer)

    random.shuffle(all_options)

    # Print the options to the terminal for verification
    print("Options displayed in terminal:")
    for i, option in enumerate(all_options, 1):
        print(f"{i}. {option}")

    return all_options.index(answer) + 1, all_options

def run_quiz():
    root = tk.Tk()
    app = QuizApp(root)
    root.after(1000, app.start_quiz)  # Start the quiz after 1 second
    root.mainloop()

if __name__ == "__main__":
    run_quiz()

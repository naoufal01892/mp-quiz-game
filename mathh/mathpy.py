import os
import csv
import random

script_dir = os.path.dirname(__file__)
csv_file_path = os.path.join(script_dir, 'math.csv')

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

    for i, option in enumerate(all_options, 1):
        print(f"{i}. {option}")

    return all_options.index(answer) + 1, answer

def get_user_choice():
    while True:
        try:
            choice = int(input("Enter the number of your choice: "))
            if 1 <= choice <= 4:
                return choice
            else:
                print("Invalid choice. Please enter a valid number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def run_quiz():
    for _ in range(20):
        random_rows = get_random_rows(csv_file_path, num_rows=5)
        correct_option_index, correct_answer = display_question_and_options(random_rows)

        user_choice = get_user_choice()
        if user_choice == correct_option_index:
            print("Correct!")
        else:
            print(f"Wrong! The correct answer is option {correct_option_index}: {correct_answer}.")

if __name__ == "__main__":
    run_quiz()

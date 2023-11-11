import csv
import random

csv_file_path = 'Book1.csv'

def get_random_rows(file_path, num_rows):
    with open(file_path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        csv_data = list(csv_reader)
        
        # Choose a random line index
        random_line_index = random.randint(0, len(csv_data) - 1)
        
        # Get the last 5 rows from the chosen line
        start_index = max(0, random_line_index - num_rows + 1)
        random_rows = csv_data[start_index:random_line_index + 1]
        
        return random_rows

def display_question_and_options(options):
    print("Question:")
    print(options[0][0])  # Display the question
    print("\nOptions:")
    for i, row in enumerate(options, 1):
        print(f"{i}. {row[1]}")  # Display the options

def get_user_choice(options):
    while True:
        try:
            choice = int(input("Enter the number of your choice: "))
            if 1 <= choice <= len(options):
                return options[choice - 1]
            else:
                print("Invalid choice. Please enter a valid number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

# Example usage
random_rows = get_random_rows(csv_file_path, num_rows=5)
display_question_and_options(random_rows)

chosen_option = get_user_choice(random_rows)
print(f"You chose: {chosen_option[1]}")
print(f"The answer is: {chosen_option[2] if len(chosen_option) > 2 else 'No answer available.'}")

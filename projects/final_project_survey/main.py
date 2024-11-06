# main.py

"""
This script controls the survey logic by performing the following steps:
- User Authentication: Prompts user name
- Loading Questions: Reads the questions from repository.json file
- Presenting Questions: Randomly selects and presents each question to the user by calling the class from questions.py
- Collecting Responses: Gathers whether each answer is correct or not.
- Displaying Results: Shows the percentage of correct answers. Answers can only be right or wrong, wven multiplechoice
- Saving Responses: Saves the results in a timestamped .txt file in answers directory.
"""

import json
import os
import random
from datetime import datetime
from questions import MultipleChoiseQuestion, NumericalQuestion

def load_questions(json_path):
    """
    Reads the repository json file

    Args:
        json_path (string): path to repository.json file

    Returns:
        list: list of questions dictionaries
    """    
    try:
        with open(json_path, 'r', encoding='utf-8') as file:
            questions = json.load(file)
        return questions
    except FileNotFoundError:
        print(f"Error: The file {json_path} was not found.")
        exit(1) # Ends programm registering it was because of error
    except json.JSONDecodeError:
        print(f"Error: The file {json_path} contains invalid JSON.")
        exit(1)

def create_answers_directory(directory='answers'):
    """
    If the answers folder does not exist it creates one

    Args:
        directory (str, optional): Directory name. Defaults to 'answers'.
    """    
    if not os.path.exists(directory):
        os.makedirs(directory)

# I need a function to calculate the percentage since im using it in two different ocasions (end of test and saving file)
def calculate_percentage(results):
    """
    Calculate total questions, count correct and calculate percentage of correct answers

    Args:
        results (list): List with dictionary containing questions ID and if correct or not

    Returns:
        tuple: total questions, correct answers and percentage
    """    
    total_questions = len(results)
    correct_answers = sum(1 for r in results if r['is_correct'])
    percentage = (correct_answers / total_questions) * 100 if total_questions > 0 else 0
    return total_questions, correct_answers, percentage

# Function to save the results in a txt file with readable content
def save_results(username, results, directory='answers'):
    """
    Save the tests result in a .txt file with name and timestamp for multiple runs for the same user,

    Args:
        username (string): Users name provided in begining
        results (list): List with results from last test taken
        directory (str, optional): Directory of answers name. Defaults to 'answers'.
    """    
    total, correct, percentage = calculate_percentage(results)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{username}_{timestamp}.txt"
    filepath = os.path.join(directory, filename)
    try:
        with open(filepath, 'w', encoding='utf-8') as file:
            file.write(f"User: {username}\n")
            file.write(f"Date and Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            for result in results:
                file.write(f"Question ID: {result['id']} - {'Correct' if result['is_correct'] else 'Incorrect'}\n")
            file.write(f"\nTotal Correct: {correct} out of {total} ({percentage:.2f}%)\n")
        print(f"\nResults saved to {filepath}")
    except Exception as e:
        print(f"Error saving results: {e}")

# Main logic of the programm after necessary function were defined above
def main():
    # Step 1: Get user name
    username = input("Enter your name: ").strip()
    if not username:
        print("Name cannot be empty.")
        exit(1)

    # Step 2: Load questions
    json_path = 'repository.json'
    questions = load_questions(json_path)
    if not questions:
        print("No questions found in the JSON file.")
        exit(1)

    # Shuffle questions to present them in random order
    random.shuffle(questions)

    # Initialize results list
    results = []

    # Step 3: Present each question
    for question_data in questions:
        q_type = question_data.get("type")
        if q_type == "multiple_choice":
            question = MultipleChoiseQuestion(question_data)
        elif q_type == "numerical":
            question = NumericalQuestion(question_data)
        else:
            print(f"Unknown question type for question ID {question_data.get('id')}. Skipping.")
            continue

        # Process the question and collect result
        q_id, is_correct = question.process()
        results.append({"id": q_id, "is_correct": is_correct})

    # Step 4: Calculate and display results
    total_questions, correct_answers, percentage = calculate_percentage(results)
    print(f"\nSurvey Completed!\nYou answered {correct_answers} out of {total_questions} questions correctly.")
    print(f"Your score: {percentage:.2f}%")

    # Step 5: Save results
    create_answers_directory()
    save_results(username, results)

    # Step 6: Offer to retake the survey
    while True:
        retake = input("\nDo you want to retake the survey? (y/n): ").strip().lower()
        if retake == 'y':
            main()  # Restart the survey
            break
        elif retake == 'n':
            print("Thank you for participating!")
            break
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

if __name__ == "__main__":
    main()

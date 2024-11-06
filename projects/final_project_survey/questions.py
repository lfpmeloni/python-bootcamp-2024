# questions.py

"""
This script defines two classes:

- MultipleChoiceQuestion: Handles multiple-choice questions.
- NumericalQuestion: Handles numerical questions.

Each class is responsible for displaying the question, processing user input, validating the answer, and returning whether the answer is correct or not.
"""

import re # regular expressions to facilitate answer handling

class MultipleChoiseQuestion:
    def __init__(self, question_data):
        """
        Initialize the MultipleChoiceQuestion with question data.

        Args:
            question_data (_type_): JSON with question information
        """        
        self.id = question_data.get("id")
        self.question = question_data.get("question")
        self.options = question_data.get("options", [])
        self.correct_answers = [
            idx + 1 for idx, option in enumerate(self.options) if option.get("is_correct", False)
        ]
        self. max_options = 4 # As per Fahrschule questions structure

    def display_question(self):
        """
        Display the multiple-choice question and its options.
        """
        print(f"\nQuestion {self.id}: {self.question}")
        for idx, option in enumerate(self.options, start=1):
            print(f"{idx}. {option['text']}")

    def get_user_input(self):
        """
        Prompt the user to input their answer(s).
        Accepts various separators: ; , - space

        Raises:
            ValueError: Provided more inputs than options available
            ValueError: Provided non numerical answer

        Returns:
            list: returns list of integers representing chosen option numbers
        """
        while True:
            user_input = input("Enter your answer(s) (e.g., 1;2 or 1,3 or 2-3 or 1 4): ")
            #Split input based on allowed separatores
            choices = re.split(r'[;, \-]+', user_input.strip())
            try:
                # Convert to unique integers
                choices = list(set(int(choice) for choice in choices if choice.isdigit()))
                if not choices:
                    raise ValueError
                if any(choice < 1 or choice > len(self.options) for choice in choices):
                    raise ValueError
                return choices
            except ValueError:
                print("Invalid input. Please enter valid option numbers separated by ; , - or space.")

    def check_answer(self, user_choices):
        """
        Compare user choices with correct answers.
        Returns True if all correct answers are selected and no incorrect ones are chosen.
        Otherwise, returns False.

        Args:
            user_choices (_type_): _description_

        Returns:
            _type_: _description_
        """
        return set(user_choices) == set(self.correct_answers)
    
    def process(self):
        """
        Full process of displaying quyestions, getting input, checking if correct.

        Returns:
            tuple: a tuple of (question_id (string), is_correct (bool)
        """
        self.display_question()
        user_choices = self.get_user_input()
        is_correct = self.check_answer(user_choices)
        return (self.id, is_correct)
    
class NumericalQuestion:
    def __init__(self, question_data):
        """
        Initialize the NumericalQuestion with question data.

        Args:
            question_data (json): Retrive from JSON
        """        
        self.id = question_data.get("id")
        self.question = question_data.get("question")
        self.correct_answer = question_data.get("answer")
        self.unit = question_data.get("unit", "")

    def display_question(self):
        """
        Display the numerical question.
        """
        print(f"\nQuestion {self.id}: {self.question}")
        if self.unit:
            print(f"  (Answer in {self.unit})")

    def get_user_input(self):
        """
        Prompt the user to input their numerical answer.
        Accepts integers and floats with '.' or ',' as decimal separators.

        Returns:
            number: a float or int
        """
        while True:
            user_input = input("Enter your answer: ").replace(',', '.').strip()
            try:
                # Attempt to convert to float or int
                if '.' in user_input:
                    value = float(user_input)
                else:
                    value = int(user_input)
                return value
            except ValueError:
                print("Invalid input. Please enter a numerical value using '.' or ',' as decimal separators.")

    def check_answer(self, user_value):
        """
        Compare user input with the correct answer.

        Args:
            user_value (_type_): _description_

        Returns:
            _type_: True if exactly equal, else False
        """        
        return user_value == self.correct_answer

    def process(self):
        """
        Full process of displaying the question, getting input, and checking the answer.

        Returns:
            tuple: a tuple of (question_id, is_correct).
        """        
        self.display_question()
        user_value = self.get_user_input()
        is_correct = self.check_answer(user_value)
        return (self.id, is_correct)
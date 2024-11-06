# Final Project: Fahrschule Survey

## Project Guidelines - Project 3: Survey

Create a Survey Tool. A file containing questions and possible answers should be read. The questions and possible answers should be displayed to the user. The user can then answer the question. Ensure that the correct data types are used! The completed data set is then appended to a file.

Minimum Requirements:

- Read the file (e.g., .txt file) and create the survey
- Include at least one multiple-choice question and one numerical question
- Ability to retake the survey without overwriting previous responses
- Save responses for possible further processing
Optional Additional Tasks:
- Graphical User Interface (GUI)
- Input of questions and answer options in the user interface or a separate script (.json can be useful here)
Survey Points
Import questions/answers 10
Creating survey from input 10
ask numerical questions 5
ask multiple choice
question 5

## Implementation Documentation

### Minimal components

- Create a json repository with questions. Essential for structured data handling.
- Write code to read the json file and create the survey.  Core functionality for dynamic survey generation.
- Define how the survey will be presented to user and explain how he should answer multiple choice and numerical questions. Important for user experience and clarity. Ensures data integrity and proper input validation.
- for numerical must accept float and int and commas ',' and dots '.'as separators. Anything else generate exeption. Allows flexibility in user responses, accommodating various input styles.
- for multiple choice (max 4 answers) accept any type of separotor of numericals. Ex: 12; 1,2; 1 - 2; 1 2. Allows flexibility in user responses, accommodating various input styles.
- Save answers on the end as an txt file on a specific folder with name, date and time as title of txt file. Critical for data persistence and future processing.
- Show results and offer to retake survey. Enhances user engagement and allows multiple attempts without data loss.

### Further improvements

- Error Handling and Validation: Implement comprehensive error handling to manage unexpected inputs or file read/write errors gracefully. Enhances user experience by preventing crashes and providing meaningful feedback.
-

### Possible optional features to implement later on

- GUI interface using Django
- Adding questions that contain pictures
- User Authentication: Allow users to enter their names or IDs before taking the survey. Facilitates personalized data storage and tracking

# Crashcourse Book using Django

We’ll write a web app called Learning Log that allows users to log the topics they’re interested in and make journal entries as they learn about each topic. The Learning Log home page will describe the site and invite users to either register or log in. Once logged in, a user can create new topics, add new entries, and read and edit existing entries

## Using Virtual Environment

For this project i set up a new virtual encironment. On the project folder use the following commands:

    python -m venv venv
    .\venv\Scripts\activate

    deactivate # To deactivate venv

Make sure to use the your virtual environment's Python interpreter:

Click on the Python interpreter selection button in the lower-left corner of VS Code (it may show as Python 3.x or Select Interpreter).
Choose the interpreter located in your venv folder (something like .\venv\Scripts\python.exe).

## Install Django

    pip install --upgrade pip
    pip install django
    
# Content of Week 1

## Day 1

### Naming best practices

Snakecase and Camelcase

    Snakecase -> my_variable, myvarible, my_function
    Camelcase -> myFunction, MyClass

### Common Markdown lint Rules

Here are some examples of common lint rules:

*Heading Style:*

    Enforces consistent heading styles, like using # for top-level headings and ## for subheadings.
    Example Rule: "Headings should not skip levels."

*Line Length:*

    Enforces a maximum line length for readability (e.g., 80 characters).
    Example Rule: "Lines should be wrapped at 80 characters."

*Code Block Style:*

Ensures consistency in code block styles, like using triple backticks (```) for code snippets. Example Rule:

```Use fenced code blocks instead of indentation.```

### Functions and Methods

    name = "albert einstein"

                print(name.title())
    function -> ^^^^^

                print(name.title())
    method ->              ^^^^^^^

A method is an action that Python can perform on a piece of data.
Every method is followed by a set of parentheses, because methods often need additional information to do their work.

Other examples:

    print(name.upper())
    print(name.lower())

### Working with pip

pip is the standard way to manage Python libraries and dependencies.

    pip freeze > requirements.txt
    pip install -r requirements.txt

Creating a new Virtual Environment (venv)

    python -m venv env_name

### Working with GitHub

1. Create repository in GitHub (github.com)
2. Clone the created repository to workspace

        git clone https://github.com/lfpmeloni/python-bootcamp-2024

3. Create, work on items and add to repository

        git add .

4. Commit and push to main branch

        git commit -m "description of the commit"
        git push origin main

### Usefull Shortcuts on Visual Studio Code

Toggle line comment

    Ctrl+/

Toggle block comment

    Shift+Alt+A

Open the Outline view

    Ctrl+Shift+O

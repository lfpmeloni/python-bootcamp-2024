# Exercise 1)
# Calculate exactly how old Shiva is to the day.

""" Shiva is beyond time and space, so there is no age for Shiva. Therefore let's get the farthest past date that we can go with datetime"""

import datetime as dt
now = dt.datetime.now()
#print(now.year - dt.datetime.min.year)

""" Seems like Shiva has the same age as Jesus but actually Shiva is the teachers dog =) Lets calculate the age of my dog Frada """

geburstag_frada = dt.datetime(2021,11,1)
print("Frada's age is: ",(now - geburstag_frada).days/365," years old")

# Exercise 2)
# Open the file Datumsspass.txt in Python and read the individual rows.

""" Using the Pythonic way of opening and reading a text file. The with statement ensures that the file will be closed automatically when the block is exited. """

# Initialize an empty list to store the lines
date_lines = []

# Open and read the text file
with open('Datumsspass.txt', 'r') as file:
    # Interate through each line in the file
    for line in file:
        #Strip any leading/trainling whitespace and append to the list
        date_lines.append(line.strip())

# Print the list to check the contents
print(date_lines)

# Exercise 3)
# Standardize the formatting of the date entries in Datumsspass.txt, the specific format is up to you.  

# Generate a list with parsing structure for each line
format_lines = [
    None,
    "%d.%m.%y", # 3.7.14
    "%A, the %d. %B %Y", # monday, the 05. February 1990
    "%d-%m-%Y", #07-08-2006
    "%d/%m/%Y", #11/12/1988
    "%d-%m/%y" #30-6/08
]

parsed_dates = []

for date, format in zip(date_lines, format_lines):
    if format:
        try:
            parsed_date = dt.datetime.strptime(date, format)
            parsed_dates.append(parsed_date)
        except ValueError:
            #If there's an issue with parsing, append None
            parsed_dates.append(None)
    else:  
        # Will happen in the first title line 'Datum Chaos:'
        parsed_dates.append(None)

print(parsed_dates)

formatted_dates = [
    date.strftime("%d.%m.%Y") if date else None for date in parsed_dates
]

print(formatted_dates)

# Exercise 4)
# Save the formatted dates to a new file.

with open('Datumsformatums.txt', 'w') as file:
    for date in formatted_dates:
        if date:
            file.write(date + '\n')

# Exercise 5)
# Write a new script with the following requirements:
# - Every input must be through the console.
# - The input must be:
# o Name
# o Favourite colour
# o Favourite animal
# - Save this information in a readable format to .txt and as .csv.
# - The .csv file should be easily readable with excel.
# Hint: In .csv, you must pay attention to the delimiter!
# Exercise Stadt Land Fluss)
# Write a program to play Stadt Land Fluss! The following requirements should be fulfilled:
# - A nice and pretty greeting in the console.
# - Questions for input of the game:
# o Letter
# o Name
# o City
# o Country
# o River
# o Fruit
# o Vegetable
# o Colour
# o Something of your choosing
# - The result should be output in a .txt file in a subdirectory of your project. The result should
# include:
# o Name
# o Letter
# o Inputs
# o Time from the first question (city) to the end of the questions.
# o Please display the time in a readable format.
# o Check if you are faster than 1 minute and include the result in the output.
# o Pay attention to a pleasant presentation when outputting the results.
# Important: Please refrain from implementing any checks. This will be an exercise next week after
# queries have been covered.
# Exercise Stadt Land Fluss_2)
# Play together with other people!
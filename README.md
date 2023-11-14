SUMMARY:

What is the purpose of the application?

📊 It manages family expenses occurred in a month, serving as a console-based program.
   
An expense contains the following details:
   - 🆔 id
   - 📅 day (of the month)
   - 💵 amount
   - 📁 type of expense (food, utilities, clothes, phone, maintenance, others)

The application is able to perform the following functionalities on the list of expenses:
   - ➕ Add:
     - Add new expense.
     - Update an existing expense.
   - ➖ Remove:
     - Delete expenses occurred in a specified day.
     - Delete expenses occurred in a range of days.
     - Delete expenses of a specified category.
   - 🔍 Search:
     - Print expenses that are greater than a specified value.
     - Print expenses that are greater than a specified value and are before a specified day.
     - Print expenses of a specified category.
   - 📰 Reports:
     - Return the sum of all expenses of a specified category.
     - Return the day with the maximum amount of total expenses.
     - Return all expenses that are equal to a specified value.
     - Return expenses sorted by category.
   - 🕵️‍♂️ Filter:
     - Remove all expenses of a specified category.
     - Remove all expenses that are smaller than a specified value.



REFERENCES:

domain_functions FILE:

Functions that modify/print the list containing all expenses:
- Line   4 -  25: Add functions
- Line  28 -  57: Remove functions
- Line  60 -  89: Search functions
- Line  92 - 128: Reports functions
- Line 131 - 149: Filter functions

test_function FILE:

Test functions that check the validity of various variables:
- Line   4 -  18: Checks the validity of 'day' variable
- Line  22 -  35: Checks the validity of 'total' variable
- Line  39 -  54: Checks the validity of 'type_p' variable
- Line  58 -  72: Checks the validity of 'id_p' variable
- Line  75 -  89: Checks the validity of 'num' variable
- Line  92 - 106: Checks the validity of 'response' variable
- Line 109 - 141: Checks the validity of a new expense(id, day, total, category) and adds it to the 'user_expenses' list

user_interface FILE:

Submenus for the console application. Used for verifying variable validity and calling functions:
- Line   7 -  36: First submenu (Add menu)
- Line  40 -  72: Second submenu (Remove menu)
- Line  75 - 107: Third submenu (Search menu)
- Line 110 - 144: Fourth submenu (Reports menu)
- Line 147 - 172: Fifth submenu (Filter menu)
- Line 175 - 183: Start menu
- Line 186 - 225: Main menu
- Line 228 - 250: End menu

main FILE:
- Line      5: Imports all UI menus
- Line 8 - 13: Creates an empty list and performs the entire console application using the main menus

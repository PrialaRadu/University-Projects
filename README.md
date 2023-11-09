SUMMARY:

What is the purpose of the application?
   - It manages family expenses incurred in a month, serving as a console-based program.
   - An expense contains the following details:
      - id
      - day (of the month)
      - amount
      - type of expense (food, utilities, clothes, phone, others, maintenance)
   - The application is able to perform the following functionalities on the list of expenses:
      - Add
      - Remove
      - Search
      - Reports
      - Filter



REFERENCES:

Functions that modify/print the list containing all expenses:
- Line 4 - 25: Add functions
- Line 28 - 57: Remove functions
- Line 60 - 89: Search functions
- Line 92 - 128: Reports functions
- Line 131 - 149: Filter functions

Test functions that check the validity of various variables:
- Line 153 - 166: Checks the validity of 'day' variable
- Line 169 - 182: Checks the validity of 'total' variable
- Line 185 - 200: Checks the validity of 'type_p' variable
- Line 203 - 217: Checks the validity of 'id_p' variable
- Line 220 - 233: Checks the validity of 'num' variable
- Line 236 - 249: Checks the validity of 'response' variable

Submenus for the console application. Used for verifying variable validity and calling functions:
- Line 253 - 282: First submenu (Add menu)
- Line 285 - 316: Second submenu (Remove menu)
- Line 319 - 350: Third submenu (Search menu)
- Line 353 - 386: Fourth submenu (Reports menu)
- Line 389 - 413: Fifth submenu (Filter menu)

The main menu for the console application. Used for calling submenus:
- Line 416 - 450

The end menu for the console application. Used for exiting or restarting the main menu:
- Line 453 - 466

Main program. Used for defining the list containing all expenses and calling the main menu and end menu:
- Line 469 - 479

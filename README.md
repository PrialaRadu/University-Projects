SUMMARY:

What is the purpose of the application?
   It manages family expenses incurred in a month, as a console application.
   An expense contains the following details:
      - id
      - day (of the month)
      - amount
      - type of expense (food, utilities, clothes, phone, others, maintenance)
   The applications is able to perform the following functionalities on the list of expenses:
      - Add
      - Remove
      - Search
      - Reports
      - Filter



References:

Line 4 - 149: Functions that modify/print the list containing all expenses.
   line 4 - 25: Add functions
   line 28 - 57: Remove functions
   line 60 - 89: Search functions
   line 92 - 128: Reports functions
   line 131 - 149: Filter functions

Line 152 - 249: Test functions that check the validity of various variables.
   line 153 - 166: Checks the validity of 'day' variable
   line 169 - 182: Checks the validity of 'total' variable
   line 185 - 200: Checks the validity of 'type_p' variable
   line 203 - 217: Checks the validity of 'id_p' variable
   line 220 - 233: Checks the validity of 'num' variable
   line 236 - 249: Checks the validity of 'response' variable

Line 252 - 413: Submenus for the console application. Used for verifying variable validity and calling functions.
   line 253 - 282: First submenu (Add menu)
   line 285 - 316: Second submenu (Remove menu)
   line 319 - 350: Third submenu (Search menu)
   line 353 - 386: Fourth submenu (Reports menu)
   line 389 - 413: Fifth submenu (Filter menu)

Line 416 - 450: The main menu for the console application. Used for calling submenus.

Line 453 - 466: The end menu for the console application. Used for exiting or restarting the main menu.

Line 469 - 479: Main program. Used for defining the list containing all expenses and calling the main menu and end menu.

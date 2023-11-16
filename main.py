# Family Expenses. Console Application


# Imports the functions that act as menus
from project.ui.user_interface import start_menu, main_menu, end_menu

# Imports the functions that get/validate/test details of expenses
from project.variables.test_variables import *

# Imports the functions that test all functionalities of the console application
from project.functionalities.test_functions import *


if __name__ == '__main__':

    # Test all possible variables and functionalities of the console application
    test_all_variables()
    test_all_functionalities()

    # Create an empty dictionary
    user_expenses = dict()

    # Start the console application using UI functions
    start_menu(user_expenses)
    main_menu(user_expenses)
    end_menu(user_expenses)

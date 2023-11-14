# Family Expenses Console Application


# Imports the functions that act as menus
from user_interface import start_menu, main_menu, end_menu


if __name__ == '__main__':
    user_expenses = list()

    start_menu(user_expenses)
    main_menu(user_expenses)
    end_menu(user_expenses)

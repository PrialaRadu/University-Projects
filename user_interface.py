# UI

from project.functionalities.domain_functions import *
from project.variables.validate_variables import *


# Add menu
def menu1(expenses):
    """
    The function acts as a submenu (Add menu) for the console application.
    Used for calling the following functions:
       - add_new_expense(expenses, day, total, type_p)
       - update_expense(expenses, id, [id, new_day, new_total, new_type])
    Handles all possible errors.
    Can return the user back to the main menu, if needed.
    :return: No return
    """
    print("1 - Add new expense. \n"
          "2 - Update expense. \n"
          "0 - Go back. \n")
    resp = validate_response(0, 2)

    if resp == 0:
        main_menu(expenses)

    elif resp == 1:
        user_day = validate_day_variable()
        user_total = validate_total_variable()
        user_type_p = validate_category_variable()
        add_new_expense(expenses, user_day, user_total, user_type_p)

    elif resp == 2:
        user_id_p = validate_id_p_variable(expenses)
        user_day = validate_day_variable()
        user_total = validate_total_variable()
        user_type_p = validate_category_variable()
        update_expense(expenses, user_id_p, [user_id_p, user_day, user_total, user_type_p])


# Remove menu
def menu2(expenses):
    """
    The function acts as a submenu (Remove menu) for the console application.
    Used for calling the following functions:
       - delete_expenses_in_day(expenses, day)
       - delete_expenses_in_days_range(expenses, start_day, end_day)
       - delete_expenses_of_type(expenses, type_p)
    Handles all possible errors.
    Can return the user back to the main menu, if needed.
    :return: No return
    """
    print("1 - Delete expenses in a day. \n"
          "2 - Delete expenses in a range of days. \n"
          "3 - Delete expenses of a category. \n"
          "0 - Go back. \n")
    resp = validate_response(0, 3)

    if resp == 0:
        main_menu(expenses)

    elif resp == 1:
        user_day = validate_day_variable()
        delete_expenses_in_day(expenses, user_day)

    elif resp == 2:
        user_start_day = validate_day_variable()
        user_end_day = validate_day_variable()
        delete_expenses_in_days_range(expenses, user_start_day, user_end_day)

    elif resp == 3:
        user_type_p = validate_category_variable()
        delete_expenses_of_category(expenses, user_type_p)


# Search menu
def menu3(expenses):
    """
    The function acts as a submenu (Search menu) for the console application.
    Used for calling the following functions:
       - print_expenses_greater_than_num(expenses, num)
       - print_exp_gr_than_num_before_day(expenses, day, num)
       - print_all_expenses_of_type(expenses, type_p)
    Handles all possible errors.
    Can return the user back to the main menu, if needed.
    :return: No return
    """
    print("1 - Print all expenses greater than a value. \n"
          "2 - Print all expenses before a certain day, smaller than a value. \n"
          "3 - Print all expenses of a certain category. \n"
          "0 - Go back. \n")
    resp = validate_response(0, 3)

    if resp == 0:
        main_menu(expenses)

    elif resp == 1:
        user_num = validate_num_variable()
        print(return_expenses_greater_than_num(expenses, user_num))

    elif resp == 2:
        user_day = validate_day_variable()
        user_num = validate_num_variable()
        print(return_exp_gr_than_num_before_day(expenses, user_day, user_num))

    elif resp == 3:
        user_type_p = validate_category_variable()
        print(return_all_expenses_of_category(expenses, user_type_p))


# Reports menu
def menu4(expenses):
    """
    The function acts as a submenu (Reports menu) for the console application.
    Used for calling the following functions:
       - print_expenses_greater_than_num(expenses, num)
       - print_exp_gr_than_num_before_day(expenses, day, num)
       - print_all_expenses_of_type(expenses, type_p)
    Handles all possible errors.
    Can return the user back to the main menu, if needed.
    :return: No return
    """
    print("1 - Print the total sum of expenses of a certain category. \n"
          "2 - Find the day with the maximum amount of expenses. \n"
          "3 - Print all expenses that are equal to a number. \n"
          "4 - Print all expenses sorted by the category. \n"
          "0 - Go back. ")
    resp = validate_response(0, 4)

    if resp == 0:
        main_menu(expenses)

    elif resp == 1:
        user_type_p = validate_category_variable()
        print(return_sum_of_category(expenses, user_type_p))

    elif resp == 2:
        print(f"Day {return_day_of_sum_max(expenses)} has the maximum amount of expenses! ")

    elif resp == 3:
        user_num = validate_num_variable()
        print(return_exp_equal_to_num(expenses, user_num))

    elif resp == 4:
        print(return_exp_sorted_by_category(expenses))


# Filter menu
def menu5(expenses):
    """
    The function acts as a submenu (Filter menu) for the console application.
    Used for calling the following functions:
       - remove_exp_based_on_type(expenses, type_p)
       - remove_exp_smaller_than_sum(expenses, num)
    Handles all possible errors.
    Can return the user back to the main menu, if needed.
    :return: No return
    """
    print("1 - Remove all expenses of a certain category. \n"
          "2 - Remove all expenses smaller than a value. \n"
          "0 - Go back. ")
    resp = validate_response(0, 2)

    if resp == 0:
        main_menu(expenses)

    elif resp == 1:
        user_type_p = validate_category_variable()
        remove_exp_based_on_category(expenses, user_type_p)

    elif resp == 2:
        user_num = validate_num_variable()
        remove_exp_smaller_than_num(expenses, user_num)


# Start menu
def start_menu(expenses):
    """
    The function acts a start menu for the console application.
    Prints a starting message and calls the 'get_user_expenses' function
    :return: No return
    """
    print("Consider adding at least one expense. ")
    get_user_expenses(expenses)


# Main menu
def main_menu(expenses):
    """
    The function acts as a main menu for the console application.
    Used for calling the following submenus:
       - menu1()
       - menu2()
       - menu3()
       - menu4()
       - menu5()
    Handles all possible errors using 'validate_response()' function.
    :return: No return
    """
    print("1 - Add expense. \n"
          "2 - Remove expense. \n"
          "3 - Search expense. \n"
          "4 - Reports on expenses. \n"
          "5 - Filter expenses. \n"
          "0 - Go back. ")
    resp = validate_response(1, 5)

    if resp == 1:
        menu1(expenses)

    elif resp == 2:
        menu2(expenses)

    elif resp == 3:
        menu3(expenses)

    elif resp == 4:
        menu4(expenses)

    elif resp == 5:
        menu5(expenses)

    print()


# End menu
def end_menu(expenses):
    """
    The function acts as an end menu for the console application.
    Used for the following actions:
       - Print and Exit
       - Print and Restart
    Handles all possible errors using 'validate_response()' function.
    :return: No return
    """
    print("1 - Print all expenses and EXIT THE MENU. \n"
          "2 - Print all expenses and RESTART THE MENU. \n")
    resp = validate_response(1, 2)

    print_expenses(expenses)

    if resp == 1:
        pass

    elif resp == 2:
        print()
        main_menu(expenses)


def print_expenses(expenses):
    print(expenses)

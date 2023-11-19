# Domain
from project.variables.get_variables import *


# 1 Add Functions
def add_new_expense(expenses, day, total, category):
    """
    The function adds a new expense to the dict 'expenses'.
    :param expenses: The dictionary that contains all expenses
    :param day: Expense day
    :param total: Total expense.
    :param category: Expense category
    :return: No return
    """
    expenses[get_length(expenses) + 1] = {'day': day, 'total': total, 'category': category}


def update_expense(expenses, id_p, new_exp):
    """
    The function updates an expense from the dict 'expenses' with new value/values.
    :param expenses: The dictionary that contains all expenses
    :param id_p: Expense ID
    :param new_exp: The new expense values, in format: id: {'day': new_day, 'total': new_total, 'category': new_type}
    :return: No return
    """
    expenses[id_p] = new_exp


# 2 Remove functions
def delete_expenses_in_day(expenses, day):
    """
    The function deletes expenses in a specified day.
    :param expenses: The dictionary containing all expenses
    :param day: Expense day
    :return: No return
    """
    to_be_removed = [key for key, value in expenses.items() if get_day(value) == day]

    for key in to_be_removed:
        del expenses[key]

    refactor_ids(expenses)


def delete_expenses_in_days_range(expenses, start_day, end_day):
    """
    The function deletes expenses in a specified range of days.
    :param expenses: The dictionary containing all expenses
    :param start_day: Starting day of range
    :param end_day: Ending day of range
    :return: No return
    """
    to_be_removed = [key for key, value in expenses.items() if start_day <= get_day(value) <= end_day]

    for key in to_be_removed:
        del expenses[key]

    refactor_ids(expenses)


def delete_expenses_of_category(expenses, category):
    """
    The function deletes expenses of a specified category.
    :param expenses: The dictionary containing all expenses
    :param category: Expense category
    :return: No return
    """
    to_be_removed = [key for key, value in expenses.items() if get_category(value) == category]

    for key in to_be_removed:
        del expenses[key]

    refactor_ids(expenses)


# 3 Search functions
def return_expenses_greater_than_num(expenses, num):
    """
    The function returns all expenses that are greater than a specified number.
    :param expenses: The dictionary containing all expenses
    :param num: The number used for comparison
    :return: Returns a new dictionary, with expenses that are greater than 'num'.
    """
    new_dict = {}
    for key, value in expenses.items():
        if get_total(value) > num:
            new_dict.update({key: value})
    return new_dict


def return_exp_gr_than_num_before_day(expenses, day, num):
    """
    The function returns all expenses that are greater than a specified number and are before a specified day.
    :param expenses: The dictionary containing all expenses
    :param day: Expense day
    :param num: The number used for comparison
    :return: Returns a new dictionary, containing expenses that are greater than 'num' and are after 'day'.
    """
    new_dict = {}
    for key, value in expenses.items():
        if get_total(value) > num and get_day(value) < day:
            new_dict.update({key: value})
    return new_dict


def return_all_expenses_of_category(expenses, category):
    """
    The function returns all expenses of a specified category.
    :param expenses: The dictionary containing all expenses
    :param category: Expense category
    :return: Returns a new dictionary, containing expenses that are of a specified category.
    """
    new_dict = {}
    for key, value in expenses.items():
        if get_category(value) == category:
            new_dict.update({key: value})
    return new_dict


# 4 Reports functions
def return_sum_of_category(expenses, category):
    """
    The function returns the sum of all expenses of a specified category.
    :param expenses: The dictionary containing all expenses
    :param category: Expense category
    :return: Returns the sum of all expenses of a specified category.
    """
    return sum(get_total(value) for key, value in expenses.items() if get_category(value) == category)


def return_day_of_sum_max(expenses):
    """
    The function returns the day with the maximum amount of total expenses.
    :param expenses: The dictionary containing all expenses
    :return: Returns the day with the maximum value of total expenses.
    """
    return max(range(1, 32), key=lambda x: sum(get_total(val) for key, val in expenses.items() if get_day(val) == x))


def return_exp_equal_to_num(expenses, num):
    """
    The function returns all expenses that are equal to a specified number.
    :param expenses: The dictionary containing all expenses
    :param num: The number used for comparison
    :return: Returns all expenses that are equal to a specified number.
    """
    new_dict = {}
    for key, value in expenses.items():
        if get_total(value) == num:
            new_dict.update({key: value})
    return new_dict


def return_exp_sorted_by_category(expenses):
    """
    The function returns expenses sorted by 'category'.
    :param expenses: The dictionary containing all expenses
    :return: Returns expenses sorted by 'category'.
    """
    sorted_expenses = sorted(expenses.items(), key=lambda x: get_category(x[1]))
    return dict(sorted_expenses)


# 5 Filter functions
def remove_exp_based_on_category(expenses, category):
    """
    The function removes all expenses of a specified category.
    :param expenses: The dictionary containing all expenses
    :param category: Expense category
    :return: No return
    """
    to_be_removed = [key for key, value in expenses.items() if get_category(value) == category]

    for key in to_be_removed:
        del expenses[key]

    refactor_ids(expenses)


def remove_exp_smaller_than_num(expenses, num):
    """
    The function removes all expenses that are smaller than a specified number.
    :param expenses: The dictionary containing all expenses
    :param num: The number user for comparison
    :return: No return
    """
    to_be_removed = [key for key, value in expenses.items() if get_total(value) < num]

    for key in to_be_removed:
        del expenses[key]

    refactor_ids(expenses)


# Function that updates IDs (if one or more expenses were deleted)
def refactor_ids(expenses):
    """
    The function updates all IDs (if one or more expenses were deleted)
    :param expenses: The dictionary containing all expenses
    :return: No return
    """
    pos = 1
    for key in list(expenses):
        if key != pos:
            expenses[pos] = expenses.pop(key)
        pos += 1

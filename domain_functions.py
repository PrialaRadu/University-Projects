# Domain


# 1 Add Functions
def add_new_expense(expenses, day, total, type_p):
    """
    The function adds a new expense to the list 'expenses'.
    :param expenses: The list that contains all expenses
    :param day: Expense day
    :param total: Total expense.
    :param type_p: Expense category
    :return: No return
    """
    expenses.append([len(expenses) + 1, day, total, type_p])


def update_expense(expenses, id_p, new_exp):
    """
    The function updates an expense from the list 'expenses' with new value/values.
    :param expenses: The list that contains all expenses
    :param id_p: Expense ID
    :param new_exp: The new expense values, in format: [id, new_day, new_total, new_type]
    :return: No return
    """
    expenses[id_p - 1] = [val for exp in expenses if exp[0] == id_p for val in new_exp]


# 2 Remove functions
def delete_expenses_in_day(expenses, day):
    """
    The function deletes expenses in a specified day.
    :param expenses: The list containing all expenses
    :param day: Expense day
    :return: No return
    """
    expenses[:] = [exp for exp in expenses if exp[1] != day]


def delete_expenses_in_days_range(expenses, start_day, end_day):
    """
    The function deletes expenses in a specified range of days.
    :param expenses: The list containing all expenses
    :param start_day: Starting day of range
    :param end_day: Ending day of range
    :return: No return
    """
    expenses[:] = [exp for exp in expenses if exp[1] < start_day or exp[1] > end_day]


def delete_expenses_of_type(expenses, type_p):
    """
    The function deletes expenses of a specified category.
    :param expenses: The list containing all expenses
    :param type_p: Expense category
    :return: No return
    """
    expenses[:] = [exp for exp in expenses if exp[3] != type_p]


# 3 Search functions
def print_expenses_greater_than_num(expenses, num):
    """
    The function returns all expenses that are greater than a specified number.
    :param expenses: The list containing all expenses
    :param num: The number used for comparison
    :return: Returns a new list, with expenses that are greater than 'num'.
    """
    return [exp for exp in expenses if exp[2] > num]


def print_exp_gr_than_num_before_day(expenses, day, num):
    """
    The function returns all expenses that are greater than a specified number and are before a specified day.
    :param expenses: The list containing all expenses
    :param day: Expense day
    :param num: The number used for comparison
    :return: Returns a new list, containing expenses that are greater than 'num' and are after 'day'.
    """
    return [exp for exp in expenses if exp[1] < day and exp[2] < num]


def print_all_expenses_of_type(expenses, type_p):
    """
    The function returns all expenses of a specified category.
    :param expenses: The list containing all expenses
    :param type_p: Expense category
    :return: Returns a new list, containing expenses that are of a specified category.
    """
    return [exp for exp in expenses if exp[3] == type_p]


# 4 Reports functions
def print_sum_of_types(expenses, type_p):
    """
    The function returns the sum of all expenses of a specified category.
    :param expenses: The list containing all expenses
    :param type_p: Expense category
    :return: Returns the sum of all expenses of a specified category.
    """
    return sum(exp[2] for exp in expenses if exp[3] == type_p)


def find_day_of_sum_max(expenses):
    """
    The function returns the day with the maximum amount of total expenses.
    :param expenses: The list containing all expenses
    :return: Returns the day with the maximum value of total expenses.
    """
    return max(range(1, 32), key=lambda x: sum(exp[2] for exp in expenses if exp[1] == x))


def print_exp_equal_to_sum(expenses, num):
    """
    The function returns all expenses that are equal to a specified number.
    :param expenses: The list containing all expenses
    :param num: The number used for comparison
    :return: Returns all expenses that are equal to a specified number.
    """
    return [exp for exp in expenses if exp[2] == num]


def print_exp_sorted_by_type(expenses):
    """
    The function returns expenses sorted by 'category'.
    :param expenses: The list containing all expenses
    :return: Returns expenses sorted by 'category'.
    """
    return sorted(expenses, key=lambda x: x[3])


# 5 Filter functions
def remove_exp_based_on_type(expenses, type_p):
    """
    The function removes all expenses of a specified category.
    :param expenses: The list containing all expenses
    :param type_p: Expense category
    :return: No return
    """
    expenses[:] = [exp for exp in expenses if exp[3] != type_p]


def remove_exp_smaller_than_sum(expenses, num):
    """
    The function removes all expenses that are smaller than a specified number.
    :param expenses: The list containing all expenses
    :param num: The number user for comparison
    :return: No return
    """
    expenses[:] = [exp for exp in expenses if exp[2] > num]

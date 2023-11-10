# P3. Family Expenses


# 1 Add
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


# 2 Remove
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


# 3 Search
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


# 4 Reports
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


# 5 Filter
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


# TEST FUNCTIONS
def validate_day_variable():
    """
    The function continuously prompts the user to input a day value and ensures that the input is a valid integer.
    If the input is valid, the function returns the valid day value.
    If the input is invalid, it catches exceptions and prints the corresponding error message.
    :return: Returns the valid day.
    """
    while True:
        try:
            day = int(input("Type the day: "))
            assert 1 <= day <= 31, "Invalid value for day. Please type a value between 1 and 31!"
            return day
        except (ValueError, AssertionError) as e:
            print(e)


def validate_total_variable():
    """
    The function continuously prompts the user to input a total value and ensures that the input is a valid float num.
    If the input is valid, the function returns the valid total value.
    If the input is invalid, it catches exceptions and prints the corresponding error message.
    :return: Returns the valid total.
    """
    while True:
        try:
            total = float(input("Type the total expense: "))
            assert total > 0, "Invalid value for total expense. Type a value greater than 0!"
            return total
        except (ValueError, AssertionError) as e:
            print(e)


def validate_type_p_variable():
    """
    The function continuously prompts the user to input a category and ensures that the input is a valid string.
    If the input is valid, the function returns the valid category string.
    If the input is invalid, it catches exceptions and prints the corresponding error message.
    :return: Returns the valid category.
    """
    while True:
        try:
            type_p = str(input("Type the category (food, utilities, clothes, phone, maintenance, others): "))
            categories = ["food", "utilities", "clothes", "phone", "others", "maintenance"]
            invalid_mes = "Invalid value for category! (food, utilities, clothes, phone, maintenance, others) "
            assert type_p in categories, invalid_mes
            return type_p
        except (ValueError, AssertionError) as e:
            print(e)


def validate_id_p_variable():
    """
    The function continuously prompts the user to input an id and ensures that the input is a valid integer.
    If the input is valid, the function returns the valid id.
    If the input is invalid, it catches exceptions and prints the corresponding error message.
    :return: Returns the valid id.
    """
    while True:
        try:
            id_p = int(input("Type the id of the expense you want do modify: "))
            invalid_mes = f"Invalid id. Type a value between 1 and {len(user_expenses)}!"
            assert 1 <= id_p <= len(user_expenses), invalid_mes
            return id_p
        except (ValueError, AssertionError) as e:
            print(e)


def validate_num_variable():
    """
    The function continuously prompts the user to input a value and ensures that the input is a valid number.
    If the input is valid, the function returns the valid number.
    If the input is invalid, it catches exceptions and prints the corresponding error message.
    :return: Returns the valid number.
    """
    while True:
        try:
            num = float(input("Type the value: "))
            assert num > 0, "Invalid value. Type a value greater than 0 !"
            return num
        except (ValueError, AssertionError) as e:
            print(e)


def validate_response(start, end):
    """
    The function continuously prompts the user to input a response and ensures that the input is a valid number.
    If the input is valid, the function returns the valid response.
    If the input is invalid, it catches exceptions and prints the corresponding error message.
    :return: Returns the valid response.
    """
    while True:
        try:
            resp = int(input())
            assert start <= resp <= end, f"Invalid response. Type a value between {start} and {end}!"
            return resp
        except (ValueError, AssertionError) as e:
            print(e)


# SUBMENUS
def menu1():
    """
    The function acts as a submenu (Add menu) for the console application.
    Used for calling the following functions:
       - add_new_expense(expenses, day, total, type_p)
       - update_expense(expenses, id, [id, new_day, new_total, new_type])
    Handles all possible errors.
    Can return the user back to the main menu, if needed.
    :return: No return
    """
    print("1 - Add new expense \n"
          "2 - Update expense \n"
          "0 - Go back \n")
    resp = validate_response(0, 2)

    if resp == 0:
        menu()

    elif resp == 1:
        user_day = validate_day_variable()
        user_total = validate_total_variable()
        user_type_p = validate_type_p_variable()
        add_new_expense(user_expenses, user_day, user_total, user_type_p)

    elif resp == 2:
        user_id_p = validate_id_p_variable()
        user_day = validate_day_variable()
        user_total = validate_total_variable()
        user_type_p = validate_type_p_variable()
        update_expense(user_expenses, user_id_p, [user_id_p, user_day, user_total, user_type_p])


def menu2():
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
    print("1 - Delete expenses in a day: \n"
          "2 - Delete expenses in a range of days: \n"
          "3 - Delete expenses of a category: \n"
          "0 - Go back \n")
    resp = validate_response(0, 3)

    if resp == 0:
        menu()

    elif resp == 1:
        user_day = validate_day_variable()
        delete_expenses_in_day(user_expenses, user_day)

    elif resp == 2:
        user_start_day = validate_day_variable()
        user_end_day = validate_day_variable()
        delete_expenses_in_days_range(user_expenses, user_start_day, user_end_day)

    elif resp == 3:
        user_type_p = validate_type_p_variable()
        delete_expenses_of_type(user_expenses, user_type_p)


def menu3():
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
    print("1 - Print all expenses greater than a value \n"
          "2 - Print all expenses before a certain day, smaller than a value \n"
          "3 - Print all expenses of a certain category \n"
          "0 - Go back \n")
    resp = validate_response(0, 3)

    if resp == 0:
        menu()

    elif resp == 1:
        user_num = validate_num_variable()
        print(print_expenses_greater_than_num(user_expenses, user_num))

    elif resp == 2:
        user_day = validate_day_variable()
        user_num = validate_num_variable()
        print(print_exp_gr_than_num_before_day(user_expenses, user_day, user_num))

    elif resp == 3:
        user_type_p = validate_type_p_variable()
        print(print_all_expenses_of_type(user_expenses, user_type_p))


def menu4():
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
    print("1 - Print the total sum of expenses of a certain category \n"
          "2 - Find the day with the maximum amount of expenses \n"
          "3 - Print all expenses that are equal to a number \n"
          "4 - Print all expenses sorted by the category \n"
          "0 - Go back")
    resp = validate_response(0, 4)

    if resp == 0:
        menu()

    elif resp == 1:
        user_type_p = validate_type_p_variable()
        print(print_sum_of_types(user_expenses, user_type_p))

    elif resp == 2:
        print(f"Day {find_day_of_sum_max(user_expenses)} has the maximum amount of expenses")

    elif resp == 3:
        user_num = validate_num_variable()
        print(print_exp_equal_to_sum(user_expenses, user_num))

    elif resp == 4:
        print(print_exp_sorted_by_type(user_expenses))


def menu5():
    """
    The function acts as a submenu (Filter menu) for the console application.
    Used for calling the following functions:
       - remove_exp_based_on_type(expenses, type_p)
       - remove_exp_smaller_than_sum(expenses, num)
    Handles all possible errors.
    Can return the user back to the main menu, if needed.
    :return: No return
    """
    print("1 - Remove all expenses of a certain category \n"
          "2 - Remove all expenses smaller than a value \n"
          "0 - Go back")
    resp = validate_response(0, 2)

    if resp == 0:
        menu()

    elif resp == 1:
        user_type_p = validate_type_p_variable()
        remove_exp_based_on_type(user_expenses, user_type_p)

    elif resp == 2:
        user_num = validate_num_variable()
        remove_exp_smaller_than_sum(user_expenses, user_num)


def menu():
    """
    The function acts as a main menu for the console application.
    Used for calling the following submenus:
       - menu1()
       - menu2()
       - menu3()
       - menu4()
       - menu5()
    Handles all possible errors.
    :return: No return
    """
    print("1 - Add expense \n"
          "2 - Remove expense \n"
          "3 - Search expense \n"
          "4 - Reports on expenses \n"
          "5 - Filter expenses \n")
    resp = validate_response(1, 5)

    if resp == 1:
        menu1()

    elif resp == 2:
        menu2()

    elif resp == 3:
        menu3()

    elif resp == 4:
        menu4()

    elif resp == 5:
        menu5()

    print()


def end_menu():
    print("1 - Print all expenses and EXIT THE MENU \n"
          "2 - Print all expenses and RESTART THE MENU \n")
    resp = validate_response(1, 2)

    if resp == 1:
        for user_exp in user_expenses:
            print(user_exp)

    elif resp == 2:
        for user_exp in user_expenses:
            print(user_exp)
        print()
        menu()


if __name__ == '__main__':
    user_expenses = [[1,  3, 131, "food"],
                     [2,  7,  86, "phone"],
                     [3, 11,  31, "food"],
                     [4, 13,  25, "maintenance"],
                     [5, 21,  13, "food"],
                     [6, 27, 119, "clothes"],
                     [7, 28, 251, "others"]]

    menu()
    end_menu()

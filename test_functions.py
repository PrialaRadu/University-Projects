# Test functions


# test variable 'day'
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
            assert 1 <= day <= 31, "Invalid value for day. Please type a value between 1 and 31! "
            return day
        except (ValueError, AssertionError) as e:
            print(e)


# test variable 'total'
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
            assert total > 0, "Invalid value for total expense. Type a value greater than 0! "
            return total
        except (ValueError, AssertionError) as e:
            print(e)


# test variable 'type_p'
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


# test variable id
def validate_id_p_variable(exps):
    """
    The function continuously prompts the user to input an id and ensures that the input is a valid integer.
    If the input is valid, the function returns the valid id.
    If the input is invalid, it catches exceptions and prints the corresponding error message.
    :return: Returns the valid id.
    """
    while True:
        try:
            id_p = int(input("Type the id of the expense you want do modify: "))
            invalid_mes = f"Invalid id. Type a value between 1 and {len(exps)}! "
            assert 1 <= id_p <= len(exps), invalid_mes
            return id_p
        except (ValueError, AssertionError) as e:
            print(e)


# test 'num' variable
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
            assert num > 0, "Invalid value. Type a value greater than 0! "
            return num
        except (ValueError, AssertionError) as e:
            print(e)


# test 'response' variable
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
            assert start <= resp <= end, f"Invalid response. Type a value between {start} and {end}! "
            return resp
        except (ValueError, AssertionError) as e:
            print(e)


# Get user input
def get_user_expenses(expenses):
    """
    Continuously prompts the user to input expense details, validates the inputs and stores the expenses in the list
    The function uses the following functions for validation:
        - validate_day_variable
        - validate_total_variable
        - validate_type_p_variable
        - validate_response
    The expenses are stored in the `user_expenses` list as lists containing:
        1. Expense ID (automatically assigned based on the length of `user_expenses`).
        2. Expense day.
        3. Expense total.
        4. Expense type.
    The user is prompted to decide whether to add another expense or modify existing ones.
    Return: no return
    """
    while True:
        user_day = validate_day_variable()
        user_total = validate_total_variable()
        user_type_p = validate_type_p_variable()

        expenses.append([len(expenses) + 1, user_day, user_total, user_type_p])

        print(f"\nExpense saved (with ID={len(expenses)}). Do you want to add another one ? \n"
              "1 - Yes, I want to add another expense! \n"
              "2 - No, I want to modify/print my expenses! ")
        resp = validate_response(1, 2)

        if resp == 1:
            pass
        elif resp == 2:
            break

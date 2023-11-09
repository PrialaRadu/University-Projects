# P3. Cheltuieli de familie


# 1 Add
def add_new_expense(expenses, day, total, type_p):
    """
    The function adds a new expense to the list 'expenses'
    :param expenses: The list that contains all expenses
    :param day: Expense day
    :param total: Total expense
    :param type_p: Expense category
    :return: No return
    """
    expenses.append([len(expenses) + 1, day, total, type_p])

def update_expense(expenses, id, new_exp ):
    """
    The functions updates an expense from the list 'expenses' with new value/values.
    :param expenses: The list that contains all expenses
    :param id: Expense ID
    :param new_exp: The new expense values, in the format: [id, new_day, new_total, new_type]
    :return: No return
    """
    for i in range(0, len(expenses)):
        if expenses[i][0] == old_id:
            expenses[i] = new_exp
# 2 Remove
def delete_expenses_in_day(expenses, day):
    """
    The function delets expenses in a specified day
    :param expenses: The list containing all expenses
    :param day: Expense day
    :return: No return
    """
    expenses[:] = [exp for exp in expenses if exp[1] != day]

def delete_expenses_in_days_range(expenses, sday, fday):
    """
    The function deletes expenses in a specified range of days
    :param expenses: The list containing all expenses
    :param sday: Starting day of range
    :param fday: Ending day of range
    :return: No return
    """
    expenses[:] = [exp for exp in expenses if exp[1] < sday or exp[1] > fday]

def delete_expenses_of_type(expenses, type_p):
    """
    The function deletes expenses of a specified category
    :param expenses: The list containing all expenses
    :param type_p: Expense category
    :return: No return
    """
    expenses[:] = [exp for exp in expenses if exp[3] != type_p]

# 3 Search
def print_expenses_greater_than_num(expenses, num):
    """
    The function returns all expenses that are greater than a specified number
    :param expenses: The list containing all expenses
    :param num: The number used for comparison
    :return: Returns a new list, with expenses that are greater than 'num'
    """
    new_list = []
    for exp in expenses:
        if exp[2] > num:
            new_list.append(exp)
    return new_list

def print_exp_gr_than_num_before_day(expenses, day, num):
    """
    The function returns all expenses that are greater than a specified number and are before a specified day
    :param expenses: The list containing all expenses
    :param day: Expense day
    :param num: The number used for comparison
    :return: Returns a new list, containing expenses that are greater than 'num' and are after 'day'
    """
    new_list = []
    for exp in expenses:
        if exp[1] < day and exp[2] < num:
            new_list.append(exp)
    return new_list

def print_all_expenses_of_type(expenses, type_p):
    """
    The function returns all expenses of a specified category
    :param expenses: The list containing all expenses
    :param type_p: Expense category
    :return: Returns a new list, containing expenses that are of a specified category
    """
    new_list = []
    for exp in expenses:
        if exp[3] == type_p:
            new_list.append(exp)
    return new_list

# 4 Reports
def print_sum_of_types(expenses, type_p):
    """
    The function returns the sum of all expenses of a specified category
    :param expenses: The list containing all expenses
    :param type_p: Expanse category
    :return: Returns the sum of all expenses of a specified category
    """
    sum = 0
    for exp in expenses:
        if exp[3] == type_p:
            sum += exp[2]
    return sum

def find_day_of_sum_max(expenses):
    """
    The function returns the day with the maximum amount of total expenses
    :param expenses: The list containing all expenses
    :return: Returns the day with the maximum value of total expenses
    """
    max, day_max = 0, 0
    for i in range(1, 32):
        sum = 0
        for exp in expenses:
            if exp[1] == i:
               sum += exp[2]
        if sum > max:
            max = sum
            day_max = i
    return day_max

def print_exp_equal_to_sum(expenses, num):
    """
    The function returns all expenses that are equal to a specified number
    :param expenses: The list containing all expenses
    :param num: The number used for comparison
    :return: Returns all expenses that are equal to a specified number
    """
    return [exp for exp in expenses if exp[2] == num ]

def print_exp_sorted_by_type(expenses):
    """
    The function returns expenses sorted by 'category'
    :param expenses: The list containing all expenses
    :return: Returns expenses sorted by 'category'
    """
    new_expenses = sorted(expenses, key=lambda x: x[3])
    return [exp for exp in new_expenses]

# 5 Filter
def remove_exp_based_on_type(expenses, type_p):
    """
    The function removes all expenses of a specified category
    :param expenses: The list containing all expenses
    :param type_p: Expense category
    :return: No return
    """
    expenses[:] = [exp for exp in expenses if exp[3] != type_p]

def remove_exp_smaller_than_sum(expenses, num):
    """
    The function removes all expenses that are smaller than a specified number
    :param expenses: The list containing all expenses
    :param num: The number user for comparison
    :return: No return
    """
    expenses[:] = [exp for exp in expenses if exp[2] > num]

# MENU

def menu1():
    """
    The function acts as a submenu (Add menu) for the console application
    Used for calling the following functions:
       - add_new_expense(expenses, day, total, type_p)
       - update_expense(expenses, id,[id, new_day, new_total, new_type])
    Handles all possible errors
    Can return the user back to the main menu, if needed
    :return: No return
    """
    while True:
        print("1 - Add new expense \n"
              "2 - Update expense \n"
              "0 - Go back \n")
        resp = int(input())

        if resp == 0:
            menu()
            break
        elif resp == 1:
            while True:
                day = int(input("Type the day: "))
                total = int(input("Type the total expense: "))
                type_p = input("Type the category (food, utilities, clothes, phone, maintenance, others): ")
                if day < 1 or day > 31:
                    print("Invalid value for day. Please type a value between 1 and 31 !")
                elif total <= 0:
                    print("Invalid value for total expense. Type a value greater than 0 !")
                elif type_p not in ["food", "utilities", "clothes", "phone", "others", "maintenance"]:
                    print("Invalid value for category. Please type a valid category (food, utilities, clothes, phone, maintenance, others) !")
                else:
                    add_new_expense(expenses, day, total, type_p)
                    break
            break
        elif resp == 2:
            while True:
                id = int(input("Type the id of the expense you want do modify: "))
                new_day = int(input("Type the day (of updated expense): \n"))
                new_total = int(input("Type the total expense (of updated expense): \n"))
                new_type = input("Type the category (food, utilities, clothes, phone, maintenance, others) (of updated expense): \n")

                if id < 1 or old_id > len(expenses):
                    print(f"Invalid id. Please type a value between 1 and {len(expenses)}")
                elif new_day < 1 or new_day > 31:
                    print("Invalid value for day. Please type a value between 1 and 31 !")
                elif new_total <= 0:
                    print("Invalid value for total expense. Type a value greater than 0 !")
                elif new_type not in ["food", "utilities", "clothes", "phone", "others", "maintenance"]:
                    print("Invalid value for category. Please type a valid category (food, utilities, clothes, phone, maintenance, others) !")
                else:
                    update_expense(expenses, id,[id, new_day, new_total, new_type])
                    break
            break

        else:
            print("Invalid Response. Type a value between 1 and 2")

def menu2():
    """
    The function acts as a submenu (Remove menu) for the console application
    Used for calling the following functions:
       - delete_expenses_in_day(expenses, day)
       - delete_expenses_in_days_range(expenses, sday, fday)
       - delete_expenses_of_type(expenses, type_p)
    Handles all possible errors
    Can return the user back to the main menu, if needed
    :return: No return
    """
    while True:
        print("1 - Delete expenses in a day: \n"
              "2 - Delete expenses in a range of days: \n"
              "3 - Delete expenses of a category: \n"
              "0 - Go back \n")
        resp = int(input())

        if resp == 0:
            menu()
            break
        elif resp == 1:
            while True:
                day = int(input("Type the day: "))
                if day < 1 or day > 31:
                    print("Invalid value for day. Please type a value between 1 and 31 !")
                else:
                    delete_expenses_in_day(expenses, day)
                    break
            break

        elif resp == 2:
            while True:
                sday = int(input("Type the starting day in the range you want to delete: \n"))
                fday = int(input("Type the ending day in the range you want to delete: \n"))
                if sday < 1 or sday > 31 or fday < 1 or fday > 31:
                    print("Invalid value for day. Please type a value between 1 and 31 !")
                else:
                    delete_expenses_in_days_range(expenses, sday, fday)
                    break
            break
        elif resp == 3:
            while True:
                type_p = input("Type the category of expenses you want to delete (food, utilities, clothes, phone, others):")
                if type_p not in ["food", "utilities", "clothes", "phone", "others", "maintenace"]:
                    print("Invalid value for category. Please type a valid category (food, utilities, clothes, phone, maintenance, others) !")
                else:
                    delete_expenses_of_type(expenses, type_p)
                    break
            break

        else:
            print("Invalid Response")

def menu3():
    """
    The function acts as a submenu (Search menu) for the console application
    Used for calling the following functions:
       - print_expenses_greater_than_num(expenses, num)
       - print_exp_gr_than_num_before_day(expenses, day, num)
       - print_all_expenses_of_type(expenses, type_p)
    Handles all possible errors
    Can return the user back to the main menu, if needed
    :return: No return
    """
    while True:
        print("1 - Print all expenses greater than a value \n"
              "2 - Print all expenses before a certain day, smaller than a value \n"
              "3 - Print all expenses of a certain category \n"
              "0 - Go back \n")
        resp = int(input())

        if resp == 0:
            menu()
            break
        elif resp == 1:
            while True:
                num = int(input("Type the value: "))
                if num <= 0:
                    print("Invalid value for total expense. Type a value greater than 0 !")
                else:
                    print(print_expenses_greater_than_num(expenses, num))
                    break
            break

        elif resp == 2:
            while True:
                day = int(input("Type the day: \n"))
                num = int(input("Type the value: \n"))
                if day < 1 or day > 31:
                    print("Invalid value for day. Please type a value between 1 and 31 !")
                if num <= 0:
                    print("Invalid value for total expense. Type a value greater than 0 !")
                else:
                    print(print_exp_gr_than_num_before_day(expenses, day, num))
                    break
            break

        elif resp == 3:
            while True:
                type_p = input("Type the payment category: ")
                if type_p not in ["food", "utilities", "clothes", "phone", "others", "maintenance"]:
                    print("Invalid value for category. Please type a valid category (food, utilities, clothes, phone, others) !")
                else:
                    print(print_all_expenses_of_type(expenses, type_p))
                    break
            break
        else:
             print("Invalid Response")

def menu4():
    """
    The function acts as a submenu (Reports menu) for the console application
    Used for calling the following functions:
       - print_expenses_greater_than_num(expenses, num)
       - print_exp_gr_than_num_before_day(expenses, day, num)
       - print_all_expenses_of_type(expenses, type_p)
    Handles all possible errors
    Can return the user back to the main menu, if needed
    :return: No return
    """
    while True:
        print("1 - Print the total sum of expenses of a certain category \n"
              "2 - Find the day with the maximum amount of expenses \n"
              "3 - Print all expenses that are equal to a number \n"
              "4 - Print all expenses sorted by the category \n"
              "0 - Go back")
        resp = int(input())

        if resp == 0:
            menu()
            break
        elif resp == 1:
            while True:
                type_p = input("Type the payment category: ")
                if type_p not in ["food", "utilities", "clothes", "phone", "others", "maintenance"]:
                    print("Invalid value for category. Please type a valid category (food, utilities, clothes, phone, maintenance, others) !")
                else:
                    print(print_sum_of_types(expenses, type_p))
                    break
            break

        elif resp == 2:
            print(f" Day {find_day_of_sum_max(expenses)} has the maximum amount of expenses")
            break

        elif resp == 3:
            while True:
                num = int(input("Type the value: "))
                if num <= 0:
                    print("Invalid value for total expense. Type a value greater than 0 !")
                else:
                    print(print_exp_equal_to_sum(expenses, num))
                    break
            break

        elif resp == 4:
            print(print_exp_sorted_by_type(expenses))
            break

        else:
            print("Invalid Response")


def menu5():
    """
    The function acts as a submenu (Filter menu) for the console application
    Used for calling the following functions:
       - remove_exp_based_on_type(expenses, type_p)
       - remove_exp_smaller_than_sum(expenses, num)
    Handles all possible errors
    Can return the user back to the main menu, if needed
    :return: No return
    """
    while True:
        print("1 - Remove all expenses of a certain category \n"
              "2 - Remove all expenses smaller than a value \n"
              "0 - Go back")
        resp = int(input())

        if resp == 0:
            menu()
            break
        elif resp == 1:
            while True:
                type_p = input("Type the category: ")
                if type_p not in ["food", "utilities", "clothes", "phone", "others", "maintenance"]:
                    print("Invalid value for category. Please type a valid category (food, utilities, clothes, phone, maintenance, others) !")
                else:
                    remove_exp_based_on_type(expenses, type_p)
                    break
            break

        elif resp == 2:
            while True:
                num = int(input("Type the value: "))
                if num <= 0:
                    print("Invalid value for total expense. Type a value greater than 0 !")
                else:
                    remove_exp_smaller_than_sum(expenses, num)
                    break
            break

        else:
            print("Invalid Response")

def menu():
    """
    The function acts as a main menu for the console application
    Used for calling the following submenus:
       - menu1()
       - menu2()
       - menu3()
       - menu4()
       - menu5()
    Handles all possible errors

    :return: No return
    """
    while True:
        print("1 - Add expense\n"
              "2 - Remove expense\n"
              "3 - Search expense\n"
              "4 - Reports on expenses\n"
              "5 - Filter expenses\n")
        resp = int(input())

        if resp == 1:
            menu1()
            break

        elif resp == 2:
            menu2()
            break

        elif resp == 3:
            menu3()
            break

        elif resp == 4:
            menu4()
            break

        elif resp == 5:
            menu5()
            break

        else:
            print("Invalid Response. Type a valid response (value between 1 and 5):")

    print()



if __name__ == '__main__':
    expenses = [[1,  3, 131, "food"],
                [2,  7,  86, "phone"],
                [3, 11,  31, "food"],
                [4, 13,  25, "maintenance"],
                [5, 21,  13, "food"],
                [6, 27, 119, "clothes"],
                [7, 28, 251, "others"]]

    while True:
        print()
        menu()
        response = int(input("1 - Print all expenses and EXIT THE MENU \n"
                             "2 - Print all expenses and RESTART THE MENU\n"))
        if response == 1:
            for exp in expenses:
                print(exp)
            break
        elif response == 2:
            for exp in expenses:
                print(exp)


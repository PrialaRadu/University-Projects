# Test functions that check the integrity of every functionality that prints/modifies the expenses dictionary

from project.functionalities.domain_functions import *
from project.variables.get_variables import *


def expenses_example():
    return {1: {'day': 7,
                'total': 155.49,
                'category': 'food'},
            2: {'day': 11,
                'total': 54.77,
                'category': 'phone'},
            3: {'day': 26,
                'total': 329.03,
                'category': 'utilities'}}


# Testing 'Add' functions
def test_add_new_expense():
    # Test case 1
    expenses = expenses_example()
    add_new_expense(expenses, 13, 57, 'food')
    assert get_length(expenses) == 4, 'Expenses dictionary should have four items after adding'
    exp = {'day': 13, 'total': 57, 'category': 'food'}
    assert get_expense(expenses, 4) == exp, 'New expense should be added correctly'

    # Test case 2
    add_new_expense(expenses, 19, 30.53, 'utilities')
    assert get_length(expenses) == 5, 'Expenses dictionary should have five items after adding'
    exp = {'day': 19, 'total': 30.53, 'category': 'utilities'}
    assert get_expense(expenses, 5) == exp, 'New expense should be added correctly'


def test_update_expense():
    # Test case 1
    expenses = expenses_example()
    new_exp = {'day': 7, 'total': 130, 'category': 'food'}
    update_expense(expenses, 1, new_exp)
    assert get_expense(expenses, 1) == new_exp, 'Expense values should be updated correctly'

    # Test case 2
    expenses = expenses_example()
    new_exp = {'day': 11, 'total': 54, 'category': 'phone'}
    update_expense(expenses, 2, new_exp)
    assert get_expense(expenses, 2) == new_exp, 'Expense values should be updated correctly'


# Testing 'Remove' functions
def test_delete_expenses_in_day():
    # Test case 1
    expenses = expenses_example()
    delete_expenses_in_day(expenses, 7)
    assert get_length(expenses) == 2, 'Expenses dictionary should have two items after removing'

    # Test case 2
    expenses = expenses_example()
    delete_expenses_in_day(expenses, 5)
    assert get_length(expenses) == 3, 'Expenses dictionary should still have three items after removing'


def test_delete_expenses_in_days_range():
    # Test case 1
    expenses = expenses_example()
    delete_expenses_in_days_range(expenses, 1, 31)
    assert get_length(expenses) == 0, 'Expenses dictionary should be empty'

    # Test case 2
    expenses = expenses_example()
    delete_expenses_in_days_range(expenses, 1, 10)
    assert get_length(expenses) == 2, 'Expenses dictionary should have two items after removing'


def test_delete_expenses_of_category():
    # Test case 1
    expenses = expenses_example()
    delete_expenses_of_category(expenses, 'food')
    assert get_length(expenses) == 2, 'Expenses dictionary should have two items after removing'

    # Test case 2
    expenses = expenses_example()
    delete_expenses_of_category(expenses, 'others')
    assert get_length(expenses) == 3, 'Expenses dictionary should still have three items'


# Testing 'Search' functions
def test_return_expenses_greater_than_num():
    # Test case 1
    expenses = expenses_example()
    result = return_expenses_greater_than_num(expenses, 100)
    assert get_length(result) == 2, 'New expenses dictionary should have two items'

    # Test case 2
    expenses = expenses_example()
    result = return_expenses_greater_than_num(expenses, 50)
    assert get_length(result) == 3, 'New expenses dictionary should have three items'


def test_return_exp_gr_than_num_before_day():
    # Test case 1
    expenses = expenses_example()
    result = return_exp_gr_than_num_before_day(expenses, 20, 100)
    assert get_length(result) == 1, 'New expenses dictionary should have one item'

    # Test case 2
    expenses = expenses_example()
    result = return_exp_gr_than_num_before_day(expenses, 15, 300)
    assert get_length(result) == 0, 'New expenses dictionary should have no item'


def test_return_all_expenses_of_category():
    # Test case 1
    expenses = expenses_example()
    result = return_all_expenses_of_category(expenses, 'food')
    assert get_length(result) == 1, 'New expenses dictionary should have one item'

    # Test case 2
    expenses = expenses_example()
    result = return_all_expenses_of_category(expenses, 'others')
    assert get_length(result) == 0, 'New expenses dictionary should have no item'


# Testing 'Reports' functions
def test_return_sum_of_category():
    # Test case 1
    expenses = expenses_example()
    result = return_sum_of_category(expenses, 'food')
    assert result == 155.49, 'Should return the value of "food" expense (155.49)'

    # Test case 2
    expenses = expenses_example()
    result = return_sum_of_category(expenses, 'phone')
    assert result == 54.77, 'Should return the value of "phone" expense (54.77)'


def test_return_day_of_sum_max():
    # Test case 1
    expenses = expenses_example()
    result = return_day_of_sum_max(expenses)
    assert result == 26, 'Should return the day with the maximum total of expenses (day 26)'


def test_return_exp_equal_to_num():
    # Test case 1
    expenses = expenses_example()
    result = return_exp_equal_to_num(expenses, 54.77)
    assert result == {2: {'day': 11, 'total': 54.77, 'category': 'phone'}}, 'Should return the second expense'

    # Test case 2
    expenses = expenses_example()
    result = return_exp_equal_to_num(expenses, 155.49)
    assert result == {1: {'day': 7, 'total': 155.49, 'category': 'food'}}, 'Should return the first expense'


def test_return_exp_sorted_by_category():
    # Test case 1
    expenses = expenses_example()
    res = return_exp_sorted_by_category(expenses)
    assert get_expense(res, 1) == get_expense(expenses, 1), 'The dict should be sorted (first expense)'
    assert get_expense(res, 2) == get_expense(expenses, 2), 'The dict should be sorted (second expense)'
    assert get_expense(res, 3) == get_expense(expenses, 3), 'The dict should be sorted (third expense)'


# Testing 'Filter' functions
def test_remove_exp_based_on_category():
    # Test case 1
    expenses = expenses_example()
    remove_exp_based_on_category(expenses, 'food')
    exp = {'day': 7, 'total': 155.49, 'category': 'food'}
    assert exp != get_expense(expenses, 1), 'Expense with food category should be removed'

    # Test case 2
    expenses = expenses_example()
    remove_exp_based_on_category(expenses, 'others')
    assert get_length(expenses) == 3, 'Expenses dictionary should remain the same'


def test_remove_exp_smaller_than_num():
    # Test case 1
    expenses = expenses_example()
    remove_exp_smaller_than_num(expenses, 200)
    assert get_length(expenses) == 1, 'Expenses dictionary should have one item'

    # Test case 2
    expenses = expenses_example()
    remove_exp_smaller_than_num(expenses, 50)
    assert get_length(expenses) == 3, 'Expenses dictionary should remain the same'


# Test all functions
def test_all_functionalities():
    # Test 'add' functions
    test_add_new_expense()
    test_update_expense()

    # Test 'remove' functions
    test_delete_expenses_in_day()
    test_delete_expenses_in_days_range()
    test_delete_expenses_of_category()

    # Test 'search' functions
    test_return_expenses_greater_than_num()
    test_return_exp_gr_than_num_before_day()
    test_return_all_expenses_of_category()

    # Test 'reports' functions
    test_return_sum_of_category()
    test_return_day_of_sum_max()
    test_return_exp_equal_to_num()
    test_return_exp_sorted_by_category()

    # Test 'filter' functions
    test_remove_exp_based_on_category()
    test_remove_exp_smaller_than_num()

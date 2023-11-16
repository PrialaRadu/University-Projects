# Test functions that check the integrity of 'get' and 'set' functions

from project.variables.get_variables import *


# Example of expense (with ID)
def expense_example():
    return {1: {'day': 13, 'total': 153.91, 'category': 'food'}}


# Example of expense (without ID)
def value_example():
    return {'day': 13, 'total': 153.91, 'category': 'food'}


def test_get_id():
    expense = expense_example()
    assert get_id(expense) == 1, 'Should return the correct id'


def test_get_day():
    expense = value_example()
    assert get_day(expense) == 13, 'Should return the correct day'


def test_get_total():
    expense = value_example()
    assert get_total(expense) == 153.91, 'Should return the correct total'


def test_get_category():
    expense = value_example()
    assert get_category(expense) == 'food', 'Should return the correct category'


def test_set_id():
    expense = expense_example()
    set_id(expense, 2)
    assert get_id(expense) == 2, 'Should change the id'


def test_set_day():
    expense = value_example()
    set_day(expense, 14)
    assert get_day(expense) == 14, 'Should change the day'


def test_set_total():
    expense = value_example()
    set_total(expense, 154)
    assert get_total(expense) == 154, 'Should change the total'


def test_set_category():
    expense = value_example()
    set_category(expense, 'phone')
    assert get_category(expense) == 'phone', 'Should change the category'


# Test all functions
def test_all_variables():
    test_get_id()
    test_get_day()
    test_get_day()
    test_get_total()
    test_get_category()
    test_set_id()
    test_set_day()
    test_set_total()
    test_set_category()

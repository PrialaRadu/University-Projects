# Functions that retrieve/change details of the expense.


# Retrieve details
def get_expense(expenses, id_p):
    return expenses[id_p]


def get_length(expenses):
    return len(expenses)


def get_id(expense):
    return list(expense)[0]


def get_day(expense):
    return expense['day']


def get_total(expense):
    return expense['total']


def get_category(expense):
    return expense['category']


# Change details
def set_id(expense, id_p):
    expense[id_p] = expense.pop(1)


def set_day(expense, day):
    expense['day'] = day


def set_total(expense, total):
    expense['total'] = total


def set_category(expense, category):
    expense['category'] = category

import calculator.vars as var
from calculator.parser import analyze1, parsing


ERRORS = {'brackets': 'brackets are not balanced',
          'not_correct': 'expression is not correct',
          'empty': 'expression is empty',
          }


def pre_error_checking(expression):
    error_name = None
    if expression.count('(') != expression.count(')'):
        error_name = 'brackets'
    elif len(expression) == expression.count(' '):
        error_name = 'empty'
    if error_name:
        raise ValueError(ERRORS[error_name])


def error_checking_after_analyze1(expression):
    error_name = None
    elements_stack = []
    operators_stack = []
    for element in expression:
        if element in var.OPERATORS:
            operators_stack.append(element)
        elif element not in ['(', ')']:
            elements_stack.append(element)
    for element in elements_stack:
        if not isinstance(element, (int, float)):
            raise ValueError(f"unknown function '{element}'")
    if expression[-1] in var.OPERATORS:
        error_name = 'not_correct'
    elif len(elements_stack) == 1 and len(operators_stack) <= 1:
        pass
    elif (len(operators_stack) < len(elements_stack)/2) or not elements_stack and expression[-1] != ')':
        error_name = 'not_correct'
    if error_name:
        raise ValueError(ERRORS[error_name])


def error_checking_after_parsing(expression):
    error_name = None
    for idx, element in enumerate(expression):
        if (element not in ['--', '++'] and element in var.OPERATORS
           and var.OPERATORS[element].priority < 5):
            try:
                if (expression[idx + 1] in var.OPERATORS and
                   var.OPERATORS[expression[idx + 1]].priority < 5 and expression[idx + 1] not in ['++', '--']):
                    error_name = 'not_correct'
                    break
            except Exception:
                break
    if error_name:
        raise ValueError(ERRORS[error_name])


def errors_checking(expression):
    pre_error_checking(expression)
    error_checking_after_analyze1(analyze1(expression))
    error_checking_after_parsing(parsing(expression))

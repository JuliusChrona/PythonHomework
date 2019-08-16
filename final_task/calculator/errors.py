import calculator.vars as var
import sys
from calculator.parser import analyze1, parsing


ERRORS = {'brackets': 'brackets are not balanced',
          'not_correct': 'expression is not correct',
          'empty': 'expression is empty',
          }


def pre_test(expression):
    error_name = None
    if expression.count('(') != expression.count(')'):
        error_name = 'brackets'
    elif len(expression) == expression.count(' '):
        error_name = 'empty'
    if error_name:
        print(f'ERROR: {ERRORS[error_name]}')
        sys.exit(0)


def test_after_analyze1(expression):
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
            print(f"ERROR: unknown function '{element}'")
            sys.exit(0)
    if expression[-1] in var.OPERATORS:
        error_name = 'not_correct'
    elif len(elements_stack) == 1 and len(operators_stack) <= 1:
        pass
    elif (len(operators_stack) < len(elements_stack)/2) or not elements_stack:
        error_name = 'not_correct'
    if error_name:
        print(f'ERROR: {ERRORS[error_name]}')
        sys.exit(0)


def test_after_parsing(expression):
    error_name = None
    for idx, element in enumerate(expression):
        if (element not in ['+', '-'] and element in var.OPERATORS
           and var.OPERATORS[element][0] < 5):
            try:
                if (expression[idx + 1] in var.OPERATORS and
                   var.OPERATORS[expression[idx + 1]][0] < 5 and expression[idx + 1] not in ['+', '-']):
                    error_name = 'not_correct'
                    break
            except Exception:
                pass
    if error_name:
        print(f'ERROR: {ERRORS[error_name]}')
        sys.exit(0)


def tests(expression):
    pre_test(expression)
    test_after_analyze1(analyze1(expression))
    test_after_parsing(parsing(expression))

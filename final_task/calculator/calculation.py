import calculator.errors as error
import calculator.parser as pars
from calculator.interface import importing
from calculator.vars import OPERATORS, MATH_CONST
from typing import List, Union

arg1, arg2 = None, None


def sorting(expression: list) -> List[Union[str, float]]:
    """ convert expression in reverse polish notation"""
    buff = []
    stack = []
    for element in expression:
        if element in OPERATORS:
            while buff and buff[-1] != "(" and OPERATORS[element][0] <= OPERATORS[buff[-1]][0]:
                if element == "^" and 4 >= OPERATORS[buff[-1]][0]:
                    break
                stack.append(buff.pop())
            buff.append(element)
        elif element == ")":
            while buff:
                oper = buff.pop()
                if oper == "(":
                    break
                stack.append(oper)
        elif element == "(":
            buff.append(element)
        else:
            stack.append(element)
    stack.extend(buff[::-1])
    return stack


def calculate(reverse_polish_notation: list) -> Union[int, float, bool]:
    stack = []
    for element in reverse_polish_notation:
        if element in OPERATORS:
            try:
                global arg1, arg2
                arg2 = stack.pop()
                arg1 = stack.pop()
                stack.append(OPERATORS[element][1](arg1, arg2))
                arg1, arg2 = None, None
            except ZeroDivisionError:
                print('ERROR: You can\'t divide by zero')
                exit(0)
            except Exception:
                try:
                    if arg1 is not None:  # arg1 can be equal 0
                        stack.append(arg1)
                    stack.append(OPERATORS[element][1](arg2))
                except Exception as e:
                    print(f'ERROR: {e}')
                    exit(0)
        elif element in OPERATORS and len(stack) == 0:
            stack.append(OPERATORS[element][1]())
        else:
            stack.append(element)
    return stack[0]


def evaluated(expression: str, module: List[str] = None) -> Union[int, float, bool]:
    if module:
        OPERATORS.update(importing(module))
        MATH_CONST.update(importing(module, is_const=True))
    error.tests(expression)
    result = calculate(sorting(pars.parsing(expression)))
    return result

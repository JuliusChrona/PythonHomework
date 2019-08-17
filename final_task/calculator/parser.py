import string
import calculator.vars as var
from typing import List, Union

alphabet = string.ascii_letters + '_'
digits = string.digits
compar_char = ['<', '<=', '==', '>=', '!=', '>', '!', '=']


def analyze1(expression: str) -> List[Union[str, float]]:
    """ combine digits in numbers, letters in words, etc """
    number = ''
    word = ''
    comparison = ''
    stack = []
    for char in expression:
        if char in alphabet:
            word += char
        elif char in digits and word:
            word += char
            continue
        elif word:
            if word in var.MATH_CONST:
                word = var.MATH_CONST[word]
            stack.append(word)
            word = ''
        if char in digits + '.':
            number += char
        elif number:
            if number.count('.') > 1:
                print('ERROR: expression is not correct')
                exit(0)
            stack.append(float(number))
            number = ''
        if char == ',':
            stack.extend([')', '('])
            continue
        if char in compar_char:
            comparison += char
        elif comparison:
            stack.append(comparison)
            comparison = ''
        if char in var.OPERATORS and char not in compar_char or char in "()":
            stack.append(char)
    if number:
        if number.count('.') > 1:
            print('ERROR: expression is not correct')
            exit(0)
        stack.append(float(number))
    if word:
        if word in var.MATH_CONST:
            word = var.MATH_CONST[word]
        stack.append(word)
    if comparison:
        stack.append(comparison)
    return stack


def deleting_signs(stack: list) -> List[Union[str, float]]:
    """ delete all extra signs '+' and '-' (e.g: 1+-+-+---+-1 -> 1+1) """
    for idx, element in enumerate(stack):
        if element == '+' or element == 'plug':
            if stack[idx - 1] == '+':
                stack[idx - 1] = 'plug'
            elif stack[idx - 1] == '-':
                del stack[idx]
                deleting_signs(stack)
        elif element == '-':
            if stack[idx - 1] == '-':
                stack[idx - 1: idx + 1] = ['+', '+']
                deleting_signs(stack)
            elif stack[idx - 1] == '+':
                del stack[idx - 1]
                deleting_signs(stack)


def analyze2(expression: list) -> List[Union[str, float]]:
    """ use unary minus and plus, and delete unnecessary signs """
    stack = expression[:]
    buff = []
    stack.reverse()
    deleting_signs(stack)
    stack = [element for element in stack if element != 'plug']
    if stack[-1] == "+":
        del stack[-1]
    elif stack[-1] == '-' and isinstance(stack[-2], (int, float)):
        stack[-2] = var.pos_neg['-'](stack[-2])
        del stack[-1]
    elif stack[-1] == '-':
        stack[-1] = '--'
    stack.reverse()
    for idx, element in enumerate(stack):
        if element in ['-', '+'] and (stack[idx - 1] in var.OPERATORS or stack[idx - 1] == '('):
            if isinstance(stack[idx + 1], (float, int)):
                stack[idx + 1] = var.pos_neg[element](stack[idx + 1])
                buff.append(idx)
            else:
                stack[idx] = '--' if element == '-' else '++'
    if buff:
        counter = 0
        for idx in buff:
            stack.pop(idx - counter)
            counter += 1
    return stack


def parsing(expression: str) -> List[Union[str, float]]:
    return(analyze2(analyze1(expression)))

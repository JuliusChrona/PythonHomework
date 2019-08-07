import string
from importlib import import_module
from typing import Generator
from operator import neg, pos
#from calculator.interface import importing

alphabet = string.ascii_letters + '_'
digits = string.digits + '.'
compar_char = '<==!=>='
res_bool = False
module = import_module('math')
math_const = dict.fromkeys(['e', 'inf', 'nan', 'pi', 'tau'])
math_const.update({const: value 
                 for const, value in module.__dict__.items()
                 if const in math_const }
                )
OPERATORS = {'+': (1, lambda arg1, arg2: arg1 + arg2), 
             '-': (1, lambda arg1, arg2: arg1 - arg2),  
             '*': (2, lambda arg1, arg2: arg1 * arg2),
             '/': (2, lambda arg1, arg2: arg1 / arg2),
             '%': (2, lambda arg1, arg2: arg1 % arg2), 
             '//': (2, lambda arg1, arg2: arg1 // arg2),
             '^': (3, lambda arg1, arg2: arg1 ** arg2),
             'round': (4, round), 'abs': (4, abs),
             '<': (0, lambda arg1, arg2: arg1 < arg2),
             '<=': (0, lambda arg1, arg2: arg1 <= arg2),
             '==': (0, lambda arg1, arg2: arg1 == arg2),
             '>=': (0, lambda arg1, arg2: arg1 >= arg2),
             '!=': (0, lambda arg1, arg2: arg1 != arg2),
             '>': (0, lambda arg1, arg2: arg1 > arg2)
            }
OPERATORS.update({obj: (4, value)
                 for obj, value in module.__dict__.items() 
                 if not obj.startswith('_') 
                 if obj not in math_const}
                )

def analyze1(expression: str) -> Generator:
    number = ''
    word = ''
    comparison = ''
    for char in expression:
        if char in alphabet:
            word += char
        elif char in digits and word:
            word += char
            continue
        elif word:
            if word in math_const:
                word = math_const[word]
            yield word
            word = ''
        if char in digits:
            number += char  
        elif number:
            yield float(number)
            number = ''
        if char == ',':
            yield ')'
            yield '('
            continue
        if char in compar_char:
            comparison += char
        elif comparison:
            yield comparison
            comparison = ''
        if char in OPERATORS and char not in compar_char or char in "()":
            yield char 
    if number:
        yield float(number)
    if word:
        if word in math_const:
            word = math_const[word]
        yield word
    if comparison:
        yield comparison

#for i in analyze('log10(-100)'): print(i)   # for tests

def analyze2(expression):
    stack = []
    stack1 = []
    for element in expression:
        stack.append(element)
    stack.reverse()
    def deleter(stack: list):
        for idx, element in enumerate(stack):
            if element == '-':
                if stack[idx - 1] == '-':
                    del stack[idx]; del stack[idx - 1]
                    stack.insert(idx, '+')
                elif stack[idx - 1] == '+':
                    del stack[idx - 1]
                    deleter(stack)
            elif element == '+':
                if stack[idx - 1] == '+':
                    del stack[idx - 1]
                    deleter(stack)
    deleter(stack)
    stack.reverse()
    deleter(stack)
    stack.reverse()
    for idx, element in enumerate(stack):
        if element in ['+', '-']:
            if isinstance(stack1[idx - 1], (float, int)):
                if element == '-':
                    stack1[idx - 1] = neg(stack1[idx - 1])
                    stack1.append('+') 
                else:
                    stack1.append('+')
            else:
                stack1.append(element)
        else:
            stack1.append(element)
    stack1.reverse()
    return stack1

#print(analyze2(analyze1('----+++-+--+1')))

def parser(expression):
    return(analyze2(analyze1(expression)))

def sorting(expression: Generator) -> Generator:
    stack = [] 
    for element in expression:
        if element in OPERATORS: 
            while stack and stack[-1] != "("  and OPERATORS[element][0] <= OPERATORS[stack[-1]][0]:
                yield stack.pop()
            stack.append(element)
        elif element == ")":
            while stack:
                oper = stack.pop()
                if oper == "(":
                    break
                yield oper
        elif element == "(":
            stack.append(element)
        else:
            yield element
    while stack:
        yield stack.pop()

#for i in sorting(analyze2(analyze1('1+1'))): print(i)   # for testing

def calc(reverse_polish_notation: Generator) -> float or int:
    stack = []
    for element in reverse_polish_notation:
        if element in OPERATORS and element in compar_char:
            global res_bool;
            res_bool = True
        if element in OPERATORS and len(stack) > 1:
            if element == 'log':
                arg1, arg2 = stack.pop(), stack.pop()
            else:
                arg2, arg1 = stack.pop(), stack.pop()  
            stack.append(OPERATORS[element][1](arg1, arg2))
        elif element in OPERATORS and len(stack) == 1:
            arg1 = stack.pop()
            if element == '-':
                stack.append(neg(arg1))
            elif element == '+':
                stack.append(pos(arg1))
            else:
                stack.append(OPERATORS[element][1](arg1))
        elif element in OPERATORS and len(stack) == 0:
            stack.append(OPERATORS[element][1]())
        else:
            stack.append(element)
    if res_bool:
        return bool(stack[0])
    elif stack[0] == int(stack[0]):
        return int(stack[0])
    else:
        return stack[0]

def evaluated(expression, module):
    if module:
        OPERATORS.update(importing(module))
    return calc(sorting(parser(expression)))

#print(evaluated('-log10(100)', None)) # for tests


''' UNARY_OPERATORS = {
    "6-(-13)": 6-(-13),
    "2*sin(pi/2)": 2*sin(pi/2)
    "2^3^4": 2**3**4,
   "10*e^0*log10(.4 -5/ -0.1-10) - -abs(-53/10) + -5": 10*e**0*log10(.4 -5/ -0.1-10) - -abs(-53/10) + -5,
   "10*e^0*log10(.4 -5/ -0.1-10) - -abs(-53/10) + -5": 10*e**0*log10(.4 -5/ -0.1-10) - -abs(-53/10) + -5,
    "sin(-cos(-sin(3.0)-cos(-sin(-3.0*5.0)-sin(cos(log10(43.0))))+cos(sin(sin(34.0-2.0^2.0))))--cos(1.0)--cos(0.0)^3.0)": sin(-cos(-sin(3.0)-cos(-sin(-3.0*5.0)-sin(cos(log10(43.0))))+cos(sin(sin(34.0-2.0**2.0))))--cos(1.0)--cos(0.0)**3.0),
   "sin(e^log(e^e^sin(23.0),45.0) + cos(3.0+log10(e^-e)))": sin(e**log(e**e**sin(23.0),45.0) + cos(3.0+log10(e**-e))),

    
'''
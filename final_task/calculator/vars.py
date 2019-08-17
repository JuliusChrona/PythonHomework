import operator
from importlib import import_module
from collections import namedtuple

Operator = namedtuple("operator", ["priority", 'function'])
Const = namedtuple("constant", 'value')
module = import_module('math')
pos_neg = {'+': operator.pos, '-': operator.neg}
MATH_CONST = dict.fromkeys(['e', 'inf', 'nan', 'pi', 'tau'], Const(value=None))
MATH_CONST.update({const: Const(value=weight)
                  for const, weight in module.__dict__.items()
                  if const in MATH_CONST}
                  )
OPERATORS = {'+': Operator(priority=2, function=operator.add),
             '-': Operator(priority=2, function=operator.sub),
             '--': Operator(priority=2, function=operator.neg),
             '++': Operator(priority=2, function=operator.pos),
             '*': Operator(priority=3, function=operator.mul),
             '/': Operator(priority=3, function=operator.truediv),
             '%': Operator(priority=3, function=operator.mod),
             '//': Operator(priority=3, function=operator.floordiv),
             '^': Operator(priority=4, function=operator.pow),
             'round': Operator(priority=5, function=round),
             'abs': Operator(priority=5, function=abs),
             '<': Operator(priority=1, function=operator.lt),
             '<=': Operator(priority=1, function=operator.le),
             '==': Operator(priority=0, function=operator.eq),
             '>=': Operator(priority=1, function=operator.ge),
             '!=': Operator(priority=0, function=operator.ne),
             '>': Operator(priority=1, function=operator.gt)
             }
OPERATORS.update({obj: Operator(priority=5, function=value)
                 for obj, value in module.__dict__.items()
                 if not obj.startswith('_')
                 if obj not in MATH_CONST}
                 )

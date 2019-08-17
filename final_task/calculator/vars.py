import operator
from importlib import import_module

module = import_module('math')
pos_neg = {'+': operator.pos, '-': operator.neg}
MATH_CONST = dict.fromkeys(['e', 'inf', 'nan', 'pi', 'tau'])
MATH_CONST.update({const: value
                  for const, value in module.__dict__.items()
                  if const in MATH_CONST}
                  )
OPERATORS = {'+': (2, operator.add),
             '-': (2, operator.sub),
             '--': (2, operator.neg),
             '++': (2, operator.pos),
             '*': (3, operator.mul),
             '/': (3, operator.truediv),
             '%': (3, operator.mod),
             '//': (3, operator.floordiv),
             '^': (4, operator.pow),
             'round': (5, round), 'abs': (5, abs),
             '<': (1, operator.lt),
             '<=': (1, operator.le),
             '==': (0, operator.eq),
             '>=': (1, operator.ge),
             '!=': (0, operator.ne),
             '>': (1, operator.gt)
             }
OPERATORS.update({obj: (5, value)
                 for obj, value in module.__dict__.items()
                 if not obj.startswith('_')
                 if obj not in MATH_CONST}
                 )

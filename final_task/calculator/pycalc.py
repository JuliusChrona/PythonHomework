#!/usr/bin/env
from calculator.interface import cmd_interface
import calculator.calculation


def main():
    expression, modules = cmd_interface()
    res = calculator.calculation.evaluated(expression, modules)
    print(res)


if __name__ == '__main__':
    main()

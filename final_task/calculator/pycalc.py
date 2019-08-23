#!/usr/bin/env
from calculator.interface import cmd_interface
import calculator.calculation


def main():
    try:
        expression, modules = cmd_interface()
        res = calculator.calculation.evaluated(expression, modules)
        print(res)
    except Exception as error:
        print(f"ERROR: {error}")


if __name__ == '__main__':
    main()

#!/usr/bin/python
from calculator.interface import main
import calculator.parser

if __name__ == '__main__':
	expression, modules = main()
	print(calculator.parser.evaluated(expression, modules))



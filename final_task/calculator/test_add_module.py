import calculator.module_for_test as tm
import time
import unittest
from calculator.calculation import evaluated


class TestAddModule(unittest.TestCase):

    def test_added_module(self):
        self.assertEqual(evaluated('time()', ['time']), time.time())
        self.assertEqual(evaluated('time()/3600/365/24', ['time']), time.time()/3600/365/24)
        self.assertEqual(evaluated('sin()', ['calculator.module_for_test']), tm.sin())
        self.assertEqual(evaluated('cos()', ['calculator.module_for_test']), tm.cos())
        self.assertEqual(evaluated('pi+e', ['calculator.module_for_test']), tm.pi + tm.e)
        self.assertEqual(evaluated('log(5, 6)', ['calculator.module_for_test']), tm.log(5, 6))
        self.assertEqual(evaluated('log(10, 100)', ['calculator.module_for_test']), tm.log(10, 100))

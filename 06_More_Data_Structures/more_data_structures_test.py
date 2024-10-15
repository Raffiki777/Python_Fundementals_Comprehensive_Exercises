import unittest
import sys
from io import StringIO
from more_data_structures import *


class TestExercise06(unittest.TestCase):

    def test_print_set(self):
        bool_output = None
        captured_output = StringIO()
        sys.stdout = captured_output
        print_set()
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue().strip()
        convert_output = eval(output)
        expected_output = {"Anele", "Litha", "Nontando", 39, "Gomolemo", "Tshegofatso", "Tanatswa", 38,
                           "Monwabisi", "Vuyisile", "Dikeledi",77, "Rafiki"}

        for x in convert_output:
            if x in expected_output:
                bool_output = True
            else:
                bool_output = None
                break

        self.assertTrue(
            bool_output, (f"\n{expected_output} != {convert_output}"))

    def test_remove_(self):
        bool_output = None
        captured_output = StringIO()
        sys.stdout = captured_output
        remove_katlego()
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue().strip()
        convert_output = eval(output)
        expected_output = {"Anele", "Litha", "Nontando", 39, "Gomolemo", "Tshegofatso", "Tanatswa", 38, "Monwabisi", "Vuyisile", "Dikeledi",77, "Rafiki"}

        for x in convert_output:
            if x in expected_output:
                bool_output = True
            else:
                bool_output = None
                break

        self.assertTrue(
            bool_output, (f"\n{expected_output} != {convert_output}"))

    def test_add_names(self):
        bool_output = None
        captured_output = StringIO()
        sys.stdout = captured_output
        add_names()
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue().strip()
        convert_output = eval(output)
        expected_output = {"Anele", "Litha", "Nontando", 39, "Gomolemo", "Tshegofatso", "Katlego", "Tanatswa", 38, "Monwabisi", "Vuyisile", "Dikeledi",77, "Rafiki", "Kyle", "Sihle"}

        for x in convert_output:
            if x in expected_output:
                bool_output = True
            else:
                bool_output = None
                break

        self.assertTrue(
            bool_output, (f"\n{expected_output} != {convert_output}"))

    def test_difference(self):
        bool_output = None
        captured_output = StringIO()
        sys.stdout = captured_output
        difference()
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue().strip()
        convert_output = eval(output)
        expected_output = {'Kyle', 'Tshegofatso'}

        for x in convert_output:
            if x in expected_output:
                bool_output = True
            else:
                bool_output = None
                break

        self.assertTrue(
            bool_output, (f"\n{expected_output} != {convert_output}"))


if __name__ == "__main__":
    unittest.main()

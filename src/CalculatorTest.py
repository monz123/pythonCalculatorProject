import unittest
from Calculator import Calculator
from CsvReader import CsvReader


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_add_method_calculator(self):
        test_data = CsvReader("src/Unit Test Addition.csv").data
        for row in test_data:
            result = int(row['Result'])
            self.assertEqual(self.calculator.add(row['Value 1'], row['Value 2']), result)
            self.assertEqual(self.calculator.result, result)

    def test_sub_method_calculator(self):
        test_data = CsvReader("src/Unit Test Subtraction.csv").data
        for row in test_data:
            result = int(row['Result'])
            self.assertEqual(self.calculator.sub(row['Value 1'], row['Value 2']), result)
            self.assertEqual(self.calculator.result, result)


if __name__ == '__main__':
    unittest.main()

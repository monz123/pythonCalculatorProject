import unittest
from Calculator import Calculator
from CsvReader import CsvReader


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_add_method_calculator(self):
        test_data = CsvReader("src/CsvForTesting/Unit Test Addition.csv").data
        for row in test_data:
            result = int(row['Result'])
            self.assertEqual(self.calculator.add(row['Value 1'], row['Value 2']), result)
            self.assertEqual(self.calculator.result, result)

    def test_sub_method_calculator(self):
        test_data = CsvReader("src/CsvForTesting/Unit Test Subtraction.csv").data
        for row in test_data:
            result = int(row['Result'])
            self.assertEqual(self.calculator.sub(row['Value 1'], row['Value 2']), result)
            self.assertEqual(self.calculator.result, result)

    def test_multiply_method_calculator(self):
        test_data = CsvReader("src/CsvForTesting/Unit Test Multiplication.csv").data
        for row in test_data:
            result = int(row['Result'])
            self.assertEqual(self.calculator.multiply(row['Value 1'], row['Value 2']), result)
            self.assertEqual(self.calculator.result, result)

    def test_square_method_calculator(self):
        test_data = CsvReader("src/CsvForTesting/Unit Test Square.csv").data
        for row in test_data:
            result = int(row['Result'])
            self.assertEqual(self.calculator.squares(row['Value 1']), result)
            self.assertEqual(self.calculator.result, result)

    def test_divide_method_calculator(self):
        test_data = CsvReader("src/CsvForTesting/Unit Test Division.csv").data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.calculator.divide(row['Value 1'], row['Value 2']), result)
            self.assertEqual(self.calculator.result, result)


if __name__ == '__main__':
    unittest.main()

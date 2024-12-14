import unittest
from calculation import calculate, calculate_addition, calculate_subtraction, calculate_division, calculate_multiplication, calculate_exponentiation

class TestCalculation(unittest.TestCase):

    def test_calculate_addition(self):
        result = calculate_addition(5, 3)
        self.assertEqual(result, 8)

    def test_calculate_subtraction(self):
        result = calculate_subtraction(5, 3)
        self.assertEqual(result, 2)

    def test_calculate_multiplication(self):
        result = calculate_multiplication(5, 3)
        self.assertEqual(result, 15)

    def test_calculate_division(self):
        result = calculate_division(6, 3)
        self.assertEqual(result, 2)

    def test_calculate_division_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            calculate_division(5, 0)

    def test_calculate_exponentiation(self):
        result = calculate_exponentiation(2, 3)
        self.assertEqual(result, 8)

    def test_calculate_invalid_operation(self):
        result = calculate(5, 3, 'invalid_operation')
        self.assertEqual(result, 0)

    def test_calculate_addition_with_floats(self):
        result = calculate_addition(5.5, 3.1)
        self.assertAlmostEqual(result, 8.6)

    def test_calculate_subtraction_with_floats(self):
        result = calculate_subtraction(5.5, 3.1)
        self.assertAlmostEqual(result, 2.4)

    def test_calculate_multiplication_with_floats(self):
        result = calculate_multiplication(5.5, 3.1)
        self.assertAlmostEqual(result, 17.05)

    def test_calculate_division_float(self):
        result = calculate_division(5.0, 2.0)
        self.assertEqual(result, 2.5)

if __name__ == '__main__':
    unittest.main()
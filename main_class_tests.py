import unittest
from unittest.mock import MagicMock
from calculator_logic import Calculator
import math


# Предполагается, что класс Calculator импортирован сюда

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()
        self.calculator.ids = {
            'result_field': MagicMock(),
            'answer_field': MagicMock(),
            'memory_cash': MagicMock()
        }

    def test_integer_entered(self):
        self.calculator.integer_entered('5')
        self.calculator.reload_input_field()
        self.assertEqual(self.calculator.current_input, '5')
        self.calculator.ids['result_field'].text = '5'

    def test_operation_entered_first_time(self):
        self.calculator.current_input = '5'
        self.calculator.operation_entered('+')
        self.assertEqual(self.calculator.last_input, '5')
        self.assertEqual(self.calculator.current_input, '')
        self.assertEqual(self.calculator.operation, '+')

    def test_equal_input(self):
        self.calculator.last_input = '5'
        self.calculator.current_input = '3'
        self.calculator.operation = '+'
        self.calculator.equal_input()
        self.assertEqual(self.calculator.current_input, '8.0')
        self.calculator.ids['answer_field'].text = '8'

    def test_sqrt(self):
        self.calculator.current_input = '9'
        self.calculator.sqrt()  # Предполагаем, что метод sqrt присутствует
        self.assertEqual(self.calculator.current_input, '3.0')
        self.calculator.ids['result_field'].text = '3.0'

    def test_sin(self):
        self.calculator.current_input = '0'
        self.calculator.sin()
        self.assertEqual(self.calculator.current_input, '0.0')

    def test_cos(self):
        self.calculator.current_input = '0'
        self.calculator.cos()
        self.assertEqual(self.calculator.current_input, '1.0')

    def test_floor(self):
        self.calculator.current_input = '2.9'
        self.calculator.floor()
        self.assertEqual(self.calculator.current_input, '2')

    def test_ceil(self):
        self.calculator.current_input = '2.1'
        self.calculator.ceil()
        self.assertEqual(self.calculator.current_input, '3')

    def test_memory_operations(self):
        self.calculator.current_input = '10'
        self.calculator.M_plus()  # Добавляем 10 в память
        self.assertEqual(self.calculator.memory, '10.0')
        self.calculator.M_minus()  # Вычитаем 10 из памяти
        self.assertEqual(self.calculator.memory, '0.0')
        self.calculator.MC()  # Очищаем память
        self.assertEqual(self.calculator.memory, '')


if __name__ == '__main__':
    unittest.main()
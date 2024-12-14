import unittest
from mock import MagicMock
from kivy.uix.boxlayout import BoxLayout
from calculator_logic import Calculator  # Замените на фактический путь вашего модуля


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()
        self.calculator.ids = {
            'result_field': MagicMock(),
            'answer_field': MagicMock(),
            'memory_cash': MagicMock(),
        }

    def test_integer_entered(self):
        self.calculator.integer_entered('5')
        self.assertEqual(self.calculator.current_input, '5')

        self.calculator.integer_entered('3')
        self.assertEqual(self.calculator.current_input, '53')
        self.calculator.pressed_equal = True
        self.calculator.integer_entered('2')
        self.assertEqual(self.calculator.current_input, '2')
        self.calculator.reload_answer_field()
        #self.calculator.reload_answer_field.assert_called_with('0')
        self.assertEqual(self.calculator.memory, '0')

    def test_operation_entered(self):
        self.calculator.integer_entered('5')
        self.calculator.operation_entered('+')
        self.assertEqual(self.calculator.operation, '+')
        self.calculator.last_input = self.calculator.current_input
        self.calculator.current_input = ''

        # Testing with active operation and current input
        self.calculator.integer_entered('3')
        self.calculator.operation_entered('*')
        self.assertEqual(self.calculator.operation, '*')
        self.assertEqual(self.calculator.last_input, '3')
        self.assertEqual(self.calculator.current_input, '')

    def test_equal_input(self):
        self.calculator.integer_entered('5')
        self.calculator.operation_entered('+')
        self.calculator.integer_entered('3')
        self.calculator.equal_input()
        self.assertEqual(self.calculator.current_input, '8.0')
        self.calculator.reload_answer_field.assert_called_with('8.0')

    def test_delete(self):
        self.calculator.integer_entered('123')
        self.calculator.delete()
        self.assertEqual(self.calculator.current_input, '12')
        self.calculator.delete()
        self.assertEqual(self.calculator.current_input, '1')
        self.calculator.delete()
        self.assertEqual(self.calculator.current_input, '')

    def test_memory_operations(self):
        self.calculator.integer_entered('10')
        self.calculator.M_plus()
        self.assertEqual(self.calculator.memory, '10.0')

        self.calculator.integer_entered('5')
        self.calculator.M_minus()
        self.assertEqual(self.calculator.memory, '5.0')

        self.calculator.MR()
        self.assertEqual(self.calculator.current_input, '5.0')

        self.calculator.MC()
        self.assertEqual(self.calculator.memory, '0')


if __name__ == '__main__':
    unittest.main()
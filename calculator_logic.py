class CalculatorLogic:
    """Класс для выполнения математических операций с памятью первого числа."""

    def __init__(self):
        self.first_number = None
        self._operation = None

    @property
    def operation(self):
        return self._operation

    @operation.setter
    def operation(self, operation):
        if operation not in ["+", "*", "/"]:
            raise ValueError("Операция должна быть '+', '*' или '/'")
        self._operation = operation

    def calculate(self, second_number):
        """Выполняет расчет на основе текущей операции."""
        if self.first_number is None or self._operation is None:
            raise ValueError("Не задано первое число или операция!")

        if self._operation == "+":
            return self.first_number + second_number
        elif self._operation == "*":
            return self.first_number * second_number
        elif self._operation == "/":
            if second_number == 0:
                raise ValueError("Деление на ноль!")
            return self.first_number / second_number

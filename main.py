from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from calculator_logic import CalculatorLogic


class CalculatorApp(App):
    def build(self):
        self.logic = CalculatorLogic()
        self.current_input = ""
        self.history = ""

        layout = BoxLayout(orientation="vertical", padding=10, spacing=10)

        self.history_label = Label(text=self.history, size_hint=(1, 0.2))
        layout.add_widget(self.history_label)

        self.input_field = TextInput(hint_text="Введите число", multiline=False, input_filter="float")
        layout.add_widget(self.input_field)

        button_layout = BoxLayout(size_hint=(1, 0.2), spacing=10)

        add_button = Button(text="+", on_press=lambda x: self.set_operation("+"))
        multiply_button = Button(text="*", on_press=lambda x: self.set_operation("*"))
        divide_button = Button(text="/", on_press=lambda x: self.set_operation("/"))
        equal_button = Button(text="=", on_press=lambda x: self.calculate_result())
        clear_button = Button(text="Очистить", on_press=lambda x: self.clear_all())

        button_layout.add_widget(add_button)
        button_layout.add_widget(multiply_button)
        button_layout.add_widget(divide_button)
        button_layout.add_widget(equal_button)
        button_layout.add_widget(clear_button)

        layout.add_widget(button_layout)

        return layout

    def set_operation(self, operation):
        """Устанавливает операцию и обновляет историю."""
        try:
            num = float(self.input_field.text)
            self.current_input = str(num)

            self.history += f"{self.current_input} {operation}\n"
            self.history_label.text = self.history

            self.logic.operation = operation
            self.logic.first_number = num

            self.input_field.text = ""
        except ValueError:
            self.history_label.text = "Ошибка: Введите корректное число!"

    def calculate_result(self):
        """Выполняет расчет и обновляет историю."""
        try:
            num = float(self.input_field.text)
            result = self.logic.calculate(num)

            self.history += f"{num} = {result}\n"
            self.history_label.text = self.history

            self.input_field.text = ""
            self.logic.first_number = result
        except ValueError:
            self.history_label.text = "Ошибка: Введите корректное число!"

    def clear_all(self):
        """Очищает историю и поле ввода."""
        self.history = ""
        self.history_label.text = self.history
        self.input_field.text = ""
        self.logic.first_number = None


if __name__ == "__main__":
    CalculatorApp().run()

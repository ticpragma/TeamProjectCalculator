from kivy.app import App
from calculator_logic import Calculator


class CalculatorApp(App):
    def build(self):
        return Calculator()


if __name__ == "__main__":
    CalculatorApp().run()

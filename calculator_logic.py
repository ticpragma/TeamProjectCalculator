from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from constants import OPERATIONS
from calculation import calculate

class Calculator(BoxLayout):
    memory = 0

    last_input = ''
    current_input = ''
    operation = ''
    pressed_equal = False

    def input_from_user(self, user_input, is_operation=False):
        if bool(is_operation):
            self.operation_entered(user_input)
        else:
            self.integer_entered(user_input)


    def operation_entered(self, user_input):

        if self.last_input == '' and self.current_input == '':
            return

        elif self.last_input == '' and self.current_input != '':
            self.last_input = self.current_input
            self.current_input = ''
            self.operation = user_input
            self.reload_input_field()

        elif self.last_input != '' and self.current_input != '':
            self.last_input = calculate(self.last_input, self.current_input, self.operation)
            self.current_input = ''
            self.reload_input_field()
            self.reload_answer_field(self.last_input)
            self.operation = user_input
        elif self.last_input != '' and self.current_input == '':
            self.operation = user_input
        else:
            return


    def integer_entered(self, user_input):
        if self.pressed_equal:
            self.current_input = user_input
            self.reload_answer_field('0')
            self.pressed_equal = False
        else:
            self.current_input = self.current_input + user_input

        self.reload_input_field()


    def reload_input_field(self):
        if self.current_input == '':
            self.ids['result_field'].text = '0'
            return

        self.ids['result_field'].text = str(self.current_input)

    def reload_answer_field(self, value):
        self.ids['answer_field'].text = str(value)

    def delete(self):
        if len(self.current_input) > 0:
            self.current_input = self.current_input[0:len(self.current_input) - 1]
            self.reload_input_field()


    def equal_input(self):
        if self.current_input != '' and self.last_input != '':
            self.current_input = calculate(self.last_input, self.current_input, self.operation)
            self.operation = ''
            self.last_input = ''
            self.reload_input_field()
            self.reload_answer_field(self.current_input)
            self.pressed_equal = True

    def test_func(self):
        lbl = Label(text='test', size_hint_y=None, height=40)
        self.ids['history'].add_widget(lbl)
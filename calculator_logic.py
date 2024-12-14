from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from constants import OPERATIONS
from calculation import calculate

class Calculator(BoxLayout):
    memory = 0
    result = 0

    last_operation = None
    last_integer = ''
    last_input = {'is_operation': False, 'value': ''}

    def input_from_user(self, user_input, is_operation=False):
        if bool(is_operation):
            self.operation_entered(user_input)
        else:
            self.integer_entered(user_input)


    def operation_entered(self, user_input):
        self.last_operation = user_input

    def integer_entered(self, user_input):
        if not self.last_input['is_operation']:
            self.last_input['value'] = user_input
            self.last_input['is_operation'] = False
            self.last_integer = self.last_integer + user_input
            self.reload_input_field()


        else:
            result = calculate()

    def reload_input_field(self):
        if self.last_integer == '':
            self.ids['result_field'].text = '0'
            return

        self.ids['result_field'].text = self.last_integer

    def delete(self):
        if len(self.last_integer) > 0:
            self.last_integer = self.last_integer[0:len(self.last_integer) - 1]
            self.reload_input_field()


    def test_func(self):
        lbl = Label(text='test', size_hint_y=None, height=40)
        self.ids['history'].add_widget(lbl)
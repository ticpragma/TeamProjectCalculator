from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class Calculator(BoxLayout):
    memory = 0
    current_input = {'input': None, 'is_operation': None}


    def input(self, user_input, is_operation=False):
        if is_operation:
            self.pressed_operation(self, user_input)
        else:
            self.entered_integer(self, user_input)

    def pressed_operation(self, user_input):
        check_operation(self, user_input)

    def entered_integer(self, user_input):


    def check_operation(self, user_input):


    def test_func(self):
        lbl = Label(text='test', size_hint_y=None, height=40)
        self.ids['history'].add_widget(lbl)
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class Calculator(BoxLayout):
    memory = 0
    current_input = ''

    def test_func(self):
        lbl = Label(text='test', size_hint_y=None, height=40)
        self.ids['history'].add_widget(lbl)
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

class MyLayout(BoxLayout):
    pass

class MyApp(App):
    def build(self):
        return MyLayout()

if __name__ == '__main__':
    MyApp().run()

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from PDapp.algorithm import Distinguish
from kivy.graphics import Color, Rectangle


class Screen(Widget):
    def __init__(self, **kwargs):
        super(Screen, self).__init__(**kwargs)
        self.result_label = None
        self.result = None

    def get_result(self):
        obj = Distinguish(int(self.fo_input.text),
                          int(self.fhi_input.text),
                          int(self.flo_input.text))
        self.result = obj.get_result
        self.result_label = Label(font_size=35,
                                  pos=(360, 50),
                                  color=(255, 255, 255, 1))
        self.result_label.text = self.result
        self.add_widget(self.result_label)


class MyApp(App):
    def build(self):
        self.root = root = Screen()
        root.bind(size=self._update_rect,
                  pos=self._update_rect)

        with root.canvas.before:
            Color(0, 250, 154, 1)
            self.rect = Rectangle(size=root.size,
                                  pos=root.pos)
        return root

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size


if __name__ == '__main__':
    MyApp().run()
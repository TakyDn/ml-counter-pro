from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout

class SplashScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation="vertical")
        self.logo = Image(source="logo.png")
        layout.add_widget(self.logo)
        self.add_widget(layout)

    def on_enter(self):
        Clock.schedule_once(self.mudar_tela, 3)

    def mudar_tela(self, dt):
        self.manager.current = "principal"

class TelaPrincipal(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation="vertical")
        titulo = Label(text="ML COUNTER PRO", font_size=30)
        layout.add_widget(titulo)
        self.add_widget(layout)

class MLApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(SplashScreen(name="splash"))
        sm.add_widget(TelaPrincipal(name="principal"))
        return sm

if __name__ == "__main__":
    MLApp().run()

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.utils import get_color_from_hex

class HolaMundoApp(App):
    def build(self):
        Window.clearcolor = get_color_from_hex('#2E86C1')
        
        layout = BoxLayout(
            orientation='vertical',
            spacing=30,
            padding=50
        )
        
        self.boton = Button(
            text='[size=24]¡Presiona Aquí![/size]',
            markup=True,
            size_hint=(0.8, 0.2),
            pos_hint={'center_x': 0.5},
            background_color=get_color_from_hex('#3498DB'),
            background_normal='',
            color=(1, 1, 1, 1),
            bold=True
        )
        self.boton.bind(on_press=self.mostrar_mensaje)
        
        layout.add_widget(self.boton)
        return layout

    def mostrar_mensaje(self, instance):
        self.root.add_widget(
            Label(
                text='[b][size=36]¡Hola Mundo![/size][/b]',
                markup=True,
                color=(1, 1, 1, 1)
            )
        )

if __name__ == '__main__':
    HolaMundoApp().run()
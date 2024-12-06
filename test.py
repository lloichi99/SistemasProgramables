from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.graphics import Color, Rectangle
import serial
import time


arduino_port = 'COM5'

ser = serial.Serial(arduino_port, 9600, timeout=1)
time.sleep(2)


class HomePage(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        # Crear un layout principal
        main_layout = BoxLayout(orientation='vertical', spacing=30, padding=30)
        
        # Título de la aplicación
        title_label = Label(
           
            text='Control de Motor Paso a Paso', 
            font_size='24sp', 
            color=(0.1, 0.1, 0.1, 1),
            bold=True
        )
        
        # Layout para los botones
        button_layout = BoxLayout(
            orientation='vertical', 
            spacing=15, 
            size_hint_y=None, 
            height=350
        )
        
        # Crear botones con estilo mejorado
        button_styles = {
            'background_color': (0.2, 0.6, 0.86, 1),  # Color azul claro
            'color': (1, 1, 1, 1),  # Texto blanco
            'font_size': '18sp',
            'size_hint': (0.7, None),
            'height': 70,
            'pos_hint': {'center_x': 0.5}
        }
        
        # Botones de control
        buttons_info = [
            ('Wave Drive', self.wave_drive_action),
            ('Doble Torque', self.double_torque_action),
            ('Medio Paso', self.half_step_action),
            ('Reversa', self.reverse_action)
        ]
        
        # Crear y configurar botones
        for text, action in buttons_info:
            btn = Button(text=text, **button_styles)
            btn.bind(on_press=action)
            button_layout.add_widget(btn)
        
        # Agregar elementos al layout principal
        main_layout.add_widget(Label(size_hint_y=0.2))  # Espacio superior
        main_layout.add_widget(title_label)
        main_layout.add_widget(button_layout)
        main_layout.add_widget(Label(size_hint_y=0.2))  # Espacio inferior
        
        # Agregar fondo con color suave
        with self.canvas.before:
            Color(0.95, 0.95, 0.95, 1)  # Color de fondo gris claro
            self.rect = Rectangle(size=self.size, pos=self.pos)
        
        # Actualizar el fondo si el tamaño cambia
        self.bind(size=self._update_rect, pos=self._update_rect)
        
        self.add_widget(main_layout)
    
    def _update_rect(self, instance, *args):
        self.rect.pos = instance.pos
        self.rect.size = instance.size
    
    # Métodos de acción (igual que antes)
    def wave_drive_action(self, instance):
        ser.write("1".encode())
        print("Wave Drive activado")
    
    def double_torque_action(self, instance):
        ser.write("2".encode())
        print("Doble Torque activado")
    
    def half_step_action(self, instance):
        ser.write("3".encode())
        print("Medio Paso activado")
    
    def reverse_action(self, instance):
        ser.write("4".encode())
        print("Reversa activada")

class ControlApp(App):
    def build(self):
        # Configurar el tamaño de la ventana
        Window.size = (350, 600)
        Window.clearcolor = (0.95, 0.95, 0.95, 1)
        
        # Crear screen manager
        sm = ScreenManager()
        home_page = HomePage(name='home')
        sm.add_widget(home_page)
        
        return sm

# Ejecutar la aplicación
if __name__ == '__main__':
    ControlApp().run()
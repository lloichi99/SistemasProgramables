from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class ControlApp(App):
    def build(self):
        # Crear el diseño principal
        layout = BoxLayout(orientation='vertical', spacing=10, padding=20)
        
        # Crear botones
        wave_drive_btn = Button(text="Wave Drive", font_size=20)
        double_torque_btn = Button(text="Doble Torque", font_size=20)
        half_step_btn = Button(text="Medio Paso", font_size=20)
        reverse_btn = Button(text="Reversa", font_size=20)
        
        # Asignar funciones a los botones
        wave_drive_btn.bind(on_press=self.wave_drive_action)
        double_torque_btn.bind(on_press=self.double_torque_action)
        half_step_btn.bind(on_press=self.half_step_action)
        reverse_btn.bind(on_press=self.reverse_action)
        
        # Agregar botones al diseño
        layout.add_widget(wave_drive_btn)
        layout.add_widget(double_torque_btn)
        layout.add_widget(half_step_btn)
        layout.add_widget(reverse_btn)
        
        return layout

    # Acciones para cada botón
    def wave_drive_action(self, instance):
        print("Wave Drive activado")
    
    def double_torque_action(self, instance):
        print("Doble Torque activado")
    
    def half_step_action(self, instance):
        print("Medio Paso activado")
    
    def reverse_action(self, instance):
        print("Reversa activada")

# Ejecutar la aplicación
if __name__ == '__main__':
    ControlApp().run()

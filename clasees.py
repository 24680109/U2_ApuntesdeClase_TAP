import flet as ft

# 1. Definición de la Clase de Modelo (Datos)
class Usuario:
    def __init__(self, nombre, rol, color_borde=ft.Colors.BLUE):
        self.nombre = nombre
        self.rol = rol
        self.color_borde = color_borde

# 2. Definición del componente personalizado
class TarjetaPerfil(ft.Container):
    def __init__(self, modelo_usuario):
        super().__init__()
        # Recibimos el objeto de la clase Usuario
        self.u = modelo_usuario
        
        self.content = ft.Column(
            controls=[
                ft.Text(self.u.nombre, weight=ft.FontWeight.BOLD, size=20),
                ft.Text(self.u.rol, italic=True),
                ft.ElevatedButton("Ver Perfil", on_click=self.saludar)
            ],
            tight=True
        )
        
        # Configuración visual del Container
        self.border = ft.border.all(2, self.u.color_borde)
        self.padding = 10
        self.border_radius = 10
        self.width = 200

    def saludar(self, e):
        # Acceso a los datos a través del objeto guardado
        print(f"Interactuando con el componente de {self.u.nombre}")

# 3. Función principal
def main(page: ft.Page):
    page.title = "Unidad 2: Clases y Componentes"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # Creamos las instancias de la clase de datos
    ana = Usuario("Ana García", "Desarrolladora Senior", ft.Colors.GREEN)
    carlos = Usuario("Carlos Ruiz", "Arquitecto de Software")

    # Pasamos los objetos a los componentes de UI
    page.add(
        ft.Text("Lista de Usuarios", size=30, weight="bold"),
        ft.Row(
            [TarjetaPerfil(ana), TarjetaPerfil(carlos)], 
            alignment=ft.MainAxisAlignment.CENTER
        )
    )

if __name__ == "__main__":
    ft.app(target=main)
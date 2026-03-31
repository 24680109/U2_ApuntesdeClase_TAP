import flet as ft

# 1. Modelo de Datos (Capa de Lógica)
# Se define un arreglo con 5 productos como exige la competencia [cite: 9, 32]
lista_productos = [
    {"id": 1, "nombre": "Laptop Pro", "descripcion": "16GB RAM, 512GB SSD", "precio": 1200.0, "imagen": "laptop.jpg"},
    {"id": 2, "nombre": "Mouse Gamer", "descripcion": "Inalámbrico RGB", "precio": 45.0, "imagen": "mouse.jpg"},
    {"id": 3, "nombre": "Teclado Mecánico", "descripcion": "Switch Blue RGB", "precio": 80.0, "imagen": "teclado.jpg"},
    {"id": 4, "nombre": "Monitor 4K", "descripcion": "27 pulgadas IPS", "precio": 350.0, "imagen": "icon.png"}, # Usando tus archivos
    {"id": 5, "nombre": "Pack Accesorios", "descripcion": "Kit de inicio", "precio": 120.0, "imagen": "splash_android.png"}, # Usando tus archivos
]

# 2. El Componente Reutilizable (Custom Card)
# Clase personalizada que hereda de ft.Container [cite: 12]
class ProductoCard(ft.Container):
    def __init__(self, producto):
        super().__init__()
        # Configuración visual: bordes redondeados, sombra y ancho fijo [cite: 14]
        self.width = 250
        self.padding = 15
        self.bgcolor = ft.colors.WHITE
        self.border_radius = 15
        self.shadow = ft.BoxShadow(blur_radius=12, color=ft.colors.with_opacity(0.1, ft.colors.BLACK))
        
        # Estructura interna del componente [cite: 13]
        self.content = ft.Column([
            # Área de Imagen: carga desde /assets [cite: 15]
            ft.Image(src=producto['imagen'], width=200, height=150, fit=ft.ImageFit.CONTAIN),
            
            # Cuerpo de Texto [cite: 16, 17, 18]
            ft.Text(producto['nombre'], weight=ft.FontWeight.BOLD, size=16), # Título negritas
            ft.Text(producto['descripcion'], size=12, color=ft.colors.GREY_700), # Descripción corta
            ft.Text(f"${producto['precio']}", color=ft.colors.GREEN_700, weight=ft.FontWeight.BOLD, size=14), # Precio destacado
            
            # Barra de Acciones [cite: 19]
            ft.Row([
                ft.IconButton(icon=ft.icons.FAVORITE_BORDER, icon_color=ft.colors.RED_400), # Favorito visual [cite: 20]
                ft.ElevatedButton("Agregar", icon=ft.icons.SHOPPING_CART_OUTLINED) # Botón carrito [cite: 21]
            ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN)
        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER)

# 3. Interfaz de Usuario Principal (GUI) [cite: 22]
def main(page: ft.Page):
    page.title = "TechStore - Catálogo"
    page.bgcolor = ft.colors.GREY_50
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 30
    
    # Identidad: Encabezado con estilo coherente [cite: 24]
    header = ft.Container(
        content=ft.Text("TECNOLOGÍA REUTILIZABLE", size=32, weight=ft.FontWeight.W_900, color=ft.colors.BLUE_GREY_900),
        margin=ft.margin.only(bottom=20)
    )
    
    # Layout: Cuadrícula que se ajusta al ancho (Responsive) [cite: 23]
    grid = ft.ResponsiveRow(
        spacing=20,
        run_spacing=20,
    )
    
    # Generación dinámica de componentes [cite: 30]
    for p in lista_productos:
        # Cada tarjeta ocupa columnas dependiendo del tamaño de pantalla
        grid.controls.append(
            ft.Column([ProductoCard(p)], col={"sm": 12, "md": 6, "lg": 4, "xl": 3})
        )
    
    page.add(header, grid)

# Ejecución vinculando la carpeta de recursos 
ft.app(target=main, assets_dir="assets")
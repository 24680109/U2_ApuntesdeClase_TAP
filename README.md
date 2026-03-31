# U2_ApuntesdeClase_TAP
# Unidad 2: Componentes y Librerías

## Introducción

En el desarrollo de software moderno, el uso de componentes y librerías es fundamental para mejorar la eficiencia, organización y reutilización del código. Estas herramientas permiten a los programadores evitar escribir todo desde cero, facilitando la creación de aplicaciones más complejas en menor tiempo.

De acuerdo con diversas fuentes como UNIR (2023) y KeepCoding, las librerías representan conjuntos de funciones previamente desarrolladas que ayudan a resolver problemas comunes, mientras que los componentes permiten estructurar mejor un programa dividiéndolo en partes reutilizables.

---

# 2.1 Definición conceptual de componentes y librerías

Un **componente** es una unidad de software independiente que realiza una función específica dentro de un sistema. Puede ser reutilizado en diferentes partes del programa o incluso en distintos proyectos.

Los componentes pueden clasificarse en:

* **Componentes visuales:** elementos de interfaz como botones, tarjetas o formularios.
* **Componentes no visuales:** clases, funciones o estructuras lógicas.

Por otro lado, una **librería** es un conjunto de funciones, clases o módulos que han sido previamente desarrollados para facilitar tareas específicas. Según DevCamp, las librerías permiten a los desarrolladores centrarse en la lógica del problema en lugar de programar todo desde cero.

### Importancia

Según KeepCoding, el uso de librerías permite:

* Reducir el tiempo de desarrollo
* Disminuir errores
* Mejorar la calidad del software

Además, las bibliotecas de componentes ayudan a mantener consistencia en el diseño y funcionalidad de una aplicación.

---

## 🔹 Ejemplo aplicado (Clases y Componentes)

Archivo: `clasees.py`

```python
import flet as ft

class Usuario:
    def __init__(self, nombre, rol, color_borde=ft.Colors.BLUE):
        self.nombre = nombre
        self.rol = rol
        self.color_borde = color_borde

class TarjetaPerfil(ft.Container):
    def __init__(self, modelo_usuario):
        super().__init__()
        self.u = modelo_usuario
        
        self.content = ft.Column(
            controls=[
                ft.Text(self.u.nombre, weight=ft.FontWeight.BOLD, size=20),
                ft.Text(self.u.rol, italic=True),
                ft.ElevatedButton("Ver Perfil", on_click=self.saludar)
            ]
        )
        
        self.border = ft.border.all(2, self.u.color_borde)
        self.padding = 10
        self.border_radius = 10

    def saludar(self, e):
        print(f"Interactuando con {self.u.nombre}")

def main(page: ft.Page):
    ana = Usuario("Ana García", "Desarrolladora")
    carlos = Usuario("Carlos Ruiz", "Arquitecto")

    page.add(
        ft.Row([TarjetaPerfil(ana), TarjetaPerfil(carlos)])
    )

ft.app(target=main)
```

Este ejemplo muestra cómo un componente (`TarjetaPerfil`) puede reutilizarse con diferentes datos.

---

# 2.2 Uso de librerías proporcionadas por el lenguaje

Las librerías proporcionadas por los lenguajes de programación contienen herramientas que permiten realizar tareas complejas de manera sencilla.

Por ejemplo, en Python existen librerías como:

* `matplotlib` para gráficos
* `flet` para interfaces
* `random` para generación de datos

Según UNIR, estas librerías permiten acelerar el desarrollo y mejorar la eficiencia del código.

---

## 🔹 Ejemplo aplicado (Dashboard con gráficas)

Archivo: `grafica.py`

```python
import matplotlib.pyplot as plt
import flet as ft
import flet_charts as fch
import random

def generar_grafica_barras():
    productos = ['A', 'B', 'C', 'D']
    ventas = [25, 30, 45, 10]
    fig, ax = plt.subplots()
    ax.bar(productos, ventas)
    return fig

def main(page: ft.Page):
    fig = generar_grafica_barras()
    page.add(fch.MatplotlibChart(figure=fig))

ft.app(target=main)
```

Este ejemplo demuestra el uso de múltiples librerías para crear una interfaz visual con gráficos.

---

# 2.3 Creación de componentes definidos por el usuario

La creación de componentes personalizados permite encapsular funcionalidades y reutilizarlas en diferentes partes del sistema.

Según Torresburriel, las librerías de componentes ayudan a mantener consistencia visual y funcional en las aplicaciones.

---

## 🔹 Ejemplo aplicado (Catálogo de productos)

Archivo: `catalogo.py`

```python
import flet as ft

productos = [
    {"n": "Laptop Pro", "p": 1200},
    {"n": "Mouse Gamer", "p": 45},
]

class ProductoCard(ft.Container):
    def __init__(self, prod):
        super().__init__()
        
        self.content = ft.Column([
            ft.Text(prod['n']),
            ft.Text(f"${prod['p']}"),
            ft.ElevatedButton("Agregar")
        ])

def main(page: ft.Page):
    for p in productos:
        page.add(ProductoCard(p))

ft.app(target=main)
```

Este ejemplo muestra cómo crear componentes reutilizables para mostrar información de productos.

---

# 2.4 Creación y uso de librerías propias

Las librerías propias permiten organizar el código en módulos reutilizables.

Según InabaWeb, esto mejora la estructura del programa y facilita su mantenimiento.

### Ejemplo conceptual

```python
from componentes import ProductoCard
```

Esto permite reutilizar componentes en distintos proyectos sin duplicar código.

---

# Conclusión

El uso de componentes y librerías es esencial en la programación moderna, ya que permite desarrollar aplicaciones más eficientes, organizadas y escalables. Además, la creación de componentes propios ayuda a mejorar la estructura del código y fomenta buenas prácticas de desarrollo.




---

# Bibliografía

* Pulgarin, V. (2025, 20 diciembre). Qué es una Librería de Programación y Para qué se Utiliza. Roco Agencia SEO y SEM. https://agenciaroco.com/que-es-una-libreria-de-programacion/?utm_source=chatgpt.com
* Torresburriel Estudio. (2024, 16 abril). ¿Qué son las librerías de componentes? | Torresburriel Estudio. Blog - UX Torresburriel Estudio. https://torresburriel.com/weblog/librerias-de-componentes/?utm_source=chatgpt.com
* Desarrollado con www.gesio.com. (s. f.). ¿Qué es una biblioteca de componentes? INDIELEC - Software CAD y CAE Para Ingeniería. https://www.indielec.com/que-es-una-biblioteca-de-componentes-blog-4-50-243/?utm_source=chatgpt.com
* Inába, S. (2023, 30 diciembre). Bibliotecas, Librerías y Módulos en Programación: Diferencias e Importancia. Soluciones Inába. https://www.inabaweb.com/bibliotecas-librerias-y-modulos-en-programacion-diferencias-e-importancia/?utm_source=chatgpt.com
* Salgado, L. G. (2025, 28 enero). Librerías en programación: Qué son y cuáles son las mejores. KeepCoding Bootcamps. https://keepcoding.io/blog/librerias-en-programacion-que-son-las-mejores/?utm_source=chatgpt.com
  

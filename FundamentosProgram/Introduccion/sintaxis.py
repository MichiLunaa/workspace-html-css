"""
Variables y Tipos de Datos:
En Python, las variables son etiquetas para los datos. No necesitas especificar el tipo, Python lo deduce.
"""

variable_entera = 30  # Variable entera (número sin decimales)
variable_decimal = 6.5  # Variable decimal (número con decimales)
variable_texto = "Hola Mundo!"  # Variable de texto (cadena de caracteres)
variable_booleana = True  # Variable booleana (Verdadero o Falso)

"""
Operadores:
Símbolos para realizar operaciones con variables y valores.
"""
resultado_suma = variable_entera + variable_decimal  # Suma de variables
comparacion = (
    variable_entera > variable_decimal
)  # Comparación (mayor que) - el resultado es True o False

"""
Entrada y Salida:
`input()`: Permite al usuario ingresar datos.
`print()`: Muestra información en la pantalla.
"""
nombre_usuario = input(
    "Por favor, ingresa tu nombre: "
)  # Pide al usuario que ingrese su nombre y lo guarda
print(
    "Hola, " + nombre_usuario + "! Este es tu primer programa en Python."
)  # Saluda al usuario con su nombre

"""
Estructuras de Control de Decisiones (if-elif-else):
Permiten ejecutar código diferente según si se cumplen ciertas condiciones.
"""
if variable_booleana:  # Si la variable_booleana es True
    print("La variable booleana es verdadera.")
elif (
    resultado_suma < 10
):  # Si la condición anterior es False Y resultado_suma es menor que 10
    print("La suma es menor que 10.")
else:  # Si ninguna de las condiciones anteriores es True
    print("Ninguna de las condiciones anteriores se cumple.")

"""
Colecciones de Datos (array):
Formas de organizar y almacenar múltiples datos.
- Listas (`[]`): Ordenadas, modificables.
- Tuplas (`()`): Ordenadas, inmutables (no se pueden cambiar después de crear).
- Diccionarios (`{}`): Pares clave-valor.
- Conjuntos (`{}` o `set()`): No ordenados, elementos únicos.
"""
lista_numeros = [1, 2, 3, 4, 5]  # Lista de números
tupla_colores = ("rojo", "verde", "azul")  # Tupla de colores
diccionario_edades = {
    "Juan": 25,
    "María": 30,
    "Carlos": 22,
}  # Diccionario de edades (nombre: edad)
conjunto_elementos = {1, 2, 3, 4, 5}  # Conjunto de números únicos

"""
Funciones:
Bloques de código reutilizables que realizan una tarea específica.
"""


def saludar(
    nombre,
):  # Define una función llamada saludar que toma un parámetro 'nombre'
    return "¡Hola, " + nombre + "!"  # La función devuelve un saludo personalizado


mensaje_saludo = saludar(
    "Estudiante"
)  # Llama a la función saludar con el argumento "Estudiante" y guarda el resultado

"""
Manejo de Errores (try-except-finally):
Permite manejar errores para que el programa no se detenga.
"""
try:  # Intenta ejecutar este código
    resultado_division = 0 / 0  # Esto causará un error de división por cero
except ZeroDivisionError:  # Si ocurre un error ZeroDivisionError, ejecuta este bloque
    print("¡Error! No se puede dividir por cero.")
finally:  # Este bloque se ejecuta siempre, haya error o no
    print("Bloque 'finally': Este código se ejecuta siempre, haya o no haya errores.")

"""
Trabajo con Archivos (with open):
Permite leer y escribir en archivos de forma segura.
`with open(...) as archivo:` asegura que el archivo se cierre automáticamente.
"""
with open(
    "archivo.txt", "w"
) as archivo:  # Abre el archivo "archivo.txt" en modo escritura ('w')
    archivo.write("¡Hola desde un archivo!")  # Escribe texto en el archivo

"""
Módulos y Bibliotecas (import math):
Colecciones de código adicional para extender la funcionalidad de Python.
"""
import math  # Importa el módulo 'math' para funciones matemáticas

raiz_cuadrada = math.sqrt(
    16
)  # Usa la función sqrt() del módulo math para calcular la raíz cuadrada

"""
Programación Orientada a Objetos (POO) (class MiClase):
Organiza el código usando "clases" y "objetos".
"""


class MiClase:  # Define una clase llamada MiClase
    def __init__(
        self, atributo
    ):  # Método constructor (__init__) para inicializar objetos de la clase
        self.atributo = atributo  # Crea un atributo llamado 'atributo' para el objeto

    def mostrar_atributo(self):  # Método para mostrar el valor del atributo
        print("El valor del atributo es:", self.atributo)


"""
Manejo de Cadenas (Strings):
Funciones y métodos para trabajar con cadenas de texto.
"""
longitud_cadena = len("Python")  # Función len() para obtener la longitud de una cadena
mayusculas = "hola".upper()  # Método upper() para convertir a mayúsculas
minusculas = "HOLA".lower()  # Método lower() para convertir a minúsculas
reemplazo = "python es divertido".replace(
    "divertido", "increíble"
)  # Método replace() para reemplazar subcadenas

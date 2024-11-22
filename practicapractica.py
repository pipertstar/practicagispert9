def calcular_promedio(notas):
    """
    Calcula el promedio de una lista de notas.

    :param notas: lista de números (notas)
    :return: el promedio de las notas
    """
    if not notas:
        return 0  # Retorna 0 si la lista está vacía
    return sum(notas) / len(notas)

# Ejemplo de uso
notas = [8, 7, 9.5, 10, 6]
promedio = calcular_promedio(notas)
print(f"El promedio de las notas es: {promedio:.2f}")


def es_color_primario(color):
    """
    Determina si un color es primario.

    :param color: string, el nombre del color (ej. "rojo", "azul", "amarillo")
    """
    # Lista de colores primarios
    colores_primarios = {"rojo", "azul", "amarillo"}

    # Comprobar si el color está en la lista de primarios
    if color.lower() in colores_primarios:
        print(f"El color {color} es primario.")
    else:
        print(f"El color {color} no es primario.")

# Ejemplo de uso
es_color_primario("rojo")       # Salida: El color rojo es primario.
es_color_primario("verde")      # Salida: El color verde no es primario.
es_color_primario("Amarillo")   # Salida: El color Amarillo es primario.

def numero_mayor(numeros):
    """
    Determina el número mayor en una lista de números.

    :param numeros: lista de números
    :return: el número mayor de la lista
    """
    if not numeros:
        print("La lista está vacía. No se puede determinar el número mayor.")
        return None
    
    mayor = max(numeros)
    print(f"El número mayor en la lista es: {mayor}")
    return mayor

# Ejemplo de uso
numeros = [3, 7, 2, 9, 5]
numero_mayor(numeros)  # Salida: El número mayor en la lista es: 9


def dibujar_rectangulo(filas, columnas):
    """
    Dibuja un rectángulo de caracteres con las filas y columnas dadas.

    :param filas: Número de filas del rectángulo.
    :param columnas: Número de columnas del rectángulo.
    """
    if filas <= 0 or columnas <= 0:
        print("Las filas y columnas deben ser mayores a 0.")
        return
    
    for _ in range(filas):
        print("*" * columnas)

# Ejemplo de uso
filas = int(input("Ingrese el número de filas: "))
columnas = int(input("Ingrese el número de columnas: "))
dibujar_rectangulo(filas, columnas)

# Asi quedaria 
******
******
******
******


def calcular_factorial(numero):
    """
    Calcula el factorial de un número entero positivo.

    :param numero: Número entero positivo.
    :return: El factorial del número.
    """
    if numero < 0:
        print("El número debe ser un entero positivo.")
        return None
    elif numero == 0 or numero == 1:
        return 1
    
    factorial = 1
    for i in range(2, numero + 1):
        factorial *= i
    
    return factorial

# Ejemplo de uso
numero = int(input("Ingrese un número entero positivo: "))
resultado = calcular_factorial(numero)
if resultado is not None:
    print(f"El factorial de {numero} es: {resultado}")

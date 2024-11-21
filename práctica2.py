# EJERCICIO 1: Función que calcula el promedio de N notas
def calcular_promedio(notas):
    if len(notas) == 0:
        return 0
    suma = sum(notas)
    promedio = suma / len(notas)
    return promedio

# Solicitar al usuario que ingrese las notas
notas = []
cantidad_notas = int(input("¿Cuántas notas deseas ingresar? "))

for i in range(cantidad_notas):
    nota = float(input(f"Ingrese la nota {i+1}: "))
    notas.append(nota)

promedio = calcular_promedio(notas)
print(f"El promedio de las notas es: {promedio}")

# EJERCICIO 2: Crear una función que determine si una función es primaria o no, se debe imprimir por pantalla
# la leyenda "el color x es primario", o "el color x no es primario"

def es_color_primario(color):
    colores_primarios = ["rojo", "azul", "amarillo"]
    if color.lower() in colores_primarios:
        print(f"El color {color} es primario")
    else:
        print(f"El color {color} no es primario")

# Solicitar al usuario que ingrese un color
color_usuario = input("Ingresa un color: ")
es_color_primario(color_usuario)

# EJERCICIO 3: Crear una función que determine qué número de una serie de N números es mayor

def encontrar_mayor(numeros):
    if not numeros:
        return None  # Retorna None si la lista está vacía
    mayor = numeros[0]
    for numero in numeros:
        if numero > mayor:
            mayor = numero
    return mayor

# Solicitar al usuario que ingrese los números
numeros = []
cantidad = int(input("¿Cuántos números deseas ingresar? "))

for _ in range(cantidad):
    numero = float(input("Ingresa un número: "))
    numeros.append(numero)

# Encontrar y mostrar el número mayor
mayor_numero = encontrar_mayor(numeros)
print("El número mayor es:", mayor_numero)

# EJERCICIO 4: Crear una función que dibuje un rectángulo de X filas y X columnas determinadas por el usuario

def draw_rectangle(rows, cols, char):
    for i in range(rows):
        print(char * cols)

# Solicitar al usuario el número de filas, columnas y el carácter
rows = int(input("Ingrese el número de filas: "))
cols = int(input("Ingrese el número de columnas: "))
char = input("Ingrese el carácter para dibujar el rectángulo: ")

# Dibujar el rectángulo con los valores ingresados por el usuario
draw_rectangle(rows, cols, char)


# Ejercicio 5: crear una función que calcule el factorial de un número entero positivo

def factorial(n):
    if n < 0:
        raise ValueError("El número debe ser un entero positivo")
    elif n == 0 or n == 1:
        return 1
    else:
        resultado = 1
        for i in range(2, n + 1):
            resultado *= i
        return resultado

# Solicitar al usuario que ingrese un número
numero = int(input("Ingresa un número entero positivo: "))
print(f"El factorial de {numero} es {factorial(numero)}")

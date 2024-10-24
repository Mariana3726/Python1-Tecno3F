# Realizar un programa que me diga si un número es par o impar.

# Pedimos al usuario que ingrese un número
numero = int(input("Ingrese un número: "))
# para saber si el número es par o impar
if numero % 2 == 0:
    print(f"El número {numero} es par")
else:
    print(f"El número {numero} es impar")


# Realizar un programa que genere la tabla de multiplicar de un número ingresado por el usuario(del 1 al 10).
# pedimos al usuario que ingrse un número
numero1 = int(input("Ingrese un número: "))
# se genera y muestra la tabla
print(f"Tabla de multiplicar del número {numero1}: ")
for i in range(1,10):
    print(f"{numero1} x {i} = {numero1 * i}")


# Realizar un programa que le pida al usuario su nombre y su edad, e imprima si es mayor de edad.
nombre = input("Escribe tu nombre: ")
edad = int(input("Ingresa tu edad: "))
if edad >= 18:
    print(f"{nombre} sos mayor de edad")
else:
    print(f"{nombre} no sos mayor de edad")


# Realizar un programa donde el usuario ingrese una palabra y un número e imprima por pantalla la palabra ingresada tantas
# veces como el número ingresado.
palabra = input("Ingresa una palabra: ")
numero3 = int(input("Ingresa un número: "))
for i in range(numero3):
    print(palabra)

# Realizar un programa que sume los números ingresados por el usuario hasta que se ingrese un cero. Al final nos debe mostrar
# la suma por pantalla.
suma_total = 0
while True:
    numero4 = int(input("Introduce un número (0 para terminar): "))
    if numero4 == 0:
        break
    suma_total += numero4
print(f"La suma total es: {suma_total}")
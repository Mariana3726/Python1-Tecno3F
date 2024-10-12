#PRÁCTICA
#Realizar un programa que le pida al usuario su nombre y lo muestre en mayúsculas

nombre = str(input("Ingrese su nombre: "))
nombre = nombre.upper()
print("Tu nombre en mayúscula es: "+nombre)

#Realizar un programa que le pida al usuario un número y le sume 5, el resultado debe mostrarse por pantalla

numero = int(input("Ingrese un número: "))
resultado = numero + 5
print("El resultado de la suma es: ",resultado)

#Realizar un programa que le pida al usuario su nombre y apellido, mostrarlo en un mensaje de bienvenida.

nombre = str(input("Ingrese su nombre: "))
apellido = str(input("Ingrese su apellido: "))
print("Bienvenid@!!! ",nombre+' '+apellido)

#Ingresar 5 números y calcular su promedio, el resultado mostrarlo por pantalla

numeros = []
for i in range(5):
    numero = float(input(f"Ingrese el número {i+1}: "))
    numeros.append(numero)
promedio = sum(numeros) / len(numeros)
print("El promedio de los números ingresados es: ",promedio)

#Realizar un programa que muestre cualquier frase ingresada por el usuario en minúscula

frase = str(input("Escriba una frase: "))
frase = frase.lower()
print('Tu frase en minúsculas es: '+frase)

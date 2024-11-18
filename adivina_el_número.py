
import random

numero_secreto = random.randint(1, 50)

print("""
    ###################################  
            ¡Bienvenidos!
    Vamos a jugar a Adivinar el Número
    ###################################
\n""")

for intento in range(5):
    n = input(f"Intento {intento + 1} de 5: Ingrese un número entre 1 y 50: ")

    if n.isdigit():
        n = int(n)
        if 1 <= n <= 50:
            if n > numero_secreto:
                print("El número secreto es MENOR")
            elif n < numero_secreto:
                print("El número secreto es MAYOR")
            else:
                print("¡Felicidades! Adivinaste el número")
                break
        else:
            print("El número ingresado está fuera del rango")
    else:
        print("En este juego solo aceptamos números enteros positivos")
else:
    print(f"Perdiste... El número era: {numero_secreto}")



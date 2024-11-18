while True:
    n = input("Ingrese un numero: ")

    if not(n.isalpha()) and n.isdigit():
        n = int(n)
        if n > 0:
            frase = input("Ingrese una palabra o frase: ")

            print(f"La palabra o frase ingresada tiene {len(frase)} caracteres")

            factorial = 1
            for i in range(1, len(frase) + 1):
                factorial *= i

            print(f"El factorial de {len(frase)} es: {factorial}")

            if (factorial % 2) == 0:
                print("El Factorial es Par")
            else:
                print("El Factorial es Inpar")
        else:
            break
    else:
        break
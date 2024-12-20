import random
import pickle

# Diccionario para almacenar los tickets
tickets = {}

# Cargar tickets desde un archivo
def cargar_tickets():
    try:
        with open('tickets.pkl', 'rb') as file:
            global tickets
            tickets = pickle.load(file)
            print("Tickets cargados exitosamente.")
    except FileNotFoundError:
        tickets = {}
        print("No se encontró el archivo de tickets. Se creará uno nuevo.")
    except EOFError:
        tickets = {}
        print("El archivo de tickets está vacío. Se creará uno nuevo.")

# Guardar tickets en un archivo
def guardar_tickets():
    with open('tickets.pkl', 'wb') as file:
        pickle.dump(tickets, file)
        print("Tickets guardados exitosamente.")

def alta_ticket():
    while True:
        nombre = input("Ingrese su nombre: ")
        sector = input("Ingrese su sector: ")
        asunto = input("Ingrese el asunto: ")
        problema = input("Describa el problema: ")

        numero_ticket = random.randint(1000, 9999)
        tickets[numero_ticket] = {
            "Nombre": nombre,
            "Sector": sector,
            "Asunto": asunto,
            "Problema": problema
        }

        guardar_tickets()

        print(f"\nTicket generado exitosamente!")
        print(f"Número de Ticket: {numero_ticket}")
        print(f"Nombre: {nombre}")
        print(f"Sector: {sector}")
        print(f"Asunto: {asunto}")
        print(f"Problema: {problema}")
        print("\nPor favor, recuerde el número de ticket.\n")

        otro_ticket = input("¿Desea crear otro ticket? (si/no): ").strip().lower()
        if otro_ticket != 'si':
            break

def leer_ticket():
    while True:
        try:
            numero_ticket = int(input("Ingrese el número de ticket: "))
            if numero_ticket in tickets:
                ticket = tickets[numero_ticket]
                print(f"\nNúmero de Ticket: {numero_ticket}")
                print(f"Nombre: {ticket['Nombre']}")
                print(f"Sector: {ticket['Sector']}")
                print(f"Asunto: {ticket['Asunto']}")
                print(f"Problema: {ticket['Problema']}\n")
            else:
                print("Número de ticket no encontrado.\n")
        except ValueError:
            print("Por favor, ingrese un número de ticket válido.\n")

        otro_ticket = input("¿Desea leer otro ticket? (si/no): ").strip().lower()
        if otro_ticket != 'si':
            break

def main():
    cargar_tickets()
    while True:
        print("Menú:")
        print("1. Alta ticket")
        print("2. Leer ticket")
        print("3. Salir")

        opcion = input("Seleccione una opción (1/2/3): ").strip()

        if opcion == '1':
            alta_ticket()
        elif opcion == '2':
            leer_ticket()
        elif opcion == '3':
            confirmacion = input("¿Está seguro que desea salir? (si/no): ").strip().lower()
            if confirmacion == 'si':
                print("Saliendo del programa...")
                break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.\n")

if __name__ == "__main__":
    main()
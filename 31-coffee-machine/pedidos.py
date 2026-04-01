ARCHIVO_PEDIDOS = "pedidos.txt"

def pedir_cafe():
    print("\nElige el café que deseas:")
    print("1. Espresso")
    print("2. Cappuccino")
    print("3. Latte")
    print("4. Americano")

    opcion = input("Selecciona una opción: ")
    cafes = {
        "1": "Espresso",
        "2": "Cappuccino",
        "3": "Latte",
        "4": "Americano"
    }

    if opcion in cafes:
        cafe_elegido = cafes[opcion]
        print(f"\nHas pedido un {cafe_elegido}. ¡Disfrútalo!")

        with open(ARCHIVO_PEDIDOS, "a", encoding="utf-8") as archivo:
            archivo.write(f"{cafe_elegido}\n")
    else:
        print("Opción no válida, por favor selecciona una opción válida")
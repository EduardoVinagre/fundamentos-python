ARCHIVO_PEDIDOS = "pedidos.txt"

def ver_historial():
    print("\nHistorial de pedidos:")
    try:
        with open(ARCHIVO_PEDIDOS, "r", encoding="utf-8") as archivo:
            pedidos = archivo.readlines()
            if pedidos:
                for i, pedido in enumerate(pedidos, start=1):
                    print(f"{i}. {pedido.strip()}")
            else:
                print("No hay pedidos en el historial.")
    except FileNotFoundError:
        print("\nNo se ha encontrado el historial de pedidos. Aún no se han realizado pedidos.")
from menu import mostrar_menu
from pedidos import pedir_cafe
from historial import ver_historial

def main():
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opcion: ")
        if opcion == "1":
            #pedir un cafe
            pedir_cafe()
        elif opcion == "2":
            #ver el historial
            ver_historial()
        elif opcion == "3":
            print("\n Muchas gracias por haber tomado nuestros riquisimos cafés")
            break
        else:
            print("Opción no válida, por favor selecciona una opción válida")

if __name__ == "__main__":
    main()
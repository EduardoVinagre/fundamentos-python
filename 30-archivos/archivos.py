# open(nombre, modo)

# Read (r) - por defecto
# Write (w) - borra el contenido del archivo
# X - crea el archivo, pero si ya existe, lanza un error
# Append (a) - agrega contenido al final del archivo    

try:
    f = open("archivo.txt", "r")
    print(f.readline())
    print(f.readline())
    f.close()
except FileNotFoundError:
    print("El archivo no existe.")


try:
    with open("archivo.txt", "r", encoding="utf-8") as f:
        print(f.readline())
        print(f.readline())
except FileNotFoundError:
    print("El archivo no existe.")
    open("archivo.txt", "x").close()  # Crea el archivo si no existe

try:
    with open("archivo.txt", "a", encoding="utf-8") as f:
        f.write("\n")
        f.write("Hola mundo desde write en el with")  # Esto lanzará un error porque el archivo está abierto en modo lectura
    with open("archivo.txt", "r", encoding="utf-8") as f:
        print(f.read())
except FileNotFoundError:
    print("El archivo no existe.")
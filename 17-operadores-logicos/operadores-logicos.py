import os

def limpiar_pantalla():
    # 'nt' es Windows, 'posix' es Linux/macOS
    os.system('cls || clear')

# Uso
limpiar_pantalla()

x = 5
y = 3
z = 5

print( x == y )  # Igualdad
print( x != y )  # Desigualdad
print( x > y )   # Mayor que
print( x < y )   # Menor que
print( x >= y )  # Mayor o igual que
print( x <= y )  # Menor o igual que

print( x > y and y < z )  # AND lógico
print( x > z or y > z )   # OR lógico
print( not (x == z) )      # NOT lógico

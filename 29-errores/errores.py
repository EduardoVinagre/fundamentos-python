try:
    print(10 / 0)
except ZeroDivisionError:
    print("No se puede dividir por cero")

try:
    print(x)
except NameError:
    print("La variable x no está definida")
finally:
    print("Este bloque se ejecuta siempre")
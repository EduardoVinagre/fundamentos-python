# funcion es un bloque de codigo que solo se ejecuta cuando lo llamamos. Permiten organizar y modularizar el codigo.

def mi_funcion():
    print("Hola, soy una función")

mi_funcion()

def saludar(nombre, nacionalidad="Colombia"):
    print(f"Hola, {nombre} de {nacionalidad}")

def funcion():
    pass


saludar("Juan")
saludar("Maria")
saludar("Carlos", "México")

def sumar(a, b):
    return a + b
resultado = sumar(5, 3)
print(resultado)

funcion()
v = True
f = False

print(v)
print(f)   

print(5>3)
print(5<3)

print(type(v))

print(bool("Hola mundo"))
print(bool(""))  # Cadena vacía
print(bool(" "))  # Cadena vacía
print(bool(" ".strip()))  # Cadena vacía

print(bool(10))
print(bool(["Manzana", "Banana"]))

print(bool(0))
print(bool([]))  # Lista vacía
print(bool({}))  # Diccionario vacío
print(bool(None))  # Valor None

print(isinstance(5, int))
print(isinstance(3.5, int))
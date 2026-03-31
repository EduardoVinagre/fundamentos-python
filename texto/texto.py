print("Hola 'mundo'")
print('Hola "mundo"')

ingles = "I'm learning Python"
print(ingles)

multiples = """Este es un texto
que abarca varias
líneas"""
print(multiples)

palabra = 'Python'
print(len(palabra))  # Longitud de la palabra

texto = "Python es un lenguaje de programación"
estaIncluida = "Python" in texto
print(estaIncluida)  # True

noEstaIncluida = "Java" not in texto
print(noEstaIncluida)  # True

mayusculas = texto.upper()
minusculas = texto.lower()
print(minusculas)
print(mayusculas)
print(texto)

espacios = "   Hola Mundo   "
sinEspacios = espacios.strip()
print(espacios.strip())  # Elimina espacios al inicio y al final
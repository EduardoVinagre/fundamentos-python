texto = "Este es un texto"

print(texto[0])
print(texto[4])

# slicing
print(texto[0:15])
print(texto[:7])
print(texto[5:])
print(texto[5:-2])

curso = "Este curso es de JavaScript, JavaScript es un lenguaje de programación."
print(curso.replace("JavaScript", "Python"))

textoDividido = texto.split(" ")
print(textoDividido)

# Normalizacion

texto2 = " Este texto tiene MAYUSCULAS y minusculas y necesito encontrar ciertas palabras"
print("mayusculas" in texto2.lower())
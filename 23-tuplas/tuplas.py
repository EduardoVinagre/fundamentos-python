# Tupla: Colección ordenada e inmutable de elementos que permiten duplicados. Se definen con paréntesis ().}
# Las tuplas son útiles para almacenar datos que no deben cambiar a lo largo del programa. 

tecnologias = ("Python", "Java", "C++", "JavaScript", "Python") # Se pueden incluir elementos duplicados en una tupla
print(tecnologias) # Imprime toda la tupla
print(tecnologias[0]) # Imprime el primer elemento de la tupla
print(tecnologias[1:3]) # Imprime una porción de la tupla
print(len(tecnologias)) # Imprime la longitud de la tupla
print("Python" in tecnologias) # Verifica si "Python" está en la tupla
print("Ruby" in tecnologias) # Verifica si "Ruby" está en la tupla  

print(len(tecnologias)) # Imprime la longitud de la tupla
print(tecnologias.count("Python")) # Cuenta cuántas veces aparece "Python" en la tupla
print(tecnologias.index("Java")) # Devuelve el índice de la primera aparición de "Java" en la tupla
# Las tuplas no permiten modificar sus elementos, por lo que no se pueden agregar, eliminar o cambiar elementos después de su creación. 

print(type(tecnologias)) # Imprime el tipo de la variable tecnologias, que es <class 'tuple'>  
# Las tuplas son útiles para almacenar datos que no deben cambiar a lo largo del programa, como coordenadas, fechas, etc.

fruta = ("Manzana")
print(type(fruta)) # Imprime el tipo de la variable fruta, que es <class 'str'>, porque al definir una tupla con un solo elemento, se interpreta como una cadena de texto.
fruta = ("Manzana",) # Para definir una tupla con un solo elemento, se debe incluir una coma después del elemento para que se interprete como una tupla.
print(type(fruta)) # Imprime el tipo de la variable fruta, que ahora es <class 'tuple'>, porque se ha definido correctamente como una tupla con un solo elemento.

tupla = ("Python", 5, True)
print(tupla) # Imprime toda la tupla
print(type(tupla)) # Imprime el tipo de la variable tupla, que es <class 'tuple'>, porque contiene elementos de diferentes tipos (cadena, entero y booleano).

x,y,z = tupla # Desempaquetado de tupla: Asigna cada elemento de la tupla a una variable correspondiente
print(x) # Imprime el valor de x, que es "Python"
print(y) # Imprime el valor de y, que es 5
print(z) # Imprime el valor de z, que es True

tupla1 = (1, 2, 3)
tupla2 = (3, 5, 6)
tupla3 = tupla1 + tupla2 # Concatenación de tuplas: Combina dos tuplas en una nueva tupla
print(tupla3) # Imprime la nueva tupla resultante de la concatenación

tupla = ("Python", 5, True)

print(tupla*2)

for item in tupla:
    print(item) # Imprime cada elemento de la tupla en una nueva línea

tuplaAModificar = ("Python", "Javascript","Go")
listaComodin = list(tuplaAModificar) # Convierte la tupla en una lista para poder modificarla
listaComodin.append("c#")
tuplaAModificar = tuple(listaComodin) # Convierte la lista de nuevo en una tupla después de modificarla
print(tuplaAModificar) # Imprime la tupla modificada con el nuevo

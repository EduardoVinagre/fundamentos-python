# Conjunto (set): Collecion no ordenada de elementos unicos (no se puede acceder por índice). Se definen con llaves {} o con la función set().
# Los conjuntos son útiles para almacenar elementos únicos y realizar operaciones matemáticas como unión, intersección, diferencia y diferencia simétrica.

frutas = {"Manzana", "Banana", "Naranja", "Manzana", "Banana"} # Se pueden incluir elementos duplicados, pero solo se almacenará uno de ellos
print(frutas) # Imprime el conjunto, que solo contiene elementos únicos
print("Manzana" in frutas) # Verifica si "Manzana" está en el conjunto
print("Pera" in frutas) # Verifica si "Pera" está en el conjunto    
print(type(frutas)) # Imprime el tipo de la variable frutas, que es <class 'set'>
print(len(frutas)) # Imprime la cantidad de elementos únicos en el conjunto

conjuntos = {"Python", 156, True, 3.14} # Un conjunto puede contener elementos de diferentes tipos
print(conjuntos) # Imprime el conjunto con elementos de diferentes tipos

for item in frutas:
    print(item) # Imprime cada elemento del conjunto en una nueva línea 

for item in conjuntos:
    print(item) # Imprime cada elemento del conjunto en una nueva línea 

# Agregar elementos a un conjunto
# Add
frutas.add("Pera") # Agrega "Pera" al conjunto frutas
print(frutas) # Imprime el conjunto frutas después de agregar "Pera"
# Update
frutas.update(["Kiwi", "Mango"]) # Agrega varios elementos al conjunto frutas. Listas, tuplas o conjuntosprint(frutas) # Imprime el conjunto frutas después de agregar "Kiwi" y "Mango"  

# Eliminar elementos de un conjunto
# Remove
frutas.remove("Banana") # Elimina "Banana" del conjunto frutas. Si el elemento no existe, se genera un error
print(frutas) # Imprime el conjunto frutas después de eliminar "Banana"
# Discard 
frutas.discard("Naranja") # Elimina "Naranja" del conjunto frutas. Si el elemento no existe, no se genera un error
print(frutas) # Imprime el conjunto frutas después de eliminar "Naranja"
# Pop
frutas.pop() # Elimina un elemento aleatorio del conjunto frutas, ya que los conjuntos no tienen un orden definido
print(frutas) # Imprime el conjunto frutas después de eliminar un elemento aleatorio
# Clear
frutas.clear() # Elimina todos los elementos del conjunto frutas, dejándolo vacío
print(frutas) # Imprime el conjunto frutas después de vaciarlo, lo que resulta en un conjunto vacío set()

a = {"a", "b", "c"}
b = {"c", "d", "e"}

print(a.union(b)) # Imprime la unión de los conjuntos a y b, que contiene todos los elementos únicos de ambos conjuntos
print(a.intersection(b)) # Imprime la intersección de los conjuntos a y b, que contiene solo los elementos que están presentes en ambos conjuntos
print(a.difference(b)) # Imprime la diferencia de los conjuntos a y b, que contiene los elementos que están en a pero no están en b
print(a.symmetric_difference(b)) # Imprime la diferencia simétrica de los conjuntos a y b, que contiene los elementos que están en a o en b pero no en ambos conjuntos          

# LISTAS: Las listas son ordenadas, mutables y permiten elementos duplicados. Se definen utilizando corchetes [].

# [indice] -> Acceder a un elemento específico de la lista
# [inicio:fin] -> Acceder a un rango de elementos de la lista

frutas = ['Manzana', 'Banana', 'Naranja', 'Pera']
print(frutas)
print(type(frutas))
print(frutas[0])  # Acceder al primer elemento
print(frutas[1:3])  # Acceder al rango de elementos desde el índice 1 hasta el 3 (sin incluirlo)

frutas[1] = 'Fresa'  # Modificar el segundo elemento de la lista
print(frutas)

lista = [1, 'Hola', 3.14, True]  # Las listas pueden contener diferentes tipos de datos
print(lista)
print(type(lista))

print(len(frutas))  # Obtener la longitud de la lista
print(len(lista))

if 'Manzana' in frutas:  # Verificar si un elemento está en la lista
    print('La manzana está en la lista de frutas.')

vehiculos = ['Auto','Moto','Avion']

# Métodos
# Append (Agregar un elemento al final de la lista)
vehiculos.append('Bicicleta')  # Agregar un elemento al final de la lista
print(vehiculos)

# Insert (Agregar un elemento en una posición específica)
vehiculos.insert(1, 'Barco')  # Agregar un elemento en la posición 1
print(vehiculos)

# Remove (Eliminar un elemento específico de la lista)
vehiculos.remove('Moto')  # Eliminar el elemento 'Moto' de la lista
print(vehiculos)

# Pop (Eliminar y devolver un elemento de la lista)
ultimo_vehiculo = vehiculos.pop()  # Eliminar el último elemento de la lista y devolverlo
print(vehiculos)
print('Vehículo eliminado:', ultimo_vehiculo)

#sort (Ordenar la lista)
vehiculos.sort()  # Ordenar la lista de vehículos alfabéticamente
print(vehiculos)

#reverse (Invertir el orden de la lista)
vehiculos.reverse()  # Invertir el orden de la lista de vehículos
print(vehiculos)

#unir listas
frutas_y_vehiculos = frutas + vehiculos  # Unir las listas de frutas y vehículos
print(frutas_y_vehiculos)

coleccion1 = [1, 2, 3]
coleccion2 = [4, 5, 6]

coleccion3 = coleccion1 + coleccion2  # Unir las dos colecciones
print(coleccion3)

coleccion1.extend(coleccion2)  # Extender la primera colección con los elementos de la segunda colección
print(coleccion1)


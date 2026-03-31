# Esta ordenada a partir de python 3.7
# Es una estructura de datos que almacena pares de clave-valor
# Se pueden usar para almacenar cualquier tipo de datos, incluyendo listas, tuplas, otros diccionarios, etc.
# Se pueden acceder a los valores a través de sus claves
# Se pueden modificar los valores a través de sus claves
# Se pueden eliminar los pares de clave-valor a través de sus claves
# Se pueden agregar nuevos pares de clave-valor a través de sus claves
# Se pueden iterar sobre los pares de clave-valor a través de un bucle for
# Se pueden ordenar los pares de clave-valor a través de sus claves o valores
# Se pueden usar para almacenar datos de forma estructurada, como por ejemplo, un diccionario de personas, donde cada persona es un par de clave-valor, donde la clave es el nombre de la persona y el valor es un diccionario con sus datos personales, como su edad, su dirección, su número de teléfono, etc.    
# Se pueden usar para almacenar datos de forma jerárquica, como por ejemplo, un diccionario de empresas, donde cada empresa es un par de clave-valor, donde la clave es el nombre de la empresa y el valor es un diccionario con sus datos empresariales, como su dirección, su número de teléfono, su número de empleados, etc.

auto = {
    "marca": "Toyota",
    "modelo": "Corolla",
    "año": 2020,
    "color": "Rojo",
    "precio": 20000,
    "características": {
        "motor": "1.8L",
        "transmisión": "Automática",
        "tracción": "Delantera",
        "consumo": "6.5L/100km"
    }
}
print(auto)
print(auto["marca"])
print(auto["características"]["motor"])
auto["precio"] = 19000
print(auto["precio"])
auto["características"]["consumo"] = "6.0L/100km"
print(auto["características"]["consumo"])
auto["color"] = "Azul"
print(auto["color"])
del auto["año"]
print(auto)
auto["año"] = 2021
print(auto)
for clave, valor in auto.items():
    print(f"{clave}: {valor}")  

print(auto.get("marca"))
print(auto.keys())
print(auto.values())
print(auto.items()) 

if "modelo" in auto:
    print("El modelo del auto es:", auto["modelo"])
else:    
    print("El modelo del auto no está disponible.")

auto.update({"año": 2022})
auto.update({"puertas": 4})

auto.update({"año": 2023, "puertas": 4, "color": "Negro"})
print(auto)

auto.pop("puertas")
print(auto)

auto.popitem()
print(auto)

#auto.clear()
print(auto)

for k in auto:
    print(k)

print("----")

for v in auto.values():
    print(v)

print("----")

for k,v in auto.items():
    print(f"{k}: {v}") 


familia = {
    "hijo1": {
        "nombre": "Pedro",
        "edad": 8
    },
    "hijo2": {
        "nombre": "Ana",
        "edad": 6
    },
    "hijo3": {
        "nombre": "Marcelo",
        "edad": 4
    },
}

print(familia["hijo1"]["nombre"])
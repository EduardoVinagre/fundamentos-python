print('-'*50)
palabra = "Python"
for letra in palabra:
    print(letra)

print('-'*50)

adjetivos = ["Rica", "Saludable"]
frutas = ['Manzana', 'Naranja', 'Kiwi']

for adjetivo in adjetivos:
    for fruta in frutas:
        print(fruta, adjetivo)

print('-'*50)

for fruta in frutas:
    for adjetivo in adjetivos:
        print(fruta, adjetivo)

# for fruta in frutas:
#     print(fruta)
# else:
#     print('Ya hemos terminado el bucle for')

# print('-'*50)

# for i in range(10):
#     print(i)

# print('-'*50)

# for i in range(0,10,2):
#     print(i)
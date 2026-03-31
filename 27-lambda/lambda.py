# Lamba es una funcion pequeña y anonima que puede tener muchos argumentos pero solo una expresion.

# Sintaxis: lambda argumentos: expresion

x = lambda a: a + 10
print(x(5))

def mifuncion(n):
    return lambda b: b * n

doble = mifuncion(2)
triple = mifuncion(3)

print(doble(5))
print(triple(5))


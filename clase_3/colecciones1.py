"""
Una colección en Python es una agrupación de elementos, que pueder datos básicos, u otras colecciones

LISTAS

Para poder acceder a un elemento de la lista necesito conocer la posición de ese elemento, en Python los índices empiezan en 0
Son colecciones donde un elemento se puede repetir
Son colecciones mutables 

"""

#nombre = input("Ingrese su nombre:")

#persona = [34, nombre, "Rocka Village", "Masculino", 1000.20, True]

#print(persona[0], persona[1], persona[4])

#edades = [58, 32, 25, 40, 30, 23, 40]

#print(edades[3], edades[6])

# Operaciones de listas sobre mutabilidad

amigos = ["ana", "pedro", "pablo", "maria", "juan", "ana"]


# Agregar un elemento a la lista (append, insert)

#amigos.append("jose")
amigos.insert(1, "jose")

# Borrar un elemento de una lista

#amigos.pop() # Elimina el último elemento de la lista
amigos.pop(2) # Elimina el elemento en el índice n
amigos.remove("pablo") # Elimina el primer elemento conociendo el valor

# Modificar un elemento de una lista

amigos[0] = "ana maria"
amigos[4] = "ana emilia"


print(amigos)

numeros = [1,2,3,4,5,6,1,1,1,1,1,4,4,4,4]

numeros.remove(1)

print(numeros, len(numeros)) # len() devuelve la cantidad de elementos que tiene la lista


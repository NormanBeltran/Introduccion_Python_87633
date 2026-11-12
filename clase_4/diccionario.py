"""

Diccionarios

En python cada elemento se compone de dos partes clave, valor 

Clave: es única
Valor: podria repetirse

diccionario = { "clave1": "valor1", "clave2": "valor2", "clave3": "valor1" }

Mutabilidad: Los diccionarios SON MUTABLES

"""

paises = { "Argentina": 47, "Paraguay": 6, "Uruguay": 3.5, "Chile": 20, "Brasil": 211}

# Agregar, modificar (valor), eliminar

paises["Colombia"] = 88

paises["Colombia"] = 53

del paises["Uruguay"]

print(paises)
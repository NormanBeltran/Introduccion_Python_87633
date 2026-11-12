"""
Bucle:

for

1. Recorrer una estructura iterable como la lista
2. Complementando con una funcion llamada range

"""

hobbies = [ "guitarra", "bailar", "salsa", "gym", "ajedrez", "futbol", "pintura", "series", "piano"]
n = 1

for h in hobbies:
    print("el hobby numero", n, " del equipo es:", h)
    n = n + 1

"""

Uso del for con range()

"""    
print("_____________________________________________________________")    
for i in range(7): # 0,1,2,3,4,5,6
    print("i=", i)

print("_____________________________________________________________")    
for i in range(10,20): # Empieza con 10, y termina con 19
    print("i=", i)

print("_____________________________________________________________")    

for i in range(10,100,15):
    print("i=", i)
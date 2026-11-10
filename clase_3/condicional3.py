"""

Si el cliente tiene menos de 20 años ==> de 5%
Si el cliente tiene menos de 40 años ==> de 15%
Si el cliente tiene menos de 60 años ==> de 45%
Si el cliente tiene mas o igual a 60 años ==> de 50%

"""
"""
edad = int(input("Ingrese su edad:"))

descuento = 0

if edad < 60:
    descuento = 45
    if edad < 40: 
        descuento = 15
        if edad < 20:
            descuento = 5

if edad >= 60:
    descuento = 50

print("Edad:", edad, " Descuento que aplica:", descuento)                
"""

edad = int(input("Ingrese su edad:"))

descuento = 0

if   edad < 20:
    descuento = 5
elif edad < 40:
    descuento = 15
elif edad < 60:
    descuento = 45
else:
    descuento = 50            

print("Edad:", edad, " Descuento que aplica:", descuento)      
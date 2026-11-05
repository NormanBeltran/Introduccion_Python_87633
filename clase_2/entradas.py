"""
input() instruccion mediante la cual pedimos datos por pantalla

"""

nombre = input("Cual es tu nombre? ")
edad = input("Cuantos años tenes? ") # input() siempre devuelve un string
saldo = input("Cual es tu saldo de cuenta bancaria? ")

edad = int(edad) # conversión de un str a un int
saldo = float(saldo)

print("Hola como estas:", nombre, "?")
print("En tu proximo cumple vas a tener  ", edad+1, "años")
print("Tu saldo es ", saldo)

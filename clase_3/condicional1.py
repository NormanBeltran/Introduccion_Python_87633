edad = int(input("Ingresa tu edad:"))

# Analiza si por la edad la persona esta habilitada para votar

print("Tu edad es ", edad)

if  edad >= 16:
    print("La persona puede votar")
    print("Por favor, dirigirse al fiscal de mesa")
    print("quien le asignara el cuarto oscuro")
else:  
    print("Ud no esta habilitado a votar por su edad")  


print("FIN DE PROGRAMA")
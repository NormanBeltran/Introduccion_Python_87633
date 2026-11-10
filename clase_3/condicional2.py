"""
Si el usuario es juanperez es administrador, cualquier otro usuario no es admin

"""

user = input("Ingrese su usuario:")

if user == "juanperez":
    print("juanperez es administrador y tiene accesos a toda la funcionalidad")
    print("del sistema y demas aplicaciones")
else:
    print("el usuario", user, "no tiene permisos de administrador")    
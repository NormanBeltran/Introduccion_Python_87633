"""
Rol de usuarios:

- admin
- jefe
- supervisor
- administrativo

"""

rol = "secretaria"

categoria = 0

if rol == "admin":
    categoria = 5
elif rol == "jefe":
    categoria = 4
elif rol == "supervisor":
    categoria = 3
elif rol == "administrativo":
    categoria = 2
else:
    categoria = -1

print("Rol:", rol, " Categoria:", categoria)
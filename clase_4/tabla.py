numero = input("Ingrese un numero para conocer la tabla de multiplicar de ese numero:")
numero = int(numero)

for i in range(10):
    print(numero, "*", (i+1), " = ", (i+1)*numero)

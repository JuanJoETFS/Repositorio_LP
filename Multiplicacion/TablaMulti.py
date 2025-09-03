#Programa para crear la tabla de multiplicar de un numero dado

#Funcion para generar la tabla de multiplicar
numero = int(input("ingrese numero para generar tabla "))

#Imprimir la tabla de multiplicar

print(f"Tabla de multiplicar del {numero}:")

for i in range(1,11):
    resultado = numero * i
    print(f"{numero} X {i} = {resultado}")
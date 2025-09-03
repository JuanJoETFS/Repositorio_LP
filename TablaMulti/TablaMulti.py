# Programa para crear la tabla de multiplicar de un número dado.

# Función para generar la tabla de multiplicar
numero = int(input("Ingrese un número para generar su tabla de multiplicar: "))

# Imprimir la tabla de multiplicar

print(f"Tabla de multiplicar del {numero}:")

for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} * {i} = {resultado}")

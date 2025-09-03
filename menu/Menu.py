 # -*-coding:utf-8 -*-
 """

 ========================================================
 |                  CALCULADORA SIMPLE - MENU
 ========================================================

Este programa es una calculadora con menu interactivo que permite
realizar operaciones basicas  como: suma, resta, multiplicacion y division

 Autor: Juan Jose Restrepo
 Fecha: 2025-08-13
 """ 

 #Crear un bucle infinito para mostrar el menu hasta que el usuario desee salir
 while True: 
    print("\n=== MENÚ DE LA CALCULADORA===")
    print("1. sumar")
    print("2. restar")
    print("3. multiplicar")
    print("4. dividir")
    print("5. salir")
    #Solicitar al usuario que elija una opcion del menú
    opcion = input("Selecciona una opcion 1-5:")

# ================ OPERACIONES==============

# Opcion 1: Sumar
if opcion  == "1":
    num1 = float(input("Ingrese el primer numero:"))
    num2 = float(input("ingrese el segundo numero:"))
    resultado = num1 + num2 
    print(f"La suma de {num1} y {num2} es: {resultado}")


#Opcion 2: Resta
elif opcion  == "2":
    num1 = float(input("Ingrese el primer numero:"))
    num2 = float(input("ingrese el segundo numero:"))
    resultado = num1 - num2 
    print(f"La resta de {num1} y {num2} es: {resultado}")

#Opcion 3: multiplicar
elif opcion  == "3":
    num1 = float(input("Ingrese el primer numero:"))
    num2 = float(input("ingrese el segundo numero:"))
    resultado = num1 * num2 
    print(f"La multiplicacion de {num1} y {num2} es: {resultado}")

#Opcion 4: division
elif opcion  == "4":
    num1 = float(input("Ingrese el primer numero:"))
    num2 = float(input("ingrese el segundo numero:"))
    resultado = num1/num2 
    print(f"La division de {num1} y {num2} es: {resultado}")
    
    if num2 == 0:
    print("Error, no se puede dividir por cero")

    # Opcion 5: Salir
    elif opcion == "5":
        print("Saliendo del programa")
        break


    # Caso por defecto: opcion no valida
    else:
        print("Opcion no valida, porfavor ingrese una opcion valida")
        # Se agrega una pausa para que el usuario pueda ver el resultado antes de continuar
        input("Presione enter para continuar")
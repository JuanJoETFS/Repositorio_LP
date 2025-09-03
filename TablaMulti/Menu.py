# -*- coding: utf-8 -*-
"""
=================================================================
|               CALCULADORA SIPLE - MENU                         |
=================================================================

Este program es una calculadora con un menu interactivo que permite
realizar operaciones básicas como suma, resta, multiplicación y división.

Autor: Feibert Guzmán 
Fecha: 2025-08-13
"""

# Crear un bucle infinito para mostrar el menú hasta que el usuario decida salir
while True:
    print("\n=== MENÚ DE LA CALCULADORA ===")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")

    # Solicitar al usuario que elija una opción del menú
    opcion = input("Seleccione una opción (1-5): ")

    # ==============OPERACIONES================

    # Opción 1: Sumar
    if opcion == "1":
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        resultado = num1 + num2
        print(f"La suma de {num1} y {num2} es: {resultado}")

    # Opción 2: Restar
    elif opcion == "2":
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        resultado = num1 - num2
        print(f"La resta de {num1} y {num2} es: {resultado}")
    # Opción 3: Multiplicar
    elif opcion == "3":
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        resultado = num1 * num2
        print(f"La multiplicación de {num1} y {num2} es: {resultado}")
    # Opción 4: Dividir
    elif opcion == "4":
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        if num2 == 0:
            print("Error: No se puede dividir por cero.")
        else:
            resultado = num1 / num2
            print(f"La división de {num1} entre {num2} es: {resultado}")
    # Opción 5: Salir
    elif opcion == '5':
        print("Saliendo del programa. ¡Hasta luego!")
        break

    # Caso por defecto: Opción no válida}
    else:
        print("Opción no válida. Por favor, elija una opción del 1 al 5.")

    # Se agrega una pausa para que el usuario pueda ver el resultado antes de continuar
    input("Presione Enter para continuar...")

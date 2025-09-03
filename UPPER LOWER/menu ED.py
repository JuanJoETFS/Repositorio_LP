import os

def limpiar_pantalla():
    """Limpia la pantalla según el sistema operativo"""
    os.system('cls' if os.name == 'nt' else 'clear')

def decorar_menu():
    """Agrega una decoración simple al menú"""
    print("=" * 50)
    print("  SISTEMA DE EJEMPLOS DE VENTAS  ".center(50))
    print("=" * 50)

def ejemplo_listas():
    """Ejemplo de listas aplicadas a ventas"""
    print("\n" + "=" * 20 + " EJEMPLO DE LISTAS " + "=" * 20)
    
    # Lista de productos vendidos
    ventas = ["Laptop", "Mouse", "Teclado", "Monitor", "Laptop", "Mouse"]
    print(f"\nVentas del día: {ventas}")
    
    # Operaciones con listas
    print("\nOperaciones con listas:")
    print(f"- Total de ventas: {len(ventas)} productos")
    print(f"- Primera venta: {ventas[0]}")
    print(f"- Última venta: {ventas[-1]}")
    
    # Agregar nueva venta
    ventas.append("Webcam")
    print(f"\nNueva venta agregada: {ventas[-1]}")
    print(f"Ventas actualizadas: {ventas}")
    
    # Contar productos específicos
    producto = "Laptop"
    print(f"\nVeces que se vendió '{producto}': {ventas.count(producto)}")
    
    # Eliminar producto
    ventas.remove("Teclado")
    print(f"\nSe eliminó la venta de 'Teclado'")
    print(f"Ventas actualizadas: {ventas}")

def ejemplo_tuplas():
    """Ejemplo de tuplas aplicadas a ventas"""
    print("\n" + "=" * 20 + " EJEMPLO DE TUPLAS " + "=" * 20)
    
    # Tupla con información de producto
    producto = ("Laptop Dell XPS", 1200.50, 10, "Electrónica")
    nombre, precio, stock, categoria = producto
    
    print(f"\nInformación del producto:")
    print(f"- Nombre: {nombre}")
    print(f"- Precio: ${precio:.2f}")
    print(f"- Stock disponible: {stock} unidades")
    print(f"- Categoría: {categoria}")
    
    # Tupla de ventas inmutables
    ventas_registradas = (
        ("2023-10-01", "Laptop", 1),
        ("2023-10-01", "Mouse", 2),
        ("2023-10-02", "Teclado", 1)
    )
    
    print(f"\nRegistro de ventas (inmutable):")
    for fecha, producto, cantidad in ventas_registradas:
        print(f"- {fecha}: {cantidad} {producto}(s)")
    
    # Intento de modificación (generará error)
    print("\nIntentando modificar una tupla...")
    try:
        # ventas_registradas[0] = ("2023-10-03", "Monitor", 1)  # Esto generaría un error
        print("Las tuplas son inmutables, no se pueden modificar después de creadas")
    except TypeError as e:
        print(f"Error: {e}")

def ejemplo_diccionarios():
    """Ejemplo de diccionarios aplicados a ventas"""
    print("\n" + "=" * 20 + " EJEMPLO DE DICCIONARIOS " + "=" * 20)
    
    # Diccionario de productos con precios
    productos = {
        "Laptop": 1200.50,
        "Mouse": 25.75,
        "Teclado": 45.30,
        "Monitor": 300.00
    }
    
    print("\nCatálogo de productos:")
    for producto, precio in productos.items():
        print(f"- {producto}: ${precio:.2f}")
    
    # Ventas realizadas
    ventas = {
        "Laptop": 3,
        "Mouse": 5,
        "Teclado": 2
    }
    
    print("\nVentas realizadas:")
    for producto, cantidad in ventas.items():
        print(f"- {producto}: {cantidad} unidades")
    
    # Calcular total de ventas
    total = sum(productos[producto] * cantidad 
               for producto, cantidad in ventas.items())
    print(f"\nTotal de ventas: ${total:.2f}")
    
    # Agregar nueva venta
    ventas["Monitor"] = 1
    print(f"\nNueva venta registrada: 1 Monitor")
    
    # Actualizar precio
    productos["Mouse"] = 22.50
    print(f"Precio actualizado de Mouse: ${productos['Mouse']:.2f}")

def ejemplo_conjuntos():
    """Ejemplo de conjuntos aplicados a ventas"""
    print("\n" + "=" * 20 + " EJEMPLO DE CONJUNTOS " + "=" * 20)
    
    # Conjuntos de productos vendidos por día
    lunes = {"Laptop", "Mouse", "Teclado", "Monitor"}
    martes = {"Laptop", "Mouse", "Webcam", "Auriculares"}
    
    print(f"\nVentas del lunes: {lunes}")
    print(f"Ventas del martes: {martes}")
    
    # Operaciones con conjuntos
    print("\nOperaciones con conjuntos:")
    print(f"- Productos vendidos ambos días (intersección): {lunes & martes}")
    print(f"- Todos los productos vendidos (unión): {lunes | martes}")
    print(f"- Productos vendidos solo el martes (diferencia): {martes - lunes}")
    
    # Verificar si un producto fue vendido
    producto = "Tablet"
    print(f"\n¿Se vendió '{producto}' el lunes? {'Sí' if producto in lunes else 'No'}")
    
    # Agregar nuevo producto
    lunes.add("Impresora")
    print(f"\nNueva venta agregada el lunes: Impresora")
    print(f"Ventas actualizadas del lunes: {lunes}")
    
    # Eliminar producto
    martes.discard("Auriculares")
    print(f"\nSe eliminó la venta de 'Auriculares' el martes")
    print(f"Ventas actualizadas del martes: {martes}")

def main():
    """Función principal del programa"""
    while True:
        limpiar_pantalla()
        decorar_menu()
        
        print("\nMENÚ DE OPCIONES:")
        print("1. Ejemplos de Listas en Ventas")
        print("2. Ejemplos de Tuplas en Ventas")
        print("3. Ejemplos de Diccionarios en Ventas")
        print("4. Ejemplos de Conjuntos en Ventas")
        print("5. Salir")
        
        opcion = input("\nSelecciona una opción (1-5): ")
        
        if opcion == "1":
            ejemplo_listas()
        elif opcion == "2":
            ejemplo_tuplas()
        elif opcion == "3":
            ejemplo_diccionarios()
        elif opcion == "4":
            ejemplo_conjuntos()
        elif opcion == "5":
            print("\n¡Gracias por usar el sistema! Hasta pronto.")
            break
        else:
            print("\nOpción no válida. Por favor, selecciona una opción entre 1 y 5.")
        
        input("\nPresiona Enter para continuar...")

if __name__ == "__main__":
    main()
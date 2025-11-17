import os

FILENAME = "productos.txt"

def crear_archivo_inicial():
    if not os.path.exists(FILENAME):
        with open(FILENAME, "w", encoding="utf-8") as f:
            f.write("Lapicera,120.5,30\n")
            f.write("Cuaderno,450.0,15\n")
            f.write("Mochila,3200.0,5\n")

def leer_productos():
    productos = []
    with open(FILENAME, "r", encoding="utf-8") as f:
        for linea in f:
            linea = linea.strip()
            if linea == "":
                continue
            nombre, precio, cantidad = linea.split(",")
            producto = {
                "nombre": nombre,
                "precio": float(precio),
                "cantidad": int(cantidad)
            }
            productos.append(producto)
    return productos

def mostrar_productos(productos):
    for p in productos:
        print(f"Producto: {p['nombre']} | Precio: ${p['precio']} | Cantidad: {p['cantidad']}")

def agregar_producto_desde_teclado(productos):
    entrada = input("Ingrese nuevo producto (nombre,precio,cantidad): ")
    nombre, precio, cantidad = entrada.strip().split(",")
    nuevo = {
        "nombre": nombre,
        "precio": float(precio),
        "cantidad": int(cantidad)
    }
    # agregar a la lista en memoria
    productos.append(nuevo)
    # agregar al archivo sin borrar contenido
    with open(FILENAME, "a", encoding="utf-8") as f:
        f.write(f"{nombre},{precio},{cantidad}\n")
    print("Producto agregado.")

def buscar_producto(productos):
    termino = input("Ingrese el nombre del producto a buscar: ")
    encontrado = False
    for p in productos:
        if p["nombre"].lower() == termino.lower():
            print(f"Producto encontrado: Nombre: {p['nombre']} | Precio: ${p['precio']} | Cantidad: {p['cantidad']}")
            encontrado = True
    if not encontrado:
        print("Error: producto no encontrado.")

def guardar_productos(productos):
    with open(FILENAME, "w", encoding="utf-8") as f:
        for p in productos:
            f.write(f"{p['nombre']},{p['precio']},{p['cantidad']}\n")
    print("Archivo sobrescrito con los productos actuales.")

def menu():
    crear_archivo_inicial()
    productos = leer_productos()
    while True:
        print("\n--- Menu ---")
        print("1 - Mostrar productos")
        print("2 - Agregar producto")
        print("3 - Buscar producto")
        print("4 - Guardar (sobrescribir archivo)")
        print("5 - Salir")
        opcion = input("Ingrese una opcion: ")
        if opcion == "1":
            productos = leer_productos()
            mostrar_productos(productos)
        elif opcion == "2":
            productos = leer_productos()
            agregar_producto_desde_teclado(productos)
        elif opcion == "3":
            productos = leer_productos()
            buscar_producto(productos)
        elif opcion == "4":
            productos = leer_productos()
            guardar_productos(productos)
        elif opcion == "5":
            break
        else:
            print("Opcion invalida.")

if __name__ == "__main__":
    menu()

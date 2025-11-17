# PRACTICO 6 - ESTRUCTURAS DE DATOS COMPLEJAS

# 1) Diccionario de precios de frutas
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

print("1) Diccionario con frutas agregadas:")
print(precios_frutas)
print()


# 2) Actualizar precios
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

print("2) Diccionario con precios actualizados:")
print(precios_frutas)
print()


# 3) Lista solo con nombres de frutas
lista_frutas = list(precios_frutas.keys())

print("3) Lista de frutas:")
print(lista_frutas)
print()


# 4) Agenda telefónica simple
telefonos = {}
print("4) Cargar agenda telefonica")

for i in range(5):
    nombre = input("Ingresar nombre: ")
    numero = input("Ingresar numero: ")
    telefonos[nombre] = numero

consulta = input("Ingresar nombre a consultar: ")

if consulta in telefonos:
    print("Numero:", telefonos[consulta])
else:
    print("El contacto no existe")

print()


# 5) Frase: palabras únicas y conteo
print("5) Analisis de frase")

frase = input("Ingresar frase: ")
palabras = frase.split()

unicas = set(palabras)
print("Palabras unicas:", unicas)

conteo = {}
for palabra in palabras:
    if palabra in conteo:
        conteo[palabra] += 1
    else:
        conteo[palabra] = 1

print("Conteo de palabras:", conteo)
print()


# 6) Alumnos y promedio con tuplas
print("6) Promedio de 3 alumnos")

alumnos = {}

for i in range(3):
    nombre = input("Ingresar nombre del alumno: ")
    nota1 = int(input("Nota 1: "))
    nota2 = int(input("Nota 2: "))
    nota3 = int(input("Nota 3: "))
    alumnos[nombre] = (nota1, nota2, nota3)

for nombre in alumnos:
    notas = alumnos[nombre]
    promedio = (notas[0] + notas[1] + notas[2]) / 3
    print(nombre, "promedio:", promedio)

print()


# 7) Sets de estudiantes aprobados
print("7) Sets de aprobados")

parcial1 = {1, 2, 3, 4, 5}
parcial2 = {4, 5, 6, 7}

ambos = parcial1 & parcial2
solo_uno = parcial1 ^ parcial2
al_menos_uno = parcial1 | parcial2

print("Aprobaron ambos:", ambos)
print("Aprobaron solo uno:", solo_uno)
print("Aprobaron al menos uno:", al_menos_uno)
print()


# 8) Stock de productos
print("8) Manejo de stock de productos")

stock = {
    "pan": 50,
    "leche": 30,
    "huevos": 12
}

producto = input("Ingresar producto: ")

if producto in stock:
    print("Stock actual:", stock[producto])
    agregar = int(input("Unidades a agregar: "))
    stock[producto] = stock[producto] + agregar
else:
    nuevo_stock = int(input("Producto nuevo. Ingresar stock: "))
    stock[producto] = nuevo_stock

print("Stock actualizado:")
print(stock)
print()


# 9) Agenda con claves tupla
print("9) Agenda con clave (dia, hora)")

agenda = {
    (1, 9): "Reunion",
    (2, 14): "Medico",
    (5, 20): "Gimnasio"
}

dia = int(input("Ingresar dia: "))
hora = int(input("Ingresar hora: "))

clave = (dia, hora)

if clave in agenda:
    print("Actividad:", agenda[clave])
else:
    print("No hay actividad")

print()


# 10) Diccionario invertido (capital: pais)
print("10) Diccionario invertido capital:pais")

paises = {
    "Argentina": "Buenos Aires",
    "Chile": "Santiago",
    "Peru": "Lima",
    "Uruguay": "Montevideo"
}

capital_a_pais = {}

for pais in paises:
    capital = paises[pais]
    capital_a_pais[capital] = pais

print(capital_a_pais)

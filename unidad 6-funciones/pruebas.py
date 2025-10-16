#Trabajo Practico: Funciones

#1 

"""def saludo():
    print("Hola mundo")

saludo()   """

#2 

"""def saludo_pers(nombre):
    print(f"Hola {nombre}")
    
   
saludo_pers("Juani")"""

#3
"""nombre = input("Dime tu nombre: ")
apellido = input("Dime tu apellido: ")
edad = int(input("Dime tu edad: "))
residencia = input("Dime donde vives: ")
def informacion_personal(nombre, apellido, edad, lugarResidencia,):
    print(f"Hola soy {nombre} {apellido}, tengo {edad} años, y vivo en {lugarResidencia}.")

informacion_personal(nombre, apellido, edad, residencia)"""

#4
"""import math
def calcular_area_circulo():
    radio = float(input("dime el radio y te doy la base: "))
    area = math.pi * radio ** 2
    print(f"El area es: {area}")
def calcular_perimetro_circulo():
    radio = float(input("dime el radio y te doy el perimetro: "))
    perimetro = 2 * math.pi * radio
    print(f"El perimetro es: {perimetro}")

calcular_area_circulo()
calcular_perimetro_circulo()"""

#5

"""def segundos_a_horas(segundos):
    return segundos / 3600

segundos = int(input("Ingrese la cantidad de segundos: "))
horas = segundos_a_horas(segundos)

print(f"{segundos} segundos equivalen a {horas} horas") """



#6
"""def calcular_tabla():

    numero = int(input("dime un numero: "))
    for x in range(11):
        print(f"{numero} * {x} = {numero*x}")

calcular_tabla()"""

#7 
"""import math

def operaciones_basicas():
    a = int(input("dime el primer numero: "))
    b = int(input("dime el segundo numero: "))
    tupla = (a + b, a*b, a - b, a / b)
    print(f"{tupla}")
operaciones_basicas()"""
#8
"""def calcular_imc(peso, altura):
    return peso / (altura ** 2)

peso = float(input("Ingrese su peso en kilogramos: "))
altura = float(input("Ingrese su altura en metros: "))

imc = calcular_imc(peso, altura)
print(f"Su IMC es: {imc}")"""


# 9
"""def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

celsius = float(input("Ingrese la temperatura en grados Celsius: "))
fahrenheit = celsius_a_fahrenheit(celsius)

print(f"{celsius} °C equivalen a {fahrenheit} °F")"""

#  10

"""def calcular_promedio(a, b, c):
    return (a + b + c) / 3

a = float(input("Ingrese el primer número: "))
b = float(input("Ingrese el segundo número: "))
c = float(input("Ingrese el tercer número: "))

promedio = calcular_promedio(a, b, c)
print(f"El promedio de los tres números es: {promedio}")"""
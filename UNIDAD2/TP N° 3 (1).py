
#Actividad1

edad = int(input("Ingrese su edad: "))
if edad >18:
    print ("Es mayor de edad")

#Actividad2

nota = int(input("Ingrese su nota:"))
if nota >= 6:
    print ("Aprobado")
else: print ("Desaprobado")

#Activiadad3

num = int(input("Ingrese un numero: "))
if num % 2 == 0 :
    print("Ha ingresado un numero par")
else: 
    print("Por favor, ingrese un número par")

#Actividad4

edad = int(input("Ingrese su edad: "))
if edad >= 0 and edad <= 12:
    print("Eres un niño/a.")
elif edad >= 12 and edad < 18:
    print("Eres un adolecente.")
elif edad >=18 and edad < 30:
    print("Eres un adulto/a joven.")
elif edad >= 30:
    print("Eres un adulto.")

#Actividad5

contraseña = input("Ingrese una contraseña: ")

if 8 <= len(contraseña) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

#Actividad6
 

import random
from statistics import mode, median, mean


numeros_aleatorios = [random.randint(1, 100) for i in range(50)]


la_moda = mode(numeros_aleatorios)
la_mediana = median(numeros_aleatorios)
la_media = mean(numeros_aleatorios)

print("Lista de números generados:", numeros_aleatorios)
print("Moda:", la_moda)
print("Mediana:", la_mediana)
print("Media:", la_media)

if la_media > la_mediana and la_mediana > la_moda:
    sesgo = "Sesgo positivo o a la derecha"
elif la_media < la_mediana and la_mediana < la_moda:
    sesgo = "Sesgo negativo o a la izquierda"
elif la_media == la_mediana == la_moda:
    sesgo = "Sin sesgo"
else:
    sesgo = "Distribución no se ajusta claramente a un sesgo típico"

print("Resultado:", sesgo)

#Actividad7

texto = input("Ingrese una palabra o frase: ")

if texto[-1] in "aeiou":
    texto += "!"


print("Resultado:", texto)

#Actividad8

nombre= input("Ingrese su nombre: ")
opcion = int(input("Ingrese una opcion (1 = Mayusculas, 2 = Minusculas, 3 = Primera letra en mayuscula): "))
if opcion == 1 :
    resultado = nombre.upper()
elif opcion == 2:
    resultado = nombre.lower()
elif opcion == 3:
    resultado = nombre.title()
else:
    resultado = "Opcion no valida."
print ("resultado: ", resultado)

#Actividad9 

magnitud = float(input("Ingrese la magnitud del terremoto: "))

if magnitud < 3:
    print ("Muy leve (imperceptible)")
elif magnitud >= 3 and magnitud < 4:
    print ("Leve (ligeramente perceptible).")
elif magnitud >= 4 and magnitud < 5:
    print ("Moderado (Sentido por personas, pero generalmente no causa daños).")
elif magnitud >= 5 and magnitud < 6:
    print ("Fuerte (Puede causar daños en extructuras debiles).")
elif magnitud >= 6 and magnitud < 7:
    print ("Muy fuerte ( puede causar daños significativos).")
else:
    magnitud > 7
    print("Extremo (puede causar graves daños a gran escala)")

#Actividad10

hemisferio = input("¿En qué hemisferio se encuentra? (N/S): ")
mes = int(input("¿Mes del año? (1-12): "))
dia = int(input("¿Día del mes? (1-31): "))

if (mes == 12 and dia >= 21) or (mes in [1, 2]) or (mes == 3 and dia <= 20):
    estacion_n = "Invierno"
    estacion_s = "Verano"
elif (mes == 3 and dia >= 21) or (mes in [4, 5]) or (mes == 6 and dia <= 20):
    estacion_n = "Primavera"
    estacion_s = "Otoño"
elif (mes == 6 and dia >= 21) or (mes in [7, 8]) or (mes == 9 and dia <= 20):
    estacion_n = "Verano"
    estacion_s = "Invierno"
else:
    estacion_n = "Otoño"
    estacion_s = "Primavera"

if hemisferio.upper() == "N":
    print("Estás en", estacion_n)
else:
    print("Estás en", estacion_s)



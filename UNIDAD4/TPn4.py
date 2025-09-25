#RESPUESTAS: 

#1)
"""for i in range(101):
    print(i)"""

#2)

"""numero = int(input("ingrese un numero entero"))
 
contador = 0
while numero > 0:
        numero = numero // 10  
        contador += 1

print("El número tiene", contador, "digitos.")"""
 
#3
"""
numero1 = int(input("ingrese el primer numero")) 
numero2 = int(input("ingrese el segundo numero"))
suma = 0
for i in range(numero1 +1 , numero2):
    suma = suma + i 
    
print(f"{suma}")"""

#4
"""total = 0

while True:
    numero_usuario = int(input("ingrese un numero entero"))
    if numero_usuario == 0:
        break
    total += numero_usuario
print(total)        """

#5
"""import random
numero_alea = random.randint(0, 9)
contador = 0
while True:
    numero_usuario = int(input("ingrese un numero"))
    if numero_alea == numero_usuario:
        break
    contador += 1
print("numero correcto")
print(f"la cantidad de intentos es: {contador}") """


#6
"""for i in range(100,-10, -1):
    if i %2 == 0:
     print(i)"""

#7

"""n = int(input("Ingresa un número entero positivo: "))
if n < 0:
    print("El número debe ser positivo.")
else:
    suma = sum(range(n + 1))
    print(f"La suma de los números entre 0 y {n} es: {suma}")"""


#8
"""cantidad = 10  #valor que se cambia para pruebas
pares = impares = positivos = negativos = 0

for i in range(cantidad):
    num = int(input(f"Ingrese el número {i+1}: "))
    
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1

    if num >= 0:
        positivos += 1
    else:
        negativos += 1

print(f"Cantidad de números pares: {pares}")
print(f"Cantidad de números impares: {impares}")
print(f"Cantidad de números positivos: {positivos}")
print(f"Cantidad de números negativos: {negativos}")  """   

#9

"""cantidad = 10
  # valor que se cambia para pruebas
suma = 0

for i in range(cantidad):
    num = int(input(f"Ingrese el número {i+1}: "))
    suma += num

media = suma / cantidad
print(f"La media de los {cantidad} números es: {media}")"""


#10

"""numero = input("Ingresa un número entero: ")

# Verifica si es negativo
if numero.startswith('-'):
    invertido = '-' + numero[:0:-1]
else:
    invertido = numero[::-1]

print(f"Número invertido: {invertido}")"""






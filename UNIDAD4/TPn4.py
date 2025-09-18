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
import random
numero_alea = random.randint(0, 9)
contador = 0
while True:
    numero_usuario = int(input("ingrese un numero"))
    if numero_alea == numero_usuario:
        break
    contador += 1
print("numero correcto")
print(f"la cantidad de intentos es: {contador}")







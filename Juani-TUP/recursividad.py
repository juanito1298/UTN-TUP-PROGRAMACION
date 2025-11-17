# 1) Factorial recursivo
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

# 2) Fibonacci recursivo
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

# 3) Potencia recursiva
def potencia(n, m):
    if m == 0:
        return 1
    return n * potencia(n, m - 1)

# 4) Decimal a binario recursivo
def decimal_a_binario(n):
    if n == 0:
        return ""
    resto = n % 2
    return decimal_a_binario(n // 2) + str(resto)

# 5) Palíndromo recursivo
def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])

# 6) Suma de dígitos recursiva
def suma_digitos(n):
    if n < 10:
        return n
    return (n % 10) + suma_digitos(n // 10)

# 7) Pirámide de bloques recursiva
def contar_bloques(n):
    if n == 1:
        return 1
    return n + contar_bloques(n - 1)

# 8) Contar apariciones de un dígito
def contar_digito(numero, digito):
    if numero == 0:
        return 0
    ultimo = numero % 10
    if ultimo == digito:
        return 1 + contar_digito(numero // 10, digito)
    return contar_digito(numero // 10, digito)

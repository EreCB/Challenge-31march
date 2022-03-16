# Activity Python 1: Function prototype, Sum


# Defining the sum function
def suma_enteros(int1, int2):
    suma = int1 + int2
    return suma


# Requesting user two numbers
print('===============================================')
print('= Bienvenido a la función para hacer una suma =')
print('= Por favor, introduce dos números enteros:   =\n')

num1 = int(input('Primer número entero: '))
num2 = int(input('Segundo número entero: '))

# Calling the sum function
suma = suma_enteros(num1, num2)

# Printing the result
print('\n= La suma de los números introducidos es: ', str(suma), '=')
print('===============================================')

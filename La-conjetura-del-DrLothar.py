"""
# La conjetura del Dr. Lothar

scriba un programa que reciba un numero del usuario y repita el siguiente proceso usando un while:

- Si el número es par, se debe dividir por 2
- Si el número es impar, se debe multiplicar por 3 y sumar 1.

Este proceso se repite hasta llegar al numero 1 y luego muestra en pantalla la cantidad de pasos que tardó en llegar. """

def lothar(n):
    steps = 0
    while not n == 1:
        steps += 1
        if (n % 2 == 0):
            n /= 2
        else:
            n = n * 3 + 1
    return steps

n = int(input())
print( lothar(n) )
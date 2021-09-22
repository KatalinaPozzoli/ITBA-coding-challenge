"""
La leyenda de Filius Bonacci
Imprima  𝑛  números de la sucesión de Fibonacci. """

def sucFibonacci(n):
  numBase = 0
  numSumando = 1
  print(numBase)
  print(numSumando)
  for i in range(n-2):
    suma = numBase + numSumando
    numBase = numSumando
    numSumando = suma
    print(numSumando)

sucFibonacci(16)
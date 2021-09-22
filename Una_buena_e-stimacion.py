"""
Una buena e-stimación

El número  𝑒  tiene inmensa utilidad para el análisis y la estadística, es una de las super-estrellas de la matemática, y su utilidad radica en que la función  𝑒𝑥  es igual a su derivada, por definición de  𝑒 .

Gracias a las series de Taylor podemos obtener la siguiente definición del número  𝑒 :

𝑒=1+11!+12!+13!+14!+15!+...

Se pide obtener una aproximación del número  𝑒  calculando la suma de los primeros  20  términos de esta sucesión infinita.

Tips:

𝑛! = 1⋅2⋅3⋅ ... ⋅𝑛 . """

def factorial(n):
  a = 1
  for i in range(1, n+1):
    a *= i
  return a

def sumatoria(m, n, fn):
  ac = 0
  for i in range(m, n+1):
    ac += fn(i)
  return ac

def eulerSumPart(n):
  return 1/factorial(n)

def eulerEstim(n):
   return sumatoria(0, n, eulerSumPart)

eulerEstim(2000)

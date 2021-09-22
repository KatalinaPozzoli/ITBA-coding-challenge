"""
El rector maníaco

Se rumorea que al rector de una universidad le apasiona adivinar números. Cuando se cruza a alguien, ya sean alumnos o profesores, les pide que piensen un número. Luego, intenta adivinarlo mientras el alumno le indica si el número es mayor, menor o igual al que el rector esta adivinando.

Ahora les proponemos a ustedes realizar el programa que adivine un número que ustedes elijan, indicándole si los números que este propone son mayores o menores al elegido.

Ustedes pensarán en un número secreto (para este ejercicio consideremos que el número es menor a 10.000), luego el programa intenta adivinarlo. El usuario debe responder con el símbolo >, < ó =. En el caso de ser igual, el programa termina e imprime la cantidad de intentos que tardó, caso contrario, debe volver a intentar adivinar el número y se repite el procedimiento.

Desafío: Encontrar la estrategia que puede ejecutar la máquina para adivinar el número en la menor cantidad de intentos posible. """

def middleTerm(a,b):
  return int((b - a) / 2 + a)

def adivinador():
  cantIntentos = 1
  rangeLimit = 10000
  rangeInit = 0
  nextStep = middleTerm(rangeInit, rangeLimit)
  userInput = input(f"<, > o = que {nextStep} ?")

  while not userInput == "=":
    cantIntentos += 1
    if userInput == "<":
      rangeLimit = middleTerm(rangeInit, rangeLimit)
    if userInput == ">":
      rangeInit = middleTerm(rangeInit, rangeLimit)
    nextStep = middleTerm(rangeInit, rangeLimit)
    userInput = input(f"<, > o = que {nextStep} ?")


  print(f'Su numero es { nextStep }. Adivinado en { cantIntentos } intentos.')

adivinador()
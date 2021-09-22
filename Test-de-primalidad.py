"""
Test de primalidad

Escribir una función que recibe un número y devuelve True si el número es primo y False en caso contrario.

Mediante un for verificar la primalidad de los numeros del  1  al  20 , es decir, decidir si cada número es primo o no.

Tips:

Un número  𝑁  es primo cuando tiene exactamente  2  divisores ( 1  y  𝑁 ).
Sin embargo, alcanza con verificar que no es múltiplo de ningún número entre  2  y  𝑁‾‾√  (recordar que  𝑁‾‾√=𝑁0.5 )
El numero 1 NO es primo. """

def primo(n):
  for i in range(2, int(n ** 0.5) + 1):
    if n % i == 0:
      return False

  return False if n <= 1 else True

for e in range(1,21):
  print(f'{e} es primo? {primo(e)}')
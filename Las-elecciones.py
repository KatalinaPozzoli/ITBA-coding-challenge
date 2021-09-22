"""
El programa debe calcular el ganador de unas elecciones e imprimir su nombre, para este ejemplo se asume que no hay empates.

Los nombres y la cantidad de candidatos es desconocida.

Input Format

El programa primero recibe un número , la cantidad de votos totales que se realizaron. Luego recibe  votos en formato string, cada uno consiste en el nombre del candidato seleccionado.

Constraints


Output Format

El programa debe calcular el ganador de las elecciones e imprimir su nombre.

Sample Input 0

12
Mickey
Donald
Mickey
Minnie
Mickey
Goofy
Daisy
Goofy
Goofy
Minnie
Goofy
Donald
Sample Output 0

Goofy """

cantVotos = int(input())
votos = dict()
for c in range(cantVotos):
  c = input()
  votos[c] = votos[c] + 1 if c in votos else 1
print(max(votos, key=votos.get))
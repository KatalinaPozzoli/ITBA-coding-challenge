"""
Ahorcado
Los desafíos se entregan mediante esta página de HackerRank. Pueden ver un instructivo acerca del uso de la plataforma en este link.

Les proponemos programar el famoso juego "Ahorcado" donde un jugador ingresa una palabra y otro jugador intenta adivinarla. En cada turno, el segundo jugador indica una letra que cree que se encuentra en la palabra elegida.

Una vez que el segundo jugador adivina todas las letras que se encuentran en la palabra, el juego termina y se muestra la cantidad de intentos que fueron necesarios. En el caso de que la cantidad de intentos errados supere cierto límite, el juego termina y el segundo jugador pierde. En esta versión del juego, si se adivina una letra que aparece varias veces en la palabra, todas las ocurrencias cuentan como adivinadas.

Formato del input:

Primero se recibe la palabra que se debe adivinar (en mayúsculas).
Luego se recibe un número  𝑁 , la cantidad máxima de intentos errados.
Por último se recibe cierta cantidad de letras en mayúsculas, una por línea, sin repetir.
Formato del output:

En caso de que se haya adivinado la palabra antes de superar el límite  𝑁 , se imprime la cantidad de intentos que tardó en adivinar.

En caso de que se haya superado el límite  𝑁 , se imprime el número  0 .

Ejemplos:

Ejemplo 1

Input:

PYTHON
3
A
B
C
P
Y
T
H
O
N
Output:

9
Si bien el jugador tuvo tres intentos erróneos ('A','B' y 'C'), adivinó la palabra antes de equivocarse la cuarta vez y es por ello que se cuenta como partida ganada. A su vez, notar que el programa imprime la cantidad de turnos que se tardaron en adivinar la palabra.

Ejemplo 2:

Input:

IEEE
3
A
B
C
D
Output:

0
El jugador pierde ya que supera los 3 intentos errados ('A', 'B', 'C' y 'D') antes de adivinar las letras 'I' y 'E'. """

def ahorcado(palabra, maxErrados):
    contadorErrores = 0
    lista = list(palabra)
    cantidadIntentos = 0
    adivinado = False
    while contadorErrores <= maxErrados and not adivinado:
        letraIngresada = input()
        filtered = list(filter(lambda l: l != letraIngresada, lista))
        if len(filtered) == len(lista):
            contadorErrores += 1
        lista = filtered
        cantidadIntentos += 1
        adivinado = len(lista) == 0

    print(cantidadIntentos if adivinado else 0)


palabra = input()
maxErrados = int(input())

ahorcado(palabra, maxErrados)
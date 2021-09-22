"""
Cálculo de promedio

Cálcular la nota de un alumno es una tarea cotidiana de un profesor. Esta tarea suele realizarse a mano o en excel muchas veces. En esta ocasión la haremos en Python.

Escribir una función que calcule el promedio de 3 notas y entrege ese valor usando return.
Reescribir la función anterior modificándola para asignar una importancia al primer examen de 20%, al segundo de 50% y al tercero de 30%.
Llamar a cada función anterior 3 veces con distintas notas y verificar, mediante la instrucción if, si el alumno aprobó en cada caso (suponga que 4 es la nota de aprobación). """

#Primera parte del ejercicio

grade1 = int(input("ingrese la primera nota: "))
grade2 = int(input("ingrese la segunda nota: "))
grade3 = int(input("ingrese la tercera nota: "))

def average(gr1, gr2, gr3):
  sum = gr1 + gr2 + gr3
  return sum/3

average(grade1, grade2, grade3)


#Seguna parte del ejercicio

def average(gr1, gr2, gr3):
  sum = gr1 * 0.2 + gr2 * 0.5 + gr3 * 0.3
  return sum

grade1 = int(input("ingrese la primera nota: "))
grade2 = int(input("ingrese la segunda nota: "))
grade3 = int(input("ingrese la tercera nota: "))
average(grade1, grade2, grade3)


#Tercera parte del ejercicio

def average(gr1, gr2, gr3):
  return gr1 * 0.2 + gr2 * 0.5 + gr3 * 0.3

def approved():
  grade1 = int(input("ingrese la primera nota: "))
  grade2 = int(input("ingrese la segunda nota: "))
  grade3 = int(input("ingrese la tercera nota: "))

  averageGrade = average(grade1, grade2, grade3)
  if averageGrade >= 4:
    print(f"El alumno aprobó con {averageGrade}")
  else:
     print(f"El alumno desaprobó con {averageGrade}")

approved()
approved()
approved()
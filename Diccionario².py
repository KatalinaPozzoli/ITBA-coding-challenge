"""
Se recibieron distintos postulantes para un empleo de traductor. Crear un diccionario en el cual la clave de cada elemento sea el nombre de un candidato y el contenido sea un diccionario de los idiomas que aprendió. Para armar el diccionario de idiomas de cada candidato, los elementos deben tener como clave el nombre del idioma y como contenido el valor True o False para los siguientes idiomas: Español, Ingles, Chino, Frances, Italiano.

Ejemplo del diccionario de idiomas:

{"Español":True, "Ingles":True, "Chino":False, "Frances":False, "Italiano":True}
Inventar valores para 5 candidatos.

El usuario luego debe poder ingresar el nombre de un idioma y el programa deberá mostrar en pantalla el nombre de aquellos candidatos que aprendieron ese idioma. """

postulantes = {
    "Nicolas":{"Español":True, "Ingles":True, "Chino":False, "Frances":False, "Italiano":True} ,
    "valentina":{"Español":True, "Ingles":True, "Chino":False, "Frances":False, "Italiano":False},
    "Maria":{"Español":True, "Ingles":False, "Chino":False, "Frances":True, "Italiano":True},
    "Ignacio": {"Español":True, "Ingles":True, "Chino":True, "Frances":True, "Italiano":True},
    "Sebastian": {"Español":False, "Ingles":True, "Chino":False, "Frances":False, "Italiano":False},
    "Katalina": {"Español":False, "Ingles":True, "Chino":False, "Frances":True, "Italiano":False}
}

idioma = input("Ingrese un idioma")

for nombre, dicParticular in postulantes.items():

    if idioma in dicParticular:
      if (dicParticular[idioma]) == True:
        print(nombre, 'habla', idioma)
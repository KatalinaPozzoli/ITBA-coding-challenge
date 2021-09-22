"""
El ABC de Python
Aclaración: Este desafío es inventado, es posible que haya errores fácticos en cuanto a los alfabetos reales.

Encontramos una piedra antigua en una plaza de Buenos Aires cuyas inscripciones nos ayudan a decifrar nuevos alfabetos. Gracias a estas inscripciones descubrimos que las letras del alfabeto latino arcaico tienen una correspondencia con el alfabeto latino y vamos a crear un programa que nos ayude a traducir palabras de un alfabeto a otro.

Crear una función que recibe un string, transforma todos los caracteres del alfabeto latino arcaico en caracteres modernos, no modifica el resto de los caracteres (signos de puntuacion, espacios, letras, números, etc.) y devuelve el resultado con return.

Ejemplos:

traducir( "𐌀𐌋𐌅𐌀𐌁𐌄𐌕𐌏" ) → "ALFABETO"

traducir( "¡𐌐𐌄𐌓𐌃𐌉!" ) → "¡PERDI!"

traducir( "¿𐌔𐌉 𐌏 𐌍𐌏? 𐌌𐌌𐌌... 𐌔𐌉." ) → "¿SI O NO? MMM... SI."

Correspondencia entre alfabetos:

Arcaico : Moderno
'𐌀' : 'A',
'𐌁' : 'B',
'𐌂' : 'C',
'𐌃' : 'D',
'𐌄' : 'E',
'𐌅' : 'F',
'𐌆' : 'Z',
'𐌇' : 'H',
'𐌉' : 'I',
'𐌊' : 'K',
'𐌋' : 'L',
'𐌌' : 'M',
'𐌍' : 'N',
'𐌏' : 'O',
'𐌐' : 'P',
'𐌒' : 'Q',
'𐌓' : 'R',
'𐌔' : 'S',
'𐌕' : 'T',
'𐌖' : 'V',
'𐌗' : 'X' """

arcaico = {'𐌀' : 'A', '𐌁' : 'B', '𐌂' : 'C', '𐌃' : 'D', '𐌄' : 'E', '𐌅' : 'F',
           '𐌆' : 'Z', '𐌇' : 'H', '𐌉' : 'I', '𐌊' : 'K', '𐌋' : 'L', '𐌌' : 'M',
           '𐌍' : 'N', '𐌏' : 'O', '𐌐' : 'P', '𐌒' : 'Q', '𐌓' : 'R', '𐌔' : 'S',
           '𐌕' : 'T', '𐌖' : 'V', '𐌗' : 'X' }

def traducir(texto):
  resultado = ""
  for letra in texto:
    if letra in arcaico:
      resultado += arcaico[letra]
    else:
      resultado += letra
  return resultado

print(traducir("𐌀𐌋𐌅𐌀𐌁𐌄𐌕𐌏"))
print(traducir("¡𐌐𐌄𐌓𐌃𐌉!"))
print(traducir("¿𐌔𐌉 𐌏 𐌍𐌏? 𐌌𐌌𐌌... 𐌔𐌉."))
print(traducir("𐌀𐌋𐌅𐌀𐌁𐌄𐌕𐌏, ¡𐌐𐌄𐌓𐌃𐌉!, ¿𐌔𐌉 𐌏 𐌍𐌏? 𐌌𐌌𐌌... 𐌔𐌉."))

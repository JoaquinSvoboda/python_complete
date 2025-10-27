cadena1 = "hola soy joaco"
cadena2 = "bienvenido"

#convierte a mayusculas
resultado = cadena1.upper()

#convierte a minusculas
resultado = cadena1.lower()

#primera letra en mayuscula
resultado = cadena1.capitalize()

#buscamos una cadena en otra cadena, si no encuentra devuelve -1
resultado = cadena1.find('hola')

#buscamos una cadena en otra cadena, si no hay coincidencia lanza una excepcion

resultado = cadena1.index('j')

#si es numerico devuelve true

resultado = cadena1.isnumeric()

#si es alfanumerico devuelve true, sino false

resultado = cadena1.isalpha()

#contamos coincidencias en otra cadena, devuelve la cantidad de coincidencias

resultado = cadena1.count("a")

#contamos cuantos caracteres tiene una cadena 

resultado = len(cadena1)

#verifiamos si una cadena empieza con

resultado = cadena1.startswith("a")

#verifiamos si una cadena termina con

resultado = cadena1.endswith("a")

#reemplaza un pedazo de la cadena con ( sirve para reemplazar , por espacios por ejemplo)

resultado = cadena1.replace("la", "lu")

#separa cadenas con la cadena que elijamos pasarle (sirve para hacer matrices)

resultado = cadena1.split(" ")

print(resultado)
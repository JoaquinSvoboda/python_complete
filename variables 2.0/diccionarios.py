#creando diccionarios con dict

diccionario = dict(nombre = "joaco", apellido = "svoboda")

#las listas no pueden ser claves, laas tuplas SI 
#las listas solo pueden ser claves si les paso el frozenset
diccionario = {frozenset(["joaco","poki"]):"jajaja"}

#creando diccionarios con fromkeys()
diccionario = dict.fromkeys(["nombre","apellido"])

#creando diccionarios con fromkeys() con valor iterable
diccionario = dict.fromkeys("ABCD")

print(diccionario)
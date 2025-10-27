diccionario = {
    "nombre" : "joaco",
    "apellido" : "svoboda",
    "subs" : 90
}

#devuelve las claves y sirve para iterar
claves = diccionario.keys()

#get obteniendo un elemento con get, si no lo encuentra lanza un none y el programa continua
claves = diccionario.get("nombre")

#eliminando un elemento del diccionario con pop
diccionario.pop("nombre")

#obteniendo elementos de un diccionario iterable
diccionario_iterable = diccionario.items()

print(diccionario)
print(diccionario_iterable)
